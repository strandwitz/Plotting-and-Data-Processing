# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 20:19:50 2020

@author: Nick Strandwitz
"""

###  Plots LEIS profile from ascii file output of IONTof Qtac
###  Created 2/29/2020 by Strandwitz; Last modified 2/29/2020 by Strandwitz
###

### TO DO: create stable loop for overlaying multiple scans

### Some general adjustable settins
lnwdth=5      # line width in plot
collabels=['scan', 'depth (nm)', 'dose', 'MoTe', 'Al/Si', 'O'] # Column labels, manually input headers here, must match dimensions
mrksz=15      # size of markers

### Brings up dialog box to select one or more files
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()
root.call('wm','attributes','.', '-topmost', True)    
filepath=filedialog.askopenfilenames(initialdir = "C:/Users/Nick Strandwitz/Documents/NCS docs/Data/LU/19.12.18-19 LEIS Training TiMoN ScN MoOx/101419-3-1/profile/", title = "select file",filetypes = (("all files","*.*"),("all files","*.*")))
print(len(filepath))   # print number of files selected

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Read in data, tab delimited, skip first row
df33 = pd.read_csv(filepath[0],  
                 sep='\t',
                  skiprows=1,
                  header=None
               )

df33.columns = collabels  # Put those column labels in

ax1 = plt.gca()  # Set up instance of axes

# Potentially modify below to make a loop for each element/region

# Plot each line; TO DO add loop to go through these?
df33.plot(kind='line',x=df33.columns[2],y=df33.columns[3], color='red', marker='s', markersize=mrksz, markeredgewidth=2, markeredgecolor='black', fontsize=20, ax=ax1, figsize=(8,8), lw=lnwdth)
df33.plot(kind='line',x=df33.columns[2],y=df33.columns[4], color='blue', marker='o', markersize=mrksz, markeredgewidth=2, markeredgecolor='black', ax=ax1, lw=lnwdth)
df33.plot(kind='line',x=df33.columns[2],y=df33.columns[5], color='violet', marker='<', markersize=mrksz, markeredgewidth=2, markeredgecolor='black', ax=ax1, lw=lnwdth)

# Format stuff
ax1.set_xlabel("Dose (10$^{15}$ cm$^{-2}$)", fontsize=30, fontname="Arial")
ax1.set_ylabel("Counts", fontsize=30, fontname="Arial")
ax1.legend(loc=2, prop={'size': 22})
ax1.set_ylim(bottom=0)

plt.setp(ax1.spines.values(), linewidth=3)  # sets the thickness of the plot box
ax1.tick_params(width=3)         #width of the ticks
ax1.tick_params(length=8)        # length of the tics
ax1.tick_params(direction='in')  # in out or inout

for tick in ax1.get_xticklabels():
    tick.set_fontname("Arial")
for tick in ax1.get_yticklabels():
    tick.set_fontname("Arial")

plt.tight_layout()               # This seems to help keep edges, such as axes labels, from getting cut off


print(filepath[0])
# Figureing out how to split up filename to extract directory and deposit images and code there
splitpath=filepath[0].split('/')
pathh=filepath[0].replace(splitpath[len(splitpath)-1],'')
plt.savefig(pathh + 'profile.pdf')
plt.savefig(pathh + 'profile.png')

plt.show()


varpathh=splitpath[len(splitpath)-1]
varpathh=varpathh.replace('.txt','.ipynb')
print(varpathh)
