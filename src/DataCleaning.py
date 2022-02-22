import string
import pandas as pd
import numpy as np

def clean_energy_data(dataframe, cols = None):
    """Takes pd.Dataframe containing raw energy data and performs the following opterations:
        - Drops columns containing only null values
        - Drops cols specified by cols
        - Standardizes time and sets as index
    
    Functions returns cleaned energy dataframe
    Args:
        dataframe (pd.Dataframe): pandas dataframe containing raw energy data
        cols (list:strings): OPTIONAL. List of strings containing names of columns 
        you would like to be dropped
    """
    #Check if arguments are correct datatypes
    assert type(dataframe) == pd.DataFrame, "Error, dataframe is not pd.Dataframe"
    if cols == None:
        pass
    else:
        assert all(type(c) == str for c in cols), "Error, cols can only contain strings"
    
    dataframe.dropna(how= "all", axis= 1, inplace= True)
    dataframe.drop(columns= [cols], axis= 1, inplace= True)

    