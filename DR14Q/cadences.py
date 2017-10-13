
import numpy as np
import pandas as pd

import matplotlib.pyplot as plt

from astropy.table import Table
from astropy.io import ascii
from astropy.coordinates import SkyCoord
from astropy import units

## Path and file of some WISE W4 data
path =   '/cos_pc19a_npr/data/SDSS/DR14Q'
filename = 'DR14Q_pruned.fits'
datafile= path+filename

df = 
from astropy.table import Table
dat = Table.read('datafile', format='fits')
df = dat.to_pandas()

#data = fits.getdata(datafile, 1)
#type(data)
#data











## https://chrisalbon.com/python/set_the_color_of_a_matplotlib.html
color_map = plt.cm.Spectral_r
#color_map = plt.cm.RdYlGn
#color_map = plt.cm.Blues
#color_map = plt.cm.BrBG
#color_map = plt.cm.Greens
#color_map = plt.cm.YlOrRd
#color_map = plt.cm.spring
#color_map = plt.cm.summer
#color_map = plt.cm.autumn
#color_map = plt.cm.winter
#color_map = plt.cm.cool
#color_map = plt.cm.YlGn
#color_map = plt.cm.RdBu
#color_map = plt.cm.PuOr
#color_map = plt.cm.Oranges

fig = plt.figure(figsize=(18, 12))
fig.add_subplot(111, projection='aitoff')

## https://stackoverflow.com/questions/29368295/matplotlib-hexbin-normalize
gsize = 45 *2 * 2 * 2 
image = plt.hexbin(ra, dec, cmap=color_map, gridsize=gsize, mincnt=0, bins='log')
#image = plt.hexbin(ra, dec, cmap=color_map, gridsize=gsize, mincnt=1, bins='log')
print('\n gsize:: ', gsize, '\n')
