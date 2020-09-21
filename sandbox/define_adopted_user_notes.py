# sandbox/denfine_adpoted_user_notes.py

dataframe = user_eng.head(1000)
dataframe['adopted_user'] = False
for id in tqdm(dataframe['user_id'].unique()):
    for week in dataframe['week'].unique():

        query = dataframe[
                (dataframe['day_of_week'] == week)
                &
                (dataframe['user_id'] == id)]['day_of_week'].unique()
        # print(query)
        if len(query) >= 3:
            dataframe[dataframe['user_id'] == id]['adopted_user'] = True
        else:
            dataframe[dataframe['user_id'] == id]['adopted_user'] = False
query
dataframe.columns
dataframe['adopted_user'].sum()

query = dataframe[
        (dataframe['day_of_week'] == week)
        &
        (dataframe['user_id'] == id)]['day_of_week'].unique()

if len([1,2,3]) >= 3:
    dataframe[dataframe['user_id'] == id]['adopted_user'] = True
else:
    dataframe[dataframe['user_id'] == id]['adopted_user'] = False


    dataframe['adopted_user'].sum()


dataframe[dataframe['user_id'] == id]['day_of_week'].unique()

dataframe[
        (dataframe['day_of_week'] == week)
        &
        (dataframe['user_id'] == id)]['day_of_week'].unique()

dataframe[(dataframe['day_of_week'] == 1) & (dataframe['user_id'] == 66)]

len(dataframe['day_of_week'].unique())


user_df_adopted['adopted_user'].sum()





# Not working, changing tactic
dataframe = user_eng.head(1000)

dataframe['date_time'].year

day = 0
df['adopted_users'][(df['num_day'] < day+7) & (df['num_day'] > day-7)].sum()

user_adopted.columns
# This is the way to do it!!
storage = []
df = user_adopted.head(1000)
for id in tqdm(df['user_id']):
    for day in df['num_day']:
        sum((df['num_day'] < day+7) & (df['num_day'] > day-7) & (df['user_id'] == id))
