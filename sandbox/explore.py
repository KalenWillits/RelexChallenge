# sandbox/explore.py

# percent of users not adopted
not_adopted = user_adopted[user_adopted['adopted_users'] == False]['adopted_users'].sum()

not_adopted/sum(user_adopted['adopted_users'])
not_adopted


max(user_logins['user_activity'])
sns.heatmap(user_adopt.corr())
