# main.py - Main script to run the data analysis tasks

import pandas as pd
from file_handler import read_file , save_file
import preprossesing as pp

def main():
    # 1. reading the data
    df = read_file("train.csv")
    print(":) Data Loaded Successfully\n")

    # 2. show data types and unique values
    print("Column Types and Unique Values:\n")
    print(pp.chk_types(df))
    print("-" * 50)

    # 3. check missing values
    print("Missing Values:\n")
    print(pp.check_missing_values(df))
    print("-" * 50)

    # 4. fill missing values with median (for numerical columns)
    print(" Filling Missing Values (Median)...\n")
    df = pp.fill_missing_with_median(df, ["Age", "Fare"])
    print(pp.check_missing_values(df))
    print("-" * 50)

    # 5. fill missing values with mode (for categorical columns)
    df = pp.fill_missing_with_mode(df, ["Embarked"])
    print(" Filled Categorical Missing Values\n")
    print(pp.check_missing_values(df))
    print("-" * 50)

    # 6. drop rows with missing values 
    df = pp.drop_missing_rows(df, ["Cabin"])
    print("Dropped rows with missing 'Cabin'\n")
    print(pp.check_missing_values(df))
    print("-" * 50)

    # 7. حفظ الداتا بعد التنضيف
    save_file(df, "cleaned_train.csv")
    print("XD Cleaned data saved to 'cleaned_train.csv'")

if __name__ == "__main__":
    main()
