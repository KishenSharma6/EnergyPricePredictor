import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from IPython import display
import math

def heatmap(dataframe, figsize, annotate=True, linewidth= .2, cmap="coolwarm"):
    f, ax= plt.subplots(figsize= figsize)
    
    corrMatrix = dataframe.corr()
    sns.heatmap(corrMatrix, annot=annotate, linewidths= linewidth, cmap=cmap)
    plt.show()   

def corr_barh(dataframe, target, figsize):
    f, ax= plt.subplots(figsize= figsize)
    
    corrMatrix = dataframe.corr()
    corrMatrix[target][:-1].sort_values().plot(kind= "barh", ax=ax);
    plt.show()

def feature_distributions(dataframe, figsize= (20,40)):
    cols= 4
    rows= int(math.ceil(len(dataframe.columns)/cols))
    f, axs= plt.subplots(rows,cols, figsize = figsize)
    axs= axs.flatten()

    for i, col in enumerate(dataframe.columns):
        dataframe[col].plot.kde(ax= axs[i], color= "blue",)
        axs[i].set_title(col)

    plt.tight_layout()
