import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('merged-2022.csv')
data['total_score'] = data['home_score'] + data['away_score']
data['over_under_result'] = data['total_score'] - data['over_under']
data['game_result'] = np.where(data['over_under_result'] > 0, 'Over', 'Under')

# Create a list of playoff game IDs
playoff_game_ids = data[data['game_id'] >= 273]['game_id'].unique()

# Get a list of unique playoff teams (both home and away)
playoff_teams = pd.concat([data[data['game_id'].isin(playoff_game_ids)]['home_team'],
                         data[data['game_id'].isin(playoff_game_ids)]['away_team']]).unique()

reg_season_data = data[data['game_id'] <= 272]
playoff_data = data[data['game_id'] >= 273]

# Countplot; reg_season_o/u.png
plt.figure(figsize=(8, 6))
sns.countplot(x='game_result', data=reg_season_data, palette=['blue'], order=['Over', 'Under'])
plt.title('# of Regular Season Games Over/Under')
plt.xlabel('Game Result')
plt.ylabel('Count')
plt.show()

# Playoff countplot; playoff_o/u.png
plt.figure(figsize=(8, 6))
sns.countplot(x='game_result', data=playoff_data, palette=['red'], order=['Over', 'Under'])
plt.title('# of Playoff Games Over/Under')
plt.xlabel('Game Result')
plt.ylabel('Count')
plt.show()

# Boxplot; o/u_result_distribution.png
plt.figure(figsize=(8, 6))
sns.boxplot(x='game_result', y='over_under_result', data=data,
            hue=data['game_id'].isin(playoff_game_ids).map({True: 'Playoffs', False: 'Regular Season'}),  # Map to strings
            palette=['blue', 'red'], order=['Over', 'Under'])  # Choose colors for regular and playoff games
plt.title('Over/Under Result Distribution')
plt.xlabel('Game Result')
plt.ylabel('Over/Under Result')
plt.legend(title='Game type', loc='upper right')  # Adjust legend location if needed
plt.show()

# Countplot; team_o/u.png
# Create a new DataFrame to store team-wise over/under counts
team_over_under = pd.DataFrame(columns=['team', 'over_count', 'under_count'])

# Iterate through each game in your data
for index, row in data.iterrows():
    home_team = row['home_team']
    away_team = row['away_team']
    total_score = row['home_score'] + row['away_score']
    over_under = row['over_under']

    # Determine if the game was over or under
    game_result = 'over' if total_score > over_under else 'under'

    # Add new teams if not already in the DataFrame
    for team in [home_team, away_team]:  # Iterate through both home and away teams
        if team not in team_over_under['team'].values:
            team_over_under = pd.concat([team_over_under, pd.DataFrame({'team': [team], 'over_count': [0], 'under_count': [0]})], ignore_index=True)

    # Now update counts for both teams (since they are guaranteed to be in the DataFrame)
    team_over_under.loc[team_over_under['team'] == home_team, game_result + '_count'] += 1
    team_over_under.loc[team_over_under['team'] == away_team, game_result + '_count'] += 1

# Reshape the DataFrame to long format for seaborn
team_over_under_long = pd.melt(team_over_under, id_vars=['team'], 
                               value_vars=['over_count', 'under_count'],
                               var_name='game_result', value_name='count')
team_over_under_long['game_result'] = team_over_under_long['game_result'].str.replace('_count', '') # remove "_count"


plt.figure(figsize=(12, 6)) # Adjust figure size to accommodate all teams
sns.barplot(x='team', y='count', hue='game_result', data=team_over_under_long, palette=['black', 'gold']) # Use barplot for count data
plt.title('# of Games Over/Under per Team')
plt.xlabel('Teams')
plt.ylabel('Count')
plt.xticks(rotation=45, ha='right')  # Rotate x-axis labels for readability
plt.tight_layout() # Adjust layout to prevent labels from overlapping
plt.show()
