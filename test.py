#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 09:40:22 2021

@author: huongphucquynhvo
"""

import numpy as np
import matplotlib.pyplot as plt
import os

#read data
inputdir = "dataEDAnew/"
outputdir = "EDA_signal_new/"
files = os.listdir(inputdir)
#get pdf signal
for file in files:
    data = np.genfromtxt(inputdir + file, delimiter=",", names=["x", "y"])
    
    #ploting
    f = plt.figure()
    plt.plot(data['x'], data['y'])
    
    
    #add title
    name = file[0:9]
    plt.title(name)
    plt.xlabel('Time(s)')
    plt.ylabel('EDA')
    
    #save plot in pdf
    
    
    f.savefig(outputdir + name + ".pdf", bbox_inches='tight')