#  IDS 706 Week 2 assignment - Creating a function to show descriptive statistics for a dataframe
# import pandas as pd


def PandasDesc(df):
    """Code to return a summary of a dataframe and save it to a file"""
    with open("./Resources/Summary_1.md", "w", encoding="utf-8") as f:
        f.write(str(df.describe()))
    f.close()
    print("Summary of the dataframe has been saved to Summary_1.md")
    return df.describe()
