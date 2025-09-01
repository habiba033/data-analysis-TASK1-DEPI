# This file will handle reading and saving data (CSV, XLSX, JSON)
import pandas as pd
# ----------- Reading Functions -----------
path = 'venv/train.csv'
def read_file(path):
    """
    Read CSV, XLSX, or JSON file into a DataFrame.
    """
    if path.endswith(".csv"):
        return pd.read_csv(path)
    elif path.endswith(".xlsx"):
        return pd.read_excel(path)
    elif path.endswith(".json"):
        return pd.read_json(path)
    else:
        return "Unsupported file format. Use CSV, XLSX, or JSON."
    

#savee the file after finshing with right format
def save_file(df: pd.DataFrame, filepath: str):
    """Save DataFrame to CSV, XLSX, or JSON."""
    if filepath.endswith(".csv"):
        df.to_csv(filepath, index=False)
    elif filepath.endswith(".xlsx"):
        df.to_excel(filepath, index=False)
    elif filepath.endswith(".json"):
        df.to_json(filepath, orient="records", lines=False)
    else:
        return"Unsupported file format. Use CSV, XLSX, or JSON."
