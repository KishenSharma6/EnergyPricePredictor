import string
import pandas as pd
import numpy as np
import re

def clean_columns(dataframe, cols = None):
    """Takes pd.Dataframe containing raw data and performs the following opterations:
        - Drops cols specified by cols 
        - Drops columns containing only null or non-unique values
    
    Functions returns cleaned energy dataframe
    Args:
        dataframe (pd.Dataframe): pandas dataframe containing raw energy data
        cols (list:strings): OPTIONAL. List of strings containing names of columns 
        you would like to be dropped
    """
    #Check data types of arguments. Drop cols if cols != None
    assert type(dataframe) == pd.DataFrame, "Error, dataframe is not pd.Dataframe"
    
    if cols == None:
        pass
    else:
        assert all(type(c) == str for c in cols), "Error, cols can only contain strings"
        dataframe= dataframe.drop(columns= cols, axis= 1)
    
    #Drop cols containing null
    dataframe= dataframe.dropna(how= "all", axis= 1)

    #Drop cols containing single unique value
    to_drop= []
    for c in list(dataframe.columns):
        if dataframe[c].nunique() == 1:
            to_drop.append(c)
    dataframe= dataframe.drop(columns = to_drop, axis= 1)

    return dataframe


def set_time_index(dataframe, time_column):
    """Clean column containing time data you would like to set as an index

    Args:
        dataframe (pandas): pandas dataframe to apply transformation
        time_column (string): name of column containing time data you would like cleaned and 
        set as index

    Returns:
        _type_: _description_
    """
    #Clean time col and set as index
    dataframe[time_column]= pd.to_datetime(dataframe[time_column].apply(lambda x: re.sub("[+].*", '', x )))
    dataframe.set_index(time_column, inplace= True)
    return dataframe

def kelvin_to_fahrenheit(dataframe, temp_cols):
    """Convert cols containing kelvin temp to freedom units

    Args:
        dataframe (pd.Dataframe): pandas dataframe containing data you would like cleaned
        temp_col (string|list of strings): string (or list of strings) containing names of 
        column(s) you would like transformation applied to
    """
    for c in temp_cols:
        dataframe[c]= dataframe[c].apply(lambda x: (1.8* (x- 273)) + 32)
    
    return dataframe

def input_mean(dataframe):
    """Input column mean values for rows containing missing data

    Args:
        dataframe (_type_): _description_
    """
    dataframe= dataframe.fillna(dataframe.mean())
    return dataframe

def input_median(dataframe):
    """Input column median values for rows containing missing data

    Args:
        dataframe (_type_): _description_
    """
    dataframe= dataframe.fillna(dataframe.mean())
    return dataframe