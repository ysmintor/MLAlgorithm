#!/usr/bin/python3
import pandas as pd
from numpy import nan as NA

data = pd.Series([1, NA, 3.5, NA, 7])
print(data.dropna())