# data-analysis-TASK1-DEPI
A beginner-friendly data preprocessing project using Python and Pandas. This repo demonstrates different techniques for handling missing values, including:  Filling with mean, median, or mode  Dropping missing values when necessary

# Data Cleaning Utilities

This project provides helper functions to handle missing values in datasets using **Pandas**.  
It includes methods for filling missing values with the **mean**, **median**, or **mode**, as well as dropping missing data when needed.

## Features
- Fill missing values with:
  - Mean
  - Median
  - Mode
- Drop missing rows or columns
- Easy to apply on multiple columns

## Example Usage
```python
import pandas as pd
from data_cleaning import fill_missing_with_mean, fill_missing_with_median, fill_missing_with_mode, drop_missing

# Sample DataFrame
df = pd.DataFrame({
    "age": [20, None, 25, 30, None],
    "salary": [5000, 6000, None, 7000, 8000]
})

# Fill missing values with median
df = fill_missing_with_median(df, ["age", "salary"])

# Drop missing rows
df = drop_missing(df, axis=0)
