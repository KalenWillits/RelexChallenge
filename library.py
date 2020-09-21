# RelaxChallenge library.py
import numpy as np
import matplotlib.pyplot as pyplot
import seaborn as sns
import pandas as pd
from tqdm import tqdm

def define_adopted_user(dataframe):
    """
    Defining an "adopted user" as a user who has logged into the product
    on three separate days in at least one seven­day period.
    """

    dataframe['adopted_user'] = False
    for id in tqdm(dataframe['user_id'].unique()):
        for week in dataframe['week'].unique():

            query = dataframe[
                    (dataframe['day_of_week'] == week)
                    &
                    (dataframe['user_id'] == id)]['day_of_week'].unique()
            if len(query) >= 3:
                dataframe[dataframe['user_id'] == id]['adopted_user'] = True
            else:
                dataframe[dataframe['user_id'] == id]['adopted_user'] = False
    return dataframe
