#  IDS 706 Week 2 assignment - testing our template using pandas 
import pandas as pd
from Pandas_Description import PandasDesc


data = {'product': ['A', 'B', 'C', 'C', 'D'],
        'price': [22000, 27000, 25000, 29000, 35000],
        'year': [2014, 2015, 2016, 2017, 2018]
        }

df = pd.DataFrame(data)
print(PandasDesc(df))
