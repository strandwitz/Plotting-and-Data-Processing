# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 20:16:27 2020

@author: Nick Strandwitz
"""

###  Plots LEIS data (ion energy vs intensity/counts)
###  Created 3/2/2020 by Strandwitz; Last modified 3/3/2020 by Strandwitz
###
###  Note that you should output your spectrum without any regions defined.  Otherwise you'll need to pick which columns get plotted

# TO DO:
#        Insert colorbar as a legend with ion doses labeled at a few points

### Some general adjustable settins

lnwdth=4      # line width in plot
#collabels=['scan', 'depth (nm)', 'dose', 'MoTe', 'Al/Si', 'O'] # Column labels, manually input headers here, must match dimensions
mrksz=15      # size of markers

### Brings up dialog box to select one or more files
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()
root.call('wm','attributes','.', '-topmost', True)    
filepath=filedialog.askopenfilenames(initialdir = r"C:\Users\Nick Strandwitz\Documents\NCS docs\Data\LU\19.12.18-19 LEIS Training TiMoN ScN MoOx\101419-3-1", title = "select file",filetypes = (("all files","*.*"),("all files","*.*")))
# %gui tk


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import ListedColormap, LinearSegmentedColormap
from matplotlib import cm
from matplotlib.ticker import FormatStrFormatter
import matplotlib.pylab as pl
import shutil     # to copy script into data directory later


# %matplotlib inline

# Read in data, tab delimited, skip first row
df = pd.read_csv(filepath[0],  
                 sep='\t',
                  skiprows=1,
                  header=None
               )

#df.columns = collabels  # Put  column labels in if you want to

#print(df.shape)  # uncomment if you want to know shape of dataframe
#print(df)        # uncomment if you want it to print the dataframe like a table

ax1 = plt.gca()   # Set up instance of axes

numspectra=int((df.shape[1]-3)/2)           # figures out how many spectra are in the file
numspectra=3                                # uncomment and set equal to number of scans you want OR
                                            # comment and it will plot all the spectra in the file

colors = cm.cool(np.linspace(0,1,numspectra)) # sets up gradient from 0 to 1 in chosed colormap based on number of spectra

df[0]=df[0].str.replace(',','')             # Silly ass LEIS software puts commas in the data... get em outta here
df[0]=df[0].astype(float)                   # Also, its a string... turn the df into a float

for x in range(numspectra):                 # loops for number of spectra
    df.plot.line(x=df.columns[0], y=df.columns[2*x+3], color=tuple(colors[x]), fontsize=20, ax=ax1, figsize=(9,9), lw=lnwdth)
    print(2*x+1)   
    
# df.plot.line above plots x data, ydata (every other column), sets the color of the line etc
    
# Format stuff
ax1.set_xlabel("Energy (eV)", fontsize=30, fontname="Arial")   # sets x label, size, font
ax1.set_ylabel("Counts", fontsize=30, fontname="Arial")        # sets y label, size, font
ax1.legend(loc=2, prop={'size': 22})        # where to put legend and size
ax1.set_ylim(bottom=0)                      # sets lower limit for y axis to zero

plt.setp(ax1.spines.values(), linewidth=3)  # sets the thickness of the plot box
ax1.tick_params(width=3)                    # width of the ticks
ax1.tick_params(length=8)                   # length of the tics
ax1.tick_params(direction='in')             # in out or inout

for tick in ax1.get_xticklabels():          # sets x tick font label
    tick.set_fontname("Arial")
for tick in ax1.get_yticklabels():          # sets y tick font label 
    tick.set_fontname("Arial")


ax1.xaxis.set_major_formatter(FormatStrFormatter('%.0f'))    # tells legend lables number of sig figs
ax1.get_legend().remove()               # removes the legend, comment to keep it in
plt.tight_layout()                      # This seems to help keep edges, such as axes labels, from getting cut off



# Save pdf and png in the directory of the source data
splitpath=filepath[0].split('/')        # splits filepath everywhere there is a '/'
pathh=filepath[0].replace(splitpath[len(splitpath)-1],'')   # takes the last element of filepath out (filename)
fname=splitpath[len(splitpath)-1]
plt.savefig(pathh + fname + 'spctr.pdf')      # combines path with filename for image file
plt.savefig(pathh + fname + 'spctr.png')      # combines path with filename for image file
shutil.copy(__file__, pathh + fname + '.py')  # saves a copy of this script with the datafile (or first datfile) name .py for later manipulation


plt.show()



