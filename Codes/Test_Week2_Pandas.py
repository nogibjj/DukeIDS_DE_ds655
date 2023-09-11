#  IDS 706 Week 2 assignment - testing our template using pandas 
import pandas as pd
from Pandas_Description import PandasDesc

Data_Link = "https://raw.githubusercontent.com/Opensourcefordatascience/Data-sets/master/Iris_Data.csv"

def test_Pandas():
    data = pd.read_csv(Data_Link)
    df = pd.DataFrame(data)
    print(PandasDesc(df))

test_Pandas()
