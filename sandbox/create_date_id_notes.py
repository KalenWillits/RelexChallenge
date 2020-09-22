# sandbox/create_date_id_notes.py

df = user_eng

df.columns



df['date_id'] = df['year'].apply(str) + df['month'].apply(str) + df['week'].apply(str) + df['day_of_week'].apply(str)

df['num_day'] = np.NaN
ids = df['date_id'].unique()
for id, num_day in zip(ids, range(len(ids))):
    df['num_day'][df['date_id'] == id] = num_day
num_day
id
sum(df['date_id'] == id)
list(zip(ids, range(len(ids))))

df['num_day'].sum()
df.num_day
