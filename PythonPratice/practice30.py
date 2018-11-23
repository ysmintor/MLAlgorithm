#!/usr/bin/python3
import pandas as pd
import numpy as np

string_data = pd.Series(['aardvark', 'artichoke', np.nan, 'avocado'])

print(string_data)

string_data[0] = None
string_data.isnull()