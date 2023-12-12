import pandas as pd
import random

# Randomizer
def SongRandomizer(df):
    """
    Randomly selects a song from the DataFrame.
    
    Parameters
    ----------
    df : pandas.DataFrame
        The DataFrame containing music data.
            
    Returns
    -------
    pandas.core.frame.DataFrame
        The record of the randomly selected song.
    """
    random_item = df.sample()
    return random_item

