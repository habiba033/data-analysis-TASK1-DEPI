# This file will handle data cleaning and preprocessing.

import pandas as pd
from file_handler import read_file

path = read_file('train.csv')
def chk_types(df):
    """
    this function checks the data types and number of unique values in each column of a DataFrame.
    It returns a DataFrame with the data types and number of unique values for each column.
    parm_1 : df
    return : DataFrame
    """
    dtypes = df.dtypes
    n_unique = df.nunique()
    return pd.DataFrame({"Dtype": dtypes, 'n_unique': n_unique})

# print(chk_types(path))

# same as above with different names.............
def check_data_types(df):
    """Print data types of all columns."""
    return pd.DataFrame({"Dtypes":df.dtypes , "n_unique":df.nunique()})
# print(check_data_types(path))


def convert_data_type(df, column, dtype: str):
    """Convert a column to a specific data type."""
    df[column] = df[column].astype(dtype)
    return df.dtypes

# print(convert_data_type(path, 'Age', 'float64'))


def check_missing_values(df):
    """Return number of missing values per column."""
    null = df.isnull().sum()
    ratio =round((null / df.shape[0]) * 100,2)
    return pd.DataFrame({"missing values": null, "ratio%": ratio}).T
# print(check_missing_values(path))


def fill_missing_with_median(df: pd.DataFrame, cols: list):
    """Fill missing values in given columns with median."""
    for col in cols:
        median = df[col].median()
        df[col] = df[col].fillna(median)
    return df
# print(fill_missing_with_median(path, ['Age']))


def fill_missing_with_mean(df: pd.DataFrame, cols: list):
    """Fill missing values in given columns with mean."""
    for col in cols:
        mean_val = df[col].mean()
        df[col] = df[col].fillna(mean_val)
    return df

def fill_missing_with_mode(df: pd.DataFrame, cols: list):
    """Fill missing values in given columns with mode."""
    for col in cols:
        mode_val = df[col].mode()[0]  # pick the first mode
        df[col] = df[col].fillna(mode_val)
    return df

def drop_missing_rows(df: pd.DataFrame, cols: list):
    """Drop rows where any of the given columns have missing values."""
    return df.dropna(subset=cols)
# print(drop_missing_rows(path, ['Cabin','Embarked']))
