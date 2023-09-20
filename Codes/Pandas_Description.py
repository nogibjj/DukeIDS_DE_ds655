#  IDS 706 Week 2 assignment - Creating a function to show descriptive statistics for a dataframe
# import pandas as pd
import os
import datetime
import tabulatehelper as th


def PandasDesc(df):
    """Code to return a summary of a dataframe and save it to a file"""
    if os.path.isfile("./Resources/Summary.md"):
        os.remove("./Resources/Summary.md")
    f = open("./Resources/Summary.md", "w", encoding="utf-8")
    f.flush()
    d = df.describe()
    h = d[:0]
    # print(h.columns)
    s = d.transpose()
    # s.set_index(h.columns, inplace=False)
    # print(str(d))
    # print(str(s))
    s["index"] = s.index
    column_to_move = s.pop("index")
    s.insert(0, "column name", column_to_move)
    f.write(th.md_table(s, formats={-1: "c"}))
    # print(th.md_table(s))
    f.write("\n\n\n")
    f.write("Generated at: " + str(datetime.datetime.now()))
    f.write("\n\n\n")
    f.write(f"""![Graph]({"PlotImage.png"})""")
    f.write("\n\n\n")
    f.close()
    print("Summary of the dataframe has been saved to Summary.md")
    return df.describe()
