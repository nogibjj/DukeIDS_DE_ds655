#  IDS 706 Week 2 assignment - Creating a function to show descriptive statistics for a dataframe
# import pandas as pd
import os
import datetime


def PandasDesc(df):
    """Code to return a summary of a dataframe and save it to a file"""
    if os.path.isfile("./Resources/Summary.md"):
        os.remove("./Resources/Summary.md")
    f = open("./Resources/Summary.md", "w", encoding="utf-8")
    f.flush()
    f.write(str(df.describe()))
    f.write("\n")
    f.write(str(datetime.datetime.now()))
    f.write("\n")
    f.write(f"""![Graph]({"PlotImage.png"})""")
    f.close()
    print("Summary of the dataframe has been saved to Summary.md")
    return df.describe()
