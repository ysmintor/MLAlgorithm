#!/usr/bin/python3
import pandas as pd
from numpy import nan as NA

data = pd.Series([1., -999., 2., -999., -1000., 3.])

print(data)

print(data.replace(-999, NA))
