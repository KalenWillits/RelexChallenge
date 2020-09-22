# RelaxChallenge library.py
import numpy as np
import matplotlib.pyplot as pyplot
import seaborn as sns
import pandas as pd
from tqdm import tqdm

def define_date_id(df):
    """
    creates the date_id and num_day columns the user_eng dataf
    """
    df['date_id'] = df['year'].apply(str) + df['month'].apply(str) + df['week'].apply(str) + df['day_of_week'].apply(str)

    df['num_day'] = np.NaN
    ids = df['date_id'].unique()
    for id, num_day in zip(ids, range(len(ids))):
        df['num_day'][df['date_id'] == id] = num_day
    return df

def define_adopted_users(df):
    """
    Defining an "adopted user" as a user who has logged into the product
    on three separate days in at least one seven­day period.
    """

    df['adopted'] = 0
    df['adopted'][df['user_activity'] >= 3] = 1
    return df

def user_activity(df, scope=3, limit=None):
    """
    Funciton for the user_eng dataframe.
    returns user activity as a columns over a given scope.
    ***This function is a resource hog, use the limit argument when testing.***
    """
    if limit == None:
        pass
    else:
        df = df.head(limit)
    df['user_activity'] = np.NaN
    for id in tqdm(df['user_id']):
        for day in df['num_day']:
            day_plus = df['num_day'] <= day+scope
            day_minus = df['num_day'] >= day-scope
            user_id = df['user_id'] == id
            user_activity = sum((day_plus) & (day_minus) & (user_id))
            df['user_activity'][user_id] = user_activity

    return df
