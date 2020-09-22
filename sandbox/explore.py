# sandbox/explore.py

# percent of users not adopted
not_adopted = user_adopted[user_adopted['adopted'] == False]['adopted'].sum()

not_adopted/sum(user_adopted['adopted'])
not_adopted


max(user_logins['user_activity'])
sns.heatmap(user_adopt.corr())

# Possible adoption rate sources:
# - Creation source
# - Marketing Drip
# - Org id
# - Invited by User


users_columns = users.columns.to_list()

adopted = activity[['user_id', 'adopted']].drop_duplicates()

users.rename(columns={'object_id':'user_id'}, inplace=True)
users_merged = users.merge(adopted, on='user_id', how='outer')

users_merged.columns
users_merged.info()


# Define this . Count the users that are adopted for each feature.

df = users_merged
df['adopted'] = pd.to_numeric(df['adopted'])

df[df['opted_in_to_mailing_list'] == True]['adopted'].sum()
df['creation_source'] # turn this into one-hot
df['org_id']

# change invited by userID into a boolean.
df = df[['creation_source', 'opted_in_to_mailing_list', 'enabled_for_marketing_drip', 'invited_by_user_id', 'adopted']]
df['creation_source'].unique()


df['invited_by_user_id'][df['invited_by_user_id'] > 0] = 1


df['invited_by_user_id'].fillna(0, inplace=True)

dum_df = pd.get_dummies(df, columns=['creation_source'])

# Count the adopted users of a feature
storage = []
for col in dum_df.columns:
    storage.append(sum(dum_df[col][dum_df['adopted'] == True]))

column_names = dum_df.columns.to_list()

fig_title = 'Adopted Users by Feature'
plt.figure(fig_size=10,7)
pd.DataFrame(zip(column_names, storage)).hist(grid=False, color='black')
plt.xticks(column_names, rotation=45)
plt.savefig(cd_figures+fig_title+'.png', transparent=True)
