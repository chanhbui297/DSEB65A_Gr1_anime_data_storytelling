# 📘 The Power of Data Preparation through Data Storytelling
---
## 📋  Group Distribution

| STT | ID        | Full Name          | % Contribution |
|-----|-----------|--------------------|----------------|
| 01  | 11230508  | Bùi Châu Anh       | 17.2%          |
| 06  | 11230522  | Thành Uyển Dung    | 16.63%         |
| 09  | 11230529  | Vũ Tuấn Đạt        | 16.3%          |
| 16  | 11230544  | Đặng Nhật Huy      | 16.6%          |
| 33  | 11230584  | Chu Bích Phương    | 16.63%         |
| 37  | 11230592  | Phạm Vân Thư       | 16.63%         |

## 📋 README Structure
1. **Project Overview**: Short description & project structure  
2. **Dataset Description**: Source, size, features, raw vs. cleaned state, reason for choosing  
3. **Storytelling Context**: Business narrative & core message  
4. **Repository Structure**: Folder organization  
5. **Workflow (4-Phase Pipeline)**: Detailed phase-by-phase breakdown  
      - **Phase 1**. Explore raw data problems: `jupyter notebook notebooks/01_Diagnostic_EDA.ipynb`
      - **Phase 2**. Run data preparation: `jupyter notebook notebooks/02_Data_Preprocessing.ipynb`
      - **Phase 3**. Compare visual narratives (Before and After Data Preparation): `jupyter notebook notebooks/03_Comparative_Analysis.ipynb`
      - **Phase 4**. Validate with modeling: `jupyter notebook notebooks/04_Modeling_Comparison.ipynb`
 
6. **How to Run the Project**: Step-by-step execution guide  
7. **Key Findings & Conclusions**: Main insights & recommendations  
8. **License & References**

---

## 🔥 1. Project Overview

This project demonstrates the **critical role of Data Preparation** in any Machine Learning workflow by using **data storytelling techniques**.  
Through a series of visual narratives and analytical comparisons, we highlight how *raw data vs. prepared data* drastically impacts:

- **Insight quality** and visualization accuracy
- **Business interpretations** and decision-making
- **Machine Learning performance** and model reliability

---

## 📊 2. Dataset Description

### **2.1. Dataset Overview**
**Dataset:** *Anime Dataset 2023 (Kaggle)*  
**Initial Size:** ~25,000 entries, 24+ features  
**Final Processed Size:** ~15,692 entries, 12 engineered features

---

### **2.2. Why We Chose This Dataset** 
- **Rich narrative potential**: Anime scoring involves multiple factors (creative, production, timing) 
- **Complex data structure**: Contains multi-label fields, inconsistent formats, and mixed data types 
- **Real-world relevance**: Represents common data challenges in entertainment/media analytics 
- **Clear before/after contrast**: Dramatic improvements possible through proper preprocessing 

---

### **2.3. Raw vs. Processed State**

#### 🔶 **Raw State (Before Cleaning)**
**Size:** *24,905 entries × 24 features*

**Critical Issues Identified**
- **37% missing scores (target variable)**
- **81% missing licensor information**
- **78% missing premiere dates**
- **20+ inconsistent date formats** across the dataset  
- **Hidden missing values:** “Unknown”, “?”, “N/A”  
- **Logical conflicts:** *7,405 records have a ranking but no score*  
- **Type misclassification:**  
  - Movies listed with **>1 episode**  
  - Aldult Genre with Rating **PG - Children**  
- **Mixed data types** and unstructured multi-label fields (genres, studios, producers)

---

#### 🔷 **Processed State (After Cleaning)**
**Size:** *15,692 entries × 12 features*

**Quality Improvements**
- Removed structural inconsistencies  
- Resolved logical conflicts (ranking–score mismatch, invalid episode counts, etc.)  
- Standardized all date formats + extracted **Aired Year** & **Aired Month**  
- Normalized multi-label categorical fields  
- Created reproducible **preprocessing pipeline**  
- Engineered **seasonal/cyclical features** for modeling  
- Established a clean, stable dataset for analysis & storytelling

---

### **2.4. Key Feature Groups**

---

## 📁 **1. Basic Identification & Description**
- **anime_id** – Unique identifier for each anime  
- **Name** – Original Japanese title  
- **English name** – Official English title  
- **Other name** – Localized, alternative, or native titles  
- **Synopsis** – Brief plot description  
- **Genres** – Genre list (multi-label, comma-separated)  
- **Image URL** – Anime thumbnail/poster URL  

---

## 🎬 **2. Production & Technical Details**
- **Type** – TV / Movie / OVA / ONA / Special / Music  
- **Source** – Manga / Light Novel / Original / Game / Web Manga / etc.  
- **Producers** – Companies that funded or produced the anime  
- **Studios** – Animation studios responsible for production  
- **Licensors** – Companies licensing the anime (high missing rate)  
- **Episodes** – Total episode count  
- **Duration** – Runtime per episode (minutes)  

---

## 📡 **3. Release & Airing Information**
- **Aired** – Full airing period or release date  
- **Premiered** – Season + Year (e.g., *Fall 2023*)  
- **Status** – Finished / Currently Airing / Not Yet Aired  
- **Aired Year** – Extracted release year  
- **Aired Month** – Extracted release month (1–12)  

---

## ⭐ **4. Audience Engagement & Performance Metrics**
- **Score** – Average user rating  
- **Rating** – Age classification (PG-13, R, G…)  
- **Rank** – Score-based ranking  
- **Popularity** – Interaction-based popularity ranking  
- **Favorites** – Count of users marking as favorite  
- **Scored By** – Total number of user ratings  
- **Members** – Total number of users adding the anime to their list  

---

## 🎬 3. Storytelling Context & Business Narrative

**Business Context**: In the competitive Anime industry, understanding what drives high scores is crucial for producers, studios, and investors. However, raw anime data is notoriously messy — containing inconsistent formats, missing values, and structural errors that obscure true patterns.

**Narrative Arc**: This project follows a detective-style story:
1. **The Problem**: Raw data shows confusing, misleading patterns
2. **The Investigation**: Systematic diagnosis reveals deep structural issues
3. **The Transformation**: Comprehensive cleaning and feature engineering
4. **The Revelation**: Clean data uncovers true drivers of success
5. **The Proof**: Quantifiable improvement in model performance

**Core Message**: Data Preparation isn't just technical cleanup — it's the foundation that determines whether your analysis reveals truth or perpetuates misinformation.

---

## 📁 4. Repository Structure

```bash
anime-data-storytelling/
│
├── .gitignore                  
├── README.md                           # Project overview (this file)
├── requirements.txt                    # Python dependencies
│
├── data/   
│   ├── raw/
│   │   └── anime-dataset-2023.csv  
│   └── processed/
│       └── prepared_data.csv   
│
├── models/                              # Saved models & pipelines
│ ├── processing_pipeline.pkl                 # Data transformation pipeline
│ └── model.pkl                               # Trained Linear Regression model
│
├── src/                                 # Custom code
│ └── Custom_Transformer.py                   # Custom transformers for anime data
│
├── notebooks/                           # Main analysis notebooks
│ ├── 01_Diagnostic_EDA.ipynb                 # Phase 1: Problem diagnosis
│ ├── 02_Data_Preprocessing.ipynb             # Phase 2: Data preparation
│ ├── 03_Comparative_Analysis.ipynb           # Phase 3: Visualization & insights
│ └── 04_Modeling_Comparison.ipynb            # Phase 4: Model validation
│
├── plots/                               # Generated visualizations
│ ├── Plot_01/                               # Diagnostic charts
│ ├── Plot_03/                               # Exploratory charts
│ ├── Plot_04/                               # Clean data insights
│ └── Plot_ML_Models/                        # Model comparison charts
│
└── report/                               # Final Report
└── Final_Report_Group1.pdf                             

```

## 🔄 5. Workflow (4-Phase Pipeline)

### **📋 PHASE 1 — Diagnostic EDA ("The Data Doctor")**

### **1. Overview**
**Notebook:** `01_Diagnostic_EDA.ipynb`  
**Goal**: The primary purpose of Phase 1 is to **diagnose all data quality issues** that may distort analysis or produce misleading insights. This phase establishes the foundation for a reliable preprocessing pipeline.

---

### **2. Key Discoveries from Diagnostic EDA**

- **Type Mismatches**: Critical numeric columns (Score, Episodes, Rank) stored as strings

- **Hidden Missingness**: 
   - Instead of NaN, Missing values are stored as 'Unknown', 'not available', 'n/a', 'na', 'tbd', 'tba' 
   - All columns has missing values. Especially, Licensors has the highest pperrcentage of missing with over 80%. 

- **Skewed Distributions**: Engagement metrics (Members, Favorites) with 99th percentile outliers
- **Inconsistent Formating**: 
   - Datetime format: '1-Sep-01', 'Oct 20, 1999 to ?'
   - Durations: '3 min', '3 min per ep'

- **Multi-label in Genre, Producers, Studios**: ['Action','Sci-fi'] make it impossible for running model

- **Ghost Records**: 1,330 entries with zero engagement metrics and no metadata

- **Data Integrity and Misclassification in Type, Ratings, Duration, Episodes**: 
   - Movie with `Episodes > 1`, or Movies with less than 40 minutes
   - Labeled with Adult genre but has an All-Ages Rating 
   - Episode with Durations > 1000 minutes

- **Date Paradoxes**: 7 records with end dates before start dates

---

### **3. Conclusion**
Phase 1 confirms that the raw dataset is **not suitable for immediate analysis**.  Thus, a robust cleaning and transformation pipeline is required to ensure Structural consistency and Logical validity.  

This diagnostic stage sets the foundation for Phase 2: **Data Preparation & Pipeline Construction**.

---

### **🛠 PHASE 2 — Data Preparation & Pipeline Construction**

### **1. Overview**
**Notebook:** `02_Data_Preprocessing.ipynb` and `Customtransformer.py` 

**Goal**: Build reproducible cleaning and transformation pipeline that handle issues stated in PHASE 1

**Outputs**:
- `data/processed/prepared_data.csv` (cleaned dataset)
- `models/processing_pipeline.pkl` (reusable pipeline)
- `models/model.pkl` (reusable Linear Regressor model)
- `src/Custom_Transformer.py` (custom class transformation used for pipeline)

---

### **2. Processing Steps**:

### **2.1. Pre-split cleaning (Structural Fixes Before Train/Test Split)**

### **A. Goal**  
Transform the raw file **`anime-dataset-2023.csv`** into a clean, structurally consistent dataset **`prepared_data.csv`**, ensuring:  
- Correct data types  
- Standardized formats  
- Unified representation for multi-label fields  
- Removal or correction of malformed entries

---

### **B. Critical Principle — Why these steps MUST happen *before* splitting**

These operations address **structural and domain-logic corrections**, not statistical learning.  
Applying them post-split would produce inconsistent schemas between train/test.

| Reason | Explanation |
|--------|-------------|
| **1. Maintain structural consistency** | Fixing types, list formats, and date formats must apply to all rows. |
| **2. No learned parameters** | These operations do **not** compute statistics (mean, median, quantiles). |
| **3. Domain rules apply universally** | e.g., cleaning genres, standardizing format, converting data type 'object' to 'numeric' and 'datetime' |
| **4. Required for sklearn pipelines** | Downstream transformers expect consistent input schema. |

---

### **C. Main Steps (Structural Cleaning)**

**Step 1.  Standardize "NaN-like" Values**  
- **Strategy**: Many object columns use string literals to represent missing data. We'll replace them with `np.nan`
- **Example**: ['unknown', 'not available', 'n/a', 'na', 'tbd', 'tba', '---'] -> `np.nan`

**Step 2. Handle Placeholder Zeros**  
- **Strategy**: The values `0` in `Rank` and `Popularity` don't represent a true zero value but rather a missing or unassigned one. These should be converted to `np.nan`.

**Step 3. Standardize Formating in (Aired, Duration)**  
- **Strategy**:
   - Handling inconsistnt Aired format like `'2005'`, `'2010 to ?'`, `'Oct 20, 1999 to ?'`
   - Extracting `Aired Month`, `Aired Year`, `Aired Date Start`, `Aired Date End` from `Aired` column
   - Convert string Duration (`24 min`) into single numeric value (`24.0`) 

**Step 4: Handle multi-lable columns (Genres, Studios, Producers)**
- **Strategy**: 
   - Split string value into proper list: `'MAPPA, White Fox'` into `["MAPPA", "White Fox"]`
   - Fixing Typo and Inconsistency using mapping: `"Sunrise Inc."` -> `"Sunrise"`

**Step 5: Data Type Coercion & Logic Validation**
- **Type conversion**: Strings like `"8.75"` → float `8.75`
- **Business rule fixes**: "Movie must have 1 episode" is domain knowledge, not learned from data
- **Ghost record removal**: Records with no score AND no metadata are fundamentally unusable

**Step 6: Drop Unnecessary Columns**

| **Feature Dropped** | **Reason for Dropping** |
|---------------------|--------------------------|
| **`Licensors`** | Missing over 80% of values → unreliable for analysis/modeling |
| **`Premiered`** | 77% missing + redundant (information extracted from `Aired` into `air_year`, `air_month`) |
| **`English name`** | Redundant (primary `Name` column sufficient for identification) |
| **`Other name`** | Redundant (primary `Name` column sufficient for identification) |
| **`Image URL`** | Non-feature data (image links cannot be used in current analytical scope) |
| **`Synopsis`** | Requires NLP techniques beyond project scope; would distract from core analysis |
    
---

### **2.2.  Splitting X, y and Train, Test set**

### **A. Spliting Target Variable - `Score`**

```bash
X = df1.drop('Score', axis=1)
y = df1['Score']
```

### **B. Spliting Train and Test set (80/20)`**
```bash

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

```
The shape after splitting is:
   - X_train shape: (12553, 11), y_train ((12553, 1))
   - X_test shape: (3139, 11), y_test (3139, 1)  

---

### **2.3.  Post-Split Pipeline (Stateful Transformations)**

### **A. Goal**  
Produce final, fully processed Train/Test sets and store the fitted pipeline inside `models/` for use in  **PHASE 4 — Modeling Comparison**.

---

### **B. Critical Principal**: 
- These operations learn statistical parameters from training data only, preventing data leakage and support reproducing for future uses.
- Since our main goal is to find out which feature contributing to a successful Anime Released, post-released features like `Rank`, `Members`, `Popularity`,`Favorites` and `Scored by` will be removed to **prevent casual data leakage** when predicting `Score` of an Anime.

--- 

### **C. Custom Transformers (Using `BaseEstimator` and `TransformerMixin`)**

--- 

   **C.1. Class MultiListModeImputer**: 
   - **Purpose**: Imputing multi-label columns (Genres, Studios, Producers)
   - **Strategy**: 
      - Aggregate all items and find the mode (most frequent label) based on **Train set**
      - Any missing / empty list in Train and Test set is replaced with [most_frequent_label]

---

   **C.2. Class FrequencyGrouper**: 
   - **Purpose**:  
      - Reduce high-cardinality categories before appling One-Hot-Encoder on (Genres, Studios, Producers)
      - Result: From **1,287 features** after OHE -> **231 features**
   - **Strategy**: 
      - Compute frequency of each label in Train split only
      - Keep labels with frequency ≥ `min_freq[col]`
      - Replace all rare labels with "Other"

---

   **C.3. Class MultiLabelBinarizerDF** (Multi-Hot Encoding): 

   - **Purpose**:  
      - Transform list-like columns (Genres, Studios, Producers) into multi-hot encoded columns 

   - **Strategy**: 
      - Fit MultiLabelBinarizer per columns in Train
      - Transform/ Generate feature names: `ColumnName__Label` (example: `Genre_Action`)
      - Return concatenated DataFrame

--- 

   **C.4. Class CyclicalMonthEncoder**: 

   - **Purpose**: Convert months to sine/cosine features  
      - `Aired Month` are cyclical; month 12 is close to month 1, but ordinal encoding does not reflect this
      - Help model learn seasonality/ monthly patterns better

   - **Strategy**: 
      - Convert month numerics into cyclical format: **sin(2π * month / 12)** and **cos(2π * month / 12)**
      
--- 

   **C.5. Class FeatureEngineering**: 
   - **Purpose**:  
      - Add domain–relevant features that models cannot automatically create.

   - **Strategy**: 
      - Interaction terms:  `Episodes_x_Duration Minutes` help capturing combined effects on Score
      - Quantile-based categorization using `pd.cut()`: Created `DurationCat` and `EpisodesCat` features to capture non-linear relationships specific to anime formats and type (Movie is has only 1 episode and usually very long) 

      
--- 

### **D. Sklearn Library: Functions, Classes, and Rationale**
--- 

   **D.1.  Power Transformation - learns lambda parameter from Train only**: 
   - **Purpose**:  
      - Normalize highly skewed numeric columns
      - Suitable for Lineae Model

   - **Strategy**: 
      - Using Yeo-Johnson instead of Box-cox to handles zero (Counting_feature has 0 values)
      
--- 

   **D.2. SimpleImputer (median, mode) - learns values from Train only**: 
   - **Strategy**:  
      - Median → for numeric columns
      - Most Frequent (mode) → for categorical columns

   - **Reasons**: 
      - Robust to outliers, best choice when distributions are skewed

--- 

   **D.3. Scaling (RobustScaler) - learns quantiles from Train only**: 
   - **Strategy**:  
      - Uses median and IQR, not mean & std. 

   - **Reasons**: 
      - Dataset contains extreme outliers (e.g., 1,000+ episode counts for special cases) 
      - Resistant to heavy-tailed distributions

--- 

   **D.4. Encoding (OneHot, MultiHot) - learns categories from Train only**: 
   - **Strategy**:  
      - handle_unknown="ignore" prevents crash on unseen categories
      - Learns category vocabulary from train only

   - **Reasons**: 
      - **One-Hot Encoding**: Handle categorical features like Rating, DurationCat and EpisodesCat.
      - **Multi-Hot Encoding**: sklearn’s OHE cannot handle list-of-labels like Genre, Producers and Studios
       
--- 

   **D.5. ColumnTransformer**: 
   - **Strategy**:  
      - There are 4 sub-pipeline used for 4 groups of features 
      - 4 groups of features: Numeric, Ordinal Category, Multi-Lable Category, Cyclical features

   - **Reasons**: 
      - Apply different transformations to different feature groups.

--- 

### **E. Building Pipeline**
The `prepocessing_pipeline.pkl` has 2 sub-pipeline: `Feature Engineering Pipeline` and `Preprocessor Pipeline` as follows

```bash
Full Pipeline  
│                   
└── Sub_Pipe_1 - Feature Engineering 
│     ├──  Create_interactions
│     ├──  Create_list_counts
│     ├──  Discretization_Duration
│     └──  Discretization_Episode
│
│
└── Sub_Pipe_2 - Preprocessor       # Using ColumnTransformer
   │
   ├── Numerical Pipeline           # ['Episodes','Duration Minutes','Aired Year',
   │   │                            # 'Episodes_x_Duration Minutes','Genres_Count','Producers_Count','Studios_Count']
   │   ├── Median Imputer
   │   ├── PowerTransformer
   │   └── RobustScaler
   │
   ├── Categorical Pipeline        # ['Type','Status','Source','Rating','EpisodesCat','DurationCat'] 
   │   ├── Mode Imputer
   │   ├── Frequency Grouper
   │   └── OneHotEncoder
   │
   ├── Multi-label Pipeline         # ['Genre','Producers','Studios']
   │   ├── MultiListModeImputer
   │   ├── Frequency Grouper
   │   └── MultiHotEncoder
   │
   └──  Date Pipeline                # ['Aired Month']
       └── CyclicalMonthEncoder

```


--- 

### **📈 PHASE 3 — Comparative Analysis ("Before vs After")**

### **1. Overview**

**Notebook:** `03_Comparative_Analysis.ipynb`  

**Goal**: Visualize how clean data changes the narrative and support the keys to a successful anime

**Workflow**: This phase contains **3 main Acts**

--- 

#### **ACT 1 — THE CONTEXT**
   - **Role**: Producer seeking the **success formula** for the **next Anime project**
   - **Goal**: Understand why the raw dataset cannot support reliable decisions  
   - **The Conflict**:  **Raw data** is chaotic — missingness, fragmentation, inconsistent formats — **creating “illusions”** that distort analysis.

---

#### **2. ACT 2 - THE REVELATION (The True Insight)**

**Each Theme will have 4 main steps:**

   1. Issues Overview
   2. Solutions
   3. Visual Evidence (Raw vs Cleaned)
   4. Business Insights

**The 3 main Theme Features:** 
 
   1. The Foundation: Target Variable (Score)
   2. Theme A: Market Factors (Type, Source)
   3. Theme B: Creative Factors (Genres, Producers, Studios)  
   4. Theme C: Release Strategy (Aired, Episodes, Duration)

---

#### **3. ACT 3: THE RESOLUTION**
   - Proof: Model performance comparison 
   - Strategic Recommendation for Producer
   - Takeaway: "Success is engineered through data-informed decisions"

---

### **2. Key Findings**

---

### **Act 1: Context - Obstacles to Finding a Successful Anime Formula**

--- 
### **A. Key Conflicts: Target Variable Analysis (Score)**

**A.1. Critical Information Blind Spots**

Large portions of the dataset *pretend to exist* but contain no usable information: instead of NaN or meaningful values, row are filled with **"Unknown"**, **"No description available"**, **"not available"**, or broken image links. 

---

**A.2. Structural Entropy**

The dataset suffers from severe structural inconsistency, making it impossible to analyze without correction.

- **Inconsistent Formats**  
  - 20+ date formats:  "Oct 20, 1999 to ?"*, *"1-Sep-01"*
  - Durations recorded as:  "3 min"*, *"3 min per ep"*, *"1 hr. 50 min"
  - Numeric fields stored as strings (Score, Rank, Favorites, Episodes)

- **Multi-label Fields**  
  Genres, Studios, Producers stored as lists of strings (e.g., 'Action,Sci-Fi'), making them unusable for modeling or aggregation.

- **Misclassified Metadata**  
  - Movies with **>1 episode**  
  - Adult genres paired with *All Ages* ratings  

---

**A.3. Signal Distortion**

Even when data exists, it is **statistically misleading**.

- **Right-skewed engagement metrics** (Members, Favorites) with extreme 99th percentile outliers  
- **Ghost titles** with zero members and favorites distort rank-based insights  
- **Duplicate names** and inconsistent aliases inflate category counts  
- **Structural anomalies** (end date < start date, impossible runtimes) introduce noise into time-based analysis

---

### **B. Conclusion - Raw data creates illusions**
- Raw data gives the *illusion* of completeness, but essential information is fundamentally absent.
- Structural entropy blurs category boundaries and corrupts every downstream analysis.
- Signal distortions create false patterns, hiding the true behavior of the anime market.

---

### **Act 2: THE REVELATION (The True Insight)**

--- 

### **A. The Foundation: Target Variable Analysis (Score)**
   - **Issue Overview**: 37% missing, text-based values, distorted distribution 

   - **Solution**: Standardize and remove missing values, convert to numeric

   - **Visual Evidence**:
      - Raw: dominated by `"UNKNOWN"`  
      - Clean: smooth bell-shaped distribution centered at **6.39**  

   - **Business Insight**: 
      - *High scores (>9.0) and low scores (<3.5) are rare; Score is statistically healthy after cleaning*

--- 

### **B. Theme A: Market Factors (Type, Source)**
   - **Issue Overview**: Type misclassification (Movie with >1 episode), Source fragmentation (16 micro-categories), Unknown value

   - **Solution**: Reclassification logic, macro-categorization (5 groups)

   - **Visual Evidence**:
      - Raw: Misleading "OVA" dominance due to misclassified Movies
      - Clean: True distribution: OVA (6,062) > TV (5,511) > Special (3,673)

   - **Business Insight**: 
      - *TV series and Monvies have highest average Score (7.1)*
      - *Producers should prioritize source from **Manga or Literary properties** for maximizing Score*

---

### **C. Theme B: Creative & Production Factors (Genres, Producers, Studios)**
   - **Issue Overview**: Multi-label fragmentation, high cardinality, inconsistent naming, Unknow value

   - **Solution**: Frequency grouping, name normalization

   - **Visual Evidence**:
      - Raw: "Sunrise Inc.", "Sunrise", "Sunrise Studios" treated as separate
      - Clean: Consolidated to single entity, revealing true market share

   - **Business Insight**: 
      - *Which Genres do top Studios consistently excel in, helping Producer decide on hiring Studio decision (example: White Fox Studio did best on Romance and Mystery)*

---

### **D. Theme C: Release Strategy (Aired, Episodes, Duration)**
   - **Issue Overview**: Numeric, Datetime feature treated as text, fragmentation, high cardinality, inconsistent format, Unknow value

   - **Solution**: Convert to numeric, datetime type; Normalize format, Grouping into meaningful Episodes, Duration ranges and seasons

   - **Visual Evidence**:
      - Raw: Random monthly distribution, inconsistent format "3 min", "3 min per ep"
      - Clean: ordered monthly distribution, meaningful groups of episodes and duration ranges

   - **Business Insight**: 
      -  *12-13 episode format with over 60 minute runtime maximizes both Score and engagement*
      -  *Apr, Jul, Oct are the hot-month for releasing new anime*

---

### **ACT 3 — THE RESOLUTION: Deep Insights & Strategic Decisions**

---

### **A. Proof — What Clean Data Reveals (Hidden Patterns Unlocked)**

From the “Before vs After” analysis, four cross-theme patterns emerge that were completely invisible in raw data:

- **Format Hierarchy**  
  TV Series & Movies consistently receive the highest scores, while OVAs/Specials hit a natural score ceiling regardless of quality.

- **Source Material Advantage**  
  Adaptations from **Manga** and **Novels** outperform **Original** concepts and **Game**-based works, confirming the value of pre-validated stories.

- **Studio–Genre Fit**  
  High performance comes from specialization.  
  *Studios excel only in specific genres* (e.g., MAPPA → Suspense, Kyoto Animation → Drama/Romance).

- **Scale Correlation**  
  Larger production committees (6+ producers) and longer runtimes (>60 min) strongly correlate with higher scores.

---

### **B. Strategic Recommendations for the Producer**

Based on the unlocked insights, a producer can now follow a **data-driven blueprint** for maximizing success probability:

- **1. Low-Risk Production Strategy**  
  Choose **TV Series** or **Feature Films** adapted from strong **Manga/Novel IPs** and secure a large committee (6+ members) to stabilize funding and production quality.

- **2. Genre & Studio Alignment**  
  Avoid overcrowded genres (Action/Comedy).  
  Invest in high-yield genres like **Mystery** and **Suspense**, and pair them with *specialized* studios (e.g., White Fox for Thriller/Mystery).

- **3. Premium Format Design**  
  Develop **Mini-Series (6–12 episodes)** with **Movie-Length duration (60–180 mins)** — the top-performing configuration (Avg Score: **8.21**).

- **4. Release Timing Optimization**  
  Schedule major releases for **Fall (October)** or **Winter (January)**.  
  Avoid **Summer**, which historically correlates with lower average scores.

---

### **C. Takeaway — The Resolution of the Story**

The cleaned dataset reveals a **highly structured and cyclical anime industry**, where release timing, studio specialization, format choice, and production scale define performance. Comparative Analysis confirms that:  
**Only after cleaning can data reliably guide business decisions.**

--- 

### **⚖️ PHASE 4 — Modeling Comparison ("The Validator")**

### **1. Overview**
**Notebook:** `04_Modeling_Comparison.ipynb`  

**Goal**: Quantify the impact of data preparation via Machine Learning performance

**Methodology**:
1. **Baseline Model**: Linear Regression on minimally processed raw data
2. **Final Model**: Same algorithm on fully prepared data
3. **Comparison**: Metrics (R², MAE) and feature importance analysis

---

### **2. Baseline Data Handling**

To keep the baseline model intentionally simple (and highlight the value of proper data preparation), the raw dataset was only minimally processed:

- **Missing Values**: All rows containing any `NaN` were dropped instead of imputed, reducing the dataset from **15,692 → 7,231** rows.
- **Categorical Features**: Two lightweight approaches were tested:  
   1. **Dropping all categorical columns entirely**, ensuring Linear Model can run without error
   2. **Ordinal Encoding** for converting categories into numeric codes (Our final method for baseline model) 

These constraints create a “worst reasonable scenario,” ensuring the Baseline Model reflects the performance of raw data without meaningful cleaning.

---

### **3. Metrics Results**:
| Metric | Baseline (Raw Data) | Final (Prepared Data) | Improvement |
|--------|-------------------|---------------------|-------------|
| **R² Score** | 0.09 | 0.53 | **+488%** |
| **MAE** | 0.64 | 0.48 | **-25%** |

---

### **4. Feature Importance Shift**:
- **Baseline**: Weak signals from Status, Rating, Source
- **Final**: Strong signals from Producers, Studios, Genres (properly encoded)
- **Insight**: Preparation unlocks the true predictive power of categorical features

---

## ⚙️ 6. How to Run the Project

### **Step 1 — Clone Repository**
```bash
git clone https://github.com/<your-username>/anime-data-storytelling.git
cd anime-data-storytelling
```

### **Step 2 — Install Dependencies**

Install required Python packages:
```bash
pip install -r requirements.txt
``` 

Note: If you prefer using a virtual environment:
```bash
# Create virtual environment
python -m venv venv

# Activate on Windows:
venv\Scripts\activate

# Activate on macOS/Linux:
source venv/bin/activate

# Then install dependencies
pip install -r requirements.txt
```

### **Step 3 — Run Analysis Pipeline**

Execute notebooks in sequential order:
1. Explore raw data problems: `jupyter notebook notebooks/01_Diagnostic_EDA.ipynb`
2. Run data preparation: `jupyter notebook notebooks/02_Data_Preprocessing.ipynb`
3. Compare visual narratives (Before and After Data Preparation): `jupyter notebook notebooks/03_Comparative_Analysis.ipynb`
4. Validate with modeling: `jupyter notebook notebooks/04_Modeling_Comparison.ipynb`

### **Step 4 — Generate All Visualizations**

All charts are automatically saved to the `plots/` directory when running notebooks 03 and 04.

### **Step 5 — Reading the Final Report**
After running all notebooks, the final synthesized report is available as a PDF in the `report/Final_Report_Group1.pdf` directory

---
## 📈 7. Key Findings & Conclusions

### **7.1. Data Preparation Impact**
1. **Visual Clarity**: Cleaned data reveals true patterns obscured by noise
2. **Business Insights**: Actionable recommendations emerge only after preparation
3. **Model Performance**: R² improved from **0.09 to 0.53** (443% increase)
4. **Feature Understanding**: Proper encoding reveals true drivers (Producers, Studios)

### **7.2. Storytelling Principles Applied**
- **Contrast**: Clear before/after comparisons
- **Focus**: Highlight most impactful transformations
- **Narrative Flow**: Problem → Solution → Visual Evidence → Business Recommendation
- **Audience Alignment**: Technical proof + business relevance

### **7.3. Strategic Recommendations for Anime Industry**

Based on insights revealed after full data cleaning and comparative analysis:

1. **Production Strategy**  
   Prioritize **TV Series or Feature Films** adapted from strong **Manga/Novel IPs**, supported by larger production committees (6+ members) to ensure quality stability.

2. **Release Timing Optimization**  
   Schedule key launches in **January, April, July, or October**, with strongest performance observed in **Fall (October)** and **Winter (January)**.

3. **Creative & Studio Alignment**  
   Move beyond saturated genres; invest in high-yield genres such as **Mystery** and **Suspense**, pairing them with specialized studios (e.g., White Fox, MAPPA, Kyoto Animation).

4. **Premium Format Opportunity**  
   Consider **Mini-Series (6–12 episodes)** with **Movie-length runtime (60–180 minutes)** — the highest-performing configuration in the dataset.

5. **Quality Signals**  
   Treat top studios, reputable producers, and longer runtimes as strong predictors of higher scores, using them as data-backed quality proxies.


---

## 📄 8. License & References

**License**: MIT  
**Dataset Source**: [Kaggle - Anime Dataset 2023](https://www.kaggle.com/datasets/dbdmobile/myanimelist-dataset)

**Key References**:
- Knaflic, C. N. (2015). *Storytelling with Data*
- McKinney, W. (2017). *Python for Data Analysis*
- Scikit-learn documentation for pipeline design

---

**Project Status**: ✅ Complete  
**Last Updated**: December 2024

*This project demonstrates that in data science, the quality of your preparation determines the quality of your insights.*