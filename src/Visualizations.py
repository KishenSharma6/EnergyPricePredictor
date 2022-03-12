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


def feature_distributions(dataframe, figsize= (20,40)):
    cols= 4
    rows= int(math.ceil(len(dataframe.columns)/cols))
    f, axs= plt.subplots(rows,cols, figsize = figsize)
    axs= axs.flatten()

    for i, col in enumerate(dataframe.columns):
        dataframe[col].plot.kde(ax= axs[i], color= "blue",)
        axs[i].set_title(col)

    plt.tight_layout()

def save_plot(path, name):
    """Save visualization as png at specified path

    Args:
        path (string): where you would like png to be saved
        name (string): file name of visualization
    """
    plt.savefig(path + name + '.png', bbox_inches='tight')
    print("Image successfully saved to path")

def load_plot(path, file_name, height= 500, width= 500):
    """Load image file_name from path

    Args:
        path (string): where you would like png to be load from
        name (string): file name of visualization you would like to load and display
        height (int): pixel length of display
        width (int): pixel width of display

    """
    display.Image(path + file_name, height=height, width=width)
