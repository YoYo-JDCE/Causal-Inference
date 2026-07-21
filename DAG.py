from typing import List
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import statsmodels.api as sm
from linearmodels.panel import PanelOLS

# Use raw.githubusercontent.com instead of github.com/.../blob/...
url = "https://raw.githubusercontent.com/scunning1975/mixtape/master/castle.dta"

# Read the Stata file cleanly without category conversion issues
df = pd.read_stata(url, convert_categoricals=False)

print(f"Loaded successfully: {df.shape[0]} rows, {df.shape[1]} columns")