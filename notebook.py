# %% markdown
# # Relax Challenge Notebook
# ## Objectives:
# *"Defining an "adopted user" as a user who has logged into the product on three separate days in at least one seven­day period , identify which factors predict future user adoption."*

# %% markdown
# ### Table of Contents:
# - [Environment](#Environment)
# - [Data Import](#Data-Import)
# - [Building Week & Day Columns](Building-Week-&-Day-Columns)
# - [Defining An Adopted User](Defining-An-Adopted-User)
# - [Data Processing](#Data-Processing)
# - [Visualization](#Visualization)
# - [Observations](#Observations)
# - [Insights](#Insights)


# %% markdown
# ### Environment

# %% codecell
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from tqdm import tqdm
from library import *

cd_data = 'data/'
cd_figures = 'figures/'

# %% markdown
# ### Data Import

# %% codecell
users = pd.read_csv(cd_data+'takehome_users.csv',  encoding = "ISO-8859-1")
user_eng = pd.read_csv(cd_data+'takehome_user_engagement.csv')

# %% markdown
# ### Building Week & Day Columns

# %% codecell
user_eng['date_time'] = pd.to_datetime(user_eng['time_stamp'])
user_eng['year'] = user_eng['date_time'].dt.year
user_eng['month'] = user_eng['date_time'].dt.month
user_eng['week'] = user_eng['date_time'].dt.week
user_eng['day_of_week'] = user_eng['date_time'].dt.weekday

# %% markdown
# ### Defining An Adopted User
# %% codecell
user_date_id = define_date_id(user_eng)
user_logins = user_activity(user_date_id, limit=20)
user_adopt = define_adopted_users(user_logins)

# %% codecell
# __aliasing & merge__
activity = user_adopt
adopted = activity[['user_id', 'adopted']].drop_duplicates()
users.rename(columns={'object_id':'user_id'}, inplace=True)
users_merged = users.merge(adopted, on='user_id', how='outer')


# %% markdown
# ### Data Processing

# %% codecell

# Grabbing only the columns that I need
adopted = activity[['user_id', 'adopted']].drop_duplicates()

# Merging the data sets
users.rename(columns={'object_id':'user_id'}, inplace=True)
users_merged = users.merge(adopted, on='user_id', how='outer')

# Alias to shorten code.
df = users_merged
df['adopted'] = pd.to_numeric(df['adopted'])

# Assigning binary values
df['invited_by_user_id'][df['invited_by_user_id'] > 0] = 1
df['invited_by_user_id'].fillna(0, inplace=True)

# One Hot encoding
dum_df = pd.get_dummies(df, columns=['creation_source'])

# Count the adopted users of a feature
storage = []
for col in dum_df.columns:
    storage.append([sum(dum_df[col][dum_df['adopted'] == True])])

column_names = dum_df.columns.to_list()

# %% markdown
# ### Visualization

# %% codecell
data_dict = dict(zip(column_names, storage))
data_df_transposed.index
data_df = pd.DataFrame(data_dict)
data_df_transposed = data_df.transpose()
data_df_transposed.columns = ['adopted']
fig_title = 'adopted_users_by_feature'
plt.figure(figsize=(10,7))
plt.title(fig_title.replace('_', ' ').title())
plt.barh(data_df_transposed.index, width=data_df_transposed['adopted'], color='black')
# plt.xticks(rotation=90)
plt.savefig(cd_figures+fig_title+'.png', transparent=True)

# %% markdown
# ### Observations

# %% markdown
# ### Insights
