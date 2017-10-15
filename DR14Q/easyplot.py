import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import ast

filename = 'DR14Q_pruned_several3cols.csv'
datafile= path+filename

df = pd.read_csv(datafile)

df.plot.scatter(x='MJD', y='N_SPEC')
plt.show()

ser = df['MJD_DUPLICATE'].apply(ast.literal_eval).str[1]
df['MJD_DUPLICATE'] = pd.to_numeric(ser, errors='coerce')
df['MJD_DUPLICATE_NEW'] = pd.to_numeric(ser, errors='coerce')

df.plot.scatter(x='MJD', y='MJD_DUPLICATE')
plt.ylim((56200,57000))
plt.show()
