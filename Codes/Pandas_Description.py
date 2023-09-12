#  IDS 706 Week 2 assignment - Creating a function to show descriptive statistics for a dataframe
#import pandas as pd

def PandasDesc(df):
  # Writing the summary statistics to a file Summary.md in output folder
  with open("./Resources/Summary.md", "w", encoding="utf-8") as f:
    f.write(str(df.describe()))
  return df.describe()
