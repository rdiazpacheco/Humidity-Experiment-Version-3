"""
Created on Mon Dec  6 10:15:50 2021

Humidity studies, Tapestar file exraction

Summary: 
    Takes a .dat file (extracted from the viewer) with the Ic values with respect to x values.
    These values are then binned to a desired size turning the continues measurement into samples. 
    The samples are then grpahed and an average value is given. 
    A graph of the samples is saved. 

@author: rdiazpacheco
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
import os
import pandas as pd

#File Directory

File_name = 'TS_Files\Frankenstein_export_001.dat';
os.chdir('TS_Files')
#pick file
TS_data_raw = np.genfromtxt('Frankenstein_export_001.dat',
                        skip_header = 2);

#Graph the Ic
xpoints = TS_data_raw[:,0];
Ic = TS_data_raw[:,1];


#Find where the IC is not 0
Ic_HTS = np.asarray(np.where(TS_data_raw[:,1] >50));
Ic_spacers = np.asarray(np.where(TS_data_raw[:,1] <10));


xdist2 = np.full_like(Ic_HTS,0);

for x in range(0,len(Ic_HTS[0])-1):
    xdist2[0,x] = Ic_HTS[0,(x+1)]-Ic_HTS[0,x];


non_0 = np.asarray(np.where(xdist2 > 5))
non0_xdist = xdist2[0,non_0[1,:]];

Ic_jumps = np.full_like(non0_xdist,0);
for x in range(0,len(non0_xdist)):
    Ic_jumps[x] = np.asarray(np.where(xdist2[0,:] == non0_xdist[x]));
    
Ic_HTS_jumps = np.arange(2*len(Ic_jumps))
for x in range(0,len(Ic_jumps)):
    Ic_HTS_jumps[2*x] = Ic_HTS[0,Ic_jumps[x]];
    Ic_HTS_jumps[2*x+1] = Ic_HTS[0,Ic_jumps[x]+1];
    
Ic_jumps2 = xpoints[Ic_HTS_jumps];


ypoints3 = np.full_like(TS_data_raw[:,0],0);
ypoints3[Ic_HTS_jumps] = 150;

plt.plot(xpoints, ypoints3, label = "HTS-connector interface")
plt.plot(xpoints, Ic)
plt.show()

"""
Ic_jumps2 = np.arange(2*len(Ic_jumps))
for x in range(1,len(Ic_jumps)):
    Ic_jumps2[2*x-1] = Ic_rel[0,Ic_jumps[x-1]];
    Ic_jumps2[2*x] = Ic_rel[0,Ic_jumps[x+1]];
"""


    

"""
#Set length of samples
sample_length = 50;
samples = np.linspace(min_value,max_value,50);
"""
