import os

# Full project structure definition
structure = {
    "data/raw": ["anime-dataset-2023.csv"], # Place your raw csv here
    "data/processed": ["prepared_data.csv"], # Place your processed csv here
    "models": [
        "processing_pipeline.pkl", # Place your saved pipeline here
        "model.pkl"                # Place your saved model here
    ],
    "notebooks": [
        "01_Diagnostic_EDA.ipynb",
        "02_Data_Preprocessing.ipynb",
        "03_Comparative_Analysis.ipynb",
        "04_Modeling_Comparison.ipynb"
    ],
    "report": ["Final_Report_GroupX.pdf"],
    "src": ["Custom_Transformer.py"], # Place your custom python script here
    ".": ["README.md", "requirements.txt", ".gitignore"]
}

def create_full_structure():
    print("Initializing Project Structure...")
    
    for folder, files in structure.items():
        # Create directories
        if folder != ".":
            os.makedirs(folder, exist_ok=True)
            # Create .gitkeep to track empty folders
            with open(os.path.join(folder, ".gitkeep"), "w") as f:
                pass
        
        # Create placeholder files
        for file in files:
            file_path = os.path.join(folder, file)
            if not os.path.exists(file_path):
                with open(file_path, "w") as f:
                    if file == ".gitignore":
                        f.write("# Data\ndata/\nmodels/*.pkl\n\n# System\n__pycache__/\n.ipynb_checkpoints/\n.DS_Store\n\n# Env\n.env\nvenv/")
                    elif file == "README.md":
                        f.write("# Project: The Power of Data Preparation\n\nSee structure details below.")
                    else:
                        pass # Empty file
                print(f"[CREATED] {file_path}")
            else:
                print(f"[EXISTS]  {file_path}")

    print("\nSuccess! Structure created. Please move your files to their respective folders.")

if __name__ == "__main__":
    create_full_structure()