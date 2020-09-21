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
# -[Exploring Features Contributing To User Adoption](#Exploring-Features-Contributing-To-User-Adoption)

# %% markdown
# ### Environment

# %% codecell
import numpy as np
import matplotlib.pyplot as pyplot
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
user_logins = user_activity(user_date_id, limit=100)
user_adopt = define_adopted_users(user_logins)

# %% markdown
# ### Exploring Features Contributing To User Adoption

# %% codecell
