import warnings
warnings.filterwarnings("ignore", category=FutureWarning)
import pandas as pd
import numpy as np
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer       # Data Cleaning
from sklearn.preprocessing import RobustScaler, OneHotEncoder, OrdinalEncoder # Data Transform
from collections import Counter
from sklearn.preprocessing import MultiLabelBinarizer
from sklearn.preprocessing import PowerTransformer
import ast

# Handle Genres, Producers, Studios
class MultiListModeImputer(BaseEstimator, TransformerMixin):
    '''
    Imputes list-like columns by replacing empty or invalid lists with the
    most frequent item (mode) found in that column.
    '''
    def __init__(self, columns):
        self.columns = columns
        self.modes_ = {}

    def _ensure_list(self, x):
        if isinstance(x, list):
            return x
        if pd.isna(x):
            return []
        if isinstance(x, str):
            try:
                return ast.literal_eval(x)
            except:
                return []
        return []

    def fit(self, X, y=None):
        for col in self.columns:
            temp = X[col].apply(self._ensure_list)
            all_items = []
            for lst in temp:
                all_items.extend(lst)

            if len(all_items) == 0:
                self.modes_[col] = None
            else:
                self.modes_[col] = Counter(all_items).most_common(1)[0][0]

        return self

    def transform(self, X):
        X = X.copy()
        for col in self.columns:
            mode_item = self.modes_[col]
            X[col] = X[col].apply(self._ensure_list)
            X[col] = X[col].apply(lambda lst: lst if len(lst) > 0 else [mode_item])
        return X

    def get_feature_names_out(self, input_features=None):
        return np.array(self.columns)

class FrequencyGrouper(BaseEstimator, TransformerMixin):
    '''
    Genre/Producer/Studios with frequency ≥ min_freq → keep name.
    Other Genre/Producer/Studio with frequency < min_freq → group into "Other".
    Help reduce Dimension

    '''
    def __init__(self, columns, min_freq):
        """
        columns: list các cột dạng list
        min_freq: dict chứa min_freq riêng cho từng cột
        """
        self.columns = columns
        self.min_freq = min_freq
        self.frequent_items_ = {}  # lưu item phổ biến của từng cột

    def _ensure_list(self, x):
        """Ensure input is in list form"""
        if isinstance(x, list):
            return x
        if pd.isna(x):
            return []
        if isinstance(x, str):
            try:
                return ast.literal_eval(x)
            except:
                return []
        return []

    def fit(self, X, y=None):
        for col in self.columns:
            min_f = self.min_freq.get(col, 10)  # default frequency is 10

            temp = X[col].apply(self._ensure_list)

            # Flatten
            all_items = []
            for lst in temp:
                all_items.extend(lst)

            counts = Counter(all_items)
            frequent = [k for k, v in counts.items() if v >= min_f]

            self.frequent_items_[col] = set(frequent)

        return self

    def transform(self, X):
        X = X.copy()

        for col in self.columns:
            freq_set = self.frequent_items_[col]

            X[col] = (
                X[col]
                .apply(self._ensure_list)
                .apply(lambda lst: [item if item in freq_set else "Other"
                                    for item in lst])
            )

        return X

    def get_feature_names_out(self, input_features=None):
        return np.array(self.columns)

class MultiLabelBinarizerDF(BaseEstimator, TransformerMixin):
    '''
    A custom transformer for multi-label columns.
    Converts each list-like column into multiple binary features using
    MultiLabelBinarizer, with feature names formatted as <col>__<label>.
    Supports get_feature_names_out() for pipeline compatibility.
    '''
    def __init__(self, columns):
        self.columns = columns
        self.encoders = {}
        self.output_features_ = []

    def fit(self, X, y=None):
        self.output_features_ = []
        for col in self.columns:
            mlb = MultiLabelBinarizer()
            mlb.fit(X[col])
            self.encoders[col] = mlb

            # store new feature name
            for c in mlb.classes_:
                self.output_features_.append(f"{col}__{c}")

        return self

    def transform(self, X):
        X = X.copy()
        encoded_list = []

        for col in self.columns:
            mlb = self.encoders[col]
            arr = mlb.transform(X[col])

            df_enc = pd.DataFrame(
                arr,
                index=X.index,
                columns=[f"{col}__{c}" for c in mlb.classes_]
            )
            encoded_list.append(df_enc)

        other_cols = X.drop(columns=self.columns)

        return pd.concat([other_cols] + encoded_list, axis=1)

    def get_feature_names_out(self, input_features=None):
        return np.array(self.output_features_)
    
# Aired Month encoder
class CyclicalMonthEncoder(BaseEstimator, TransformerMixin):
    def __init__(self, columns):
        self.columns = columns
        self.generated_features_ = []

    def fit(self, X, y=None):
        # Tạo danh sách tên feature sẽ sinh ra
        self.generated_features_ = []
        for col in self.columns:
            self.generated_features_.append(f"{col}_sin")
            self.generated_features_.append(f"{col}_cos")
        return self

    def transform(self, X):
        X = X.copy()

        for col in self.columns:
            # Fill missing
            X[col] = X[col].fillna(X[col].median()).astype(float)

            # Add sin/cos features
            X[col + "_sin"] = np.sin(2 * np.pi * X[col] / 12)
            X[col + "_cos"] = np.cos(2 * np.pi * X[col] / 12)

            X = X.drop(columns=[col])

        return X

    def get_feature_names_out(self, input_features=None):
        return np.array(self.generated_features_)


# Create New Feature
def create_interactions(df, pairs=[
    ('Episodes', 'duration_minutes')
]):
    df = df.copy()
    out = {}
    for a, b in pairs:
        out[f'{a}_x_{b}'] = df[a] * df[b]
    return pd.DataFrame(out, index=df.index)


def create_list_counts(df, columns):
    df = df.copy()
    out = {}
    for col in columns:
        out[col + "_Count"] = df[col].apply(lambda x: len(x) if isinstance(x, list) else 0)
    return pd.DataFrame(out, index=df.index)


class FeatureEngineering(BaseEstimator, TransformerMixin):
    def __init__(self,
                 year_col='air_year',
                 degree=2,
                 list_columns=['Genres', 'Producers', 'Studios'],
                 interaction_pairs=[('Episodes', 'duration_minutes')],
                 duration_col='duration_minutes',
                 duration_q=4,
                 episodes_col='Episodes',
                 episodes_q=4):

        # Inputs
        self.year_col = year_col
        self.degree = degree
        self.list_columns = list_columns
        self.interaction_pairs = interaction_pairs
        self.duration_col = duration_col
        self.duration_q = duration_q
        self.episodes_col = episodes_col
        self.episodes_q = episodes_q

        # Will be populated in fit()
        self.duration_bins = None
        self.episodes_bins = None

        # Meaningful labels
        self.duration_labels = ["Very Short", "Short", "Medium", "Long"]
        self.episodes_labels = ["Mini_Series", "Short_Series",
                                "Standard_Series", "Long_Running"]

    def fit(self, X, y=None):
        X = X.copy()

        # --- Compute quantile bins (train only) ---
        self.duration_bins = np.unique(
            np.quantile(
                X[self.duration_col].dropna(),
                np.linspace(0, 1, self.duration_q + 1)
            )
        )

        self.episodes_bins = np.unique(
            np.quantile(
                X[self.episodes_col].dropna(),
                np.linspace(0, 1, self.episodes_q + 1)
            )
        )

        return self

    def transform(self, X):
        X = X.copy()

        # Count list features
        df_list = create_list_counts(X, self.list_columns)

        # Interaction features
        df_inter = create_interactions(X, self.interaction_pairs)

        # --- DurationCat ---
        dur_numeric = pd.cut(
            X[self.duration_col],
            bins=self.duration_bins,
            labels=False,
            include_lowest=True
        )

        dur_labels = dur_numeric.map(
            lambda x: self.duration_labels[int(x)] if pd.notna(x) else np.nan
        )

        df_dur = pd.DataFrame({'DurationCat': dur_labels}, index=X.index)

        # --- EpisodesCat ---
        ep_numeric = pd.cut(
            X[self.episodes_col],
            bins=self.episodes_bins,
            labels=False,
            include_lowest=True
        )

        ep_labels = ep_numeric.map(
            lambda x: self.episodes_labels[int(x)] if pd.notna(x) else np.nan
        )

        df_ep = pd.DataFrame({'EpisodesCat': ep_labels}, index=X.index)

        # Combine all new features
        X_new = pd.concat([X, df_list, df_inter, df_dur, df_ep], axis=1)

        return X_new
