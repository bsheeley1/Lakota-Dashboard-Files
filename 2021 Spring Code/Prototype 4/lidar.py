# -*- coding: utf-8 -*-
"""
Created on Wed Mar 31 14:39:12 2021

@author: bbshe
"""
import laspy
import numpy as np
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
import plotly.express as px

def myFunc(file):
    inFile = laspy.file.File(file, mode = "r")
    fig = plt.figure(figsize=[20, 5])
    ax = plt.axes(projection='3d')
    sc = ax.scatter(inFile.x, inFile.y, inFile.z, c=inFile.z ,s=0.1, marker='o', cmap="Spectral")
    plt.colorbar(sc)
    plt.savefig('Assets/Test.png')
    plt.show()
    return 
