import pandas as pd
import numpy as np

df = pd.read_csv('diabetes_012_health_indicators_BRFSS2015.csv')
print(df.info())
print(df.describe())

print('Pearson coef:\n', np.corrcoef(df.sample(10000)))
input()