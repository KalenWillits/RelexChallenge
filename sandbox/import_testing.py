# sandbox/import_testing.py
user_eng.columns
users.columns
users.head()

user_eng.isnull().sum()

user_eng['week'] = pd.to_datetime(users_eng['time_stamp']).dt.week
user_eng['week'].unique()
