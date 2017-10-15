import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import ast

from astropy.table import Table
from astropy.io import ascii
from astropy.io import fits
from astropy.coordinates import SkyCoord
from astropy import units

path =   '/cos_pc19a_npr/data/SDSS/DR14Q/'
filename = 'DR14Q_pruned_repeats.csv'
#filename = 'DR14Q_pruned_repeats_top20.csv'
datafile= path+filename

df = pd.read_csv(datafile)
df.columns
print(type(df))

multiples = df[df["N_SPEC"] >2].copy()

multiples.plot.scatter(x='MJD', y='N_SPEC')
plt.show()

ser = multiples['MJD_DUPLICATE'].apply(ast.literal_eval).str[1]
multiples['MJD_DUPLICATE'] = pd.to_numeric(ser, errors='coerce')
multiples['MJD_DUPLICATE_NEW'] = pd.to_numeric(ser, errors='coerce')

print(multiples['MJD_DUPLICATE_NEW'].head(10))

multiples.plot.scatter(x='MJD', y='MJD_DUPLICATE')
plt.ylim((56200,57000))
plt.show()
