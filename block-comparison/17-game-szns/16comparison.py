# -*- coding: utf-8 -*-
"""16comparison.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1jh7vvMqusd2Ec2jtWqsfYW_BRvC3by11
"""

from IPython import get_ipython
from IPython.display import display
!pip install --force-reinstall pandas 2.2.2
import pandas as pd
import matplotlib.pyplot as plt
import re
import seaborn as sns

# Assuming your datasets are in CSV format
dataset17 = pd.read_csv('2017.csv')
reg_season_17 = dataset17[dataset17['game_id'] <= 256]
playoff_17 = dataset17[dataset17['game_id'] >= 257]

dataset18 = pd.read_csv('2018.csv')
reg_season_18 = dataset18[dataset18['game_id'] <= 256]
playoff_18 = dataset18[dataset18['game_id'] >= 257]

dataset19 = pd.read_csv('2019.csv')
reg_season_19 = dataset19[dataset19['game_id'] <= 256]
playoff_19 = dataset19[dataset19['game_id'] >= 257]

dataset20 = pd.read_csv('2020.csv')
reg_season_20 = dataset20[dataset20['game_id'] <= 256]
playoff_20 = dataset20[dataset20['game_id'] >= 257]

# Assuming all datasets have the same structure
all_reg_season_data = pd.concat([reg_season_17, reg_season_18, reg_season_19, reg_season_20])
all_playoff_data = pd.concat([playoff_17, playoff_18, playoff_19, playoff_20])

def team_id(team_name):
    # Maps a team's name to its team ID
    team_mapping = {
        'Arizona': 'ARI',
        'Atlanta': 'ATL',
        'Baltimore': 'BAL',
        'Buffalo': 'BUF',
        'Carolina': 'CAR',
        'Chicago': 'CHI',
        'Cincinnati': 'CIN',
        'Cleveland': 'CLE',
        'Dallas': 'DAL',
        'Denver': 'DEN',
        'Detroit': 'DET',
        'Green Bay': 'GB',
        'Houston': 'HOU',
        'Indianapolis': 'IND',
        'Jacksonville': 'JAX',
        'Kansas City': 'KC',
        'Los Angeles': 'LAC',
        'Los Angeles': 'LAR',
        'Las Vegas': 'LV',
          'Oakland': 'OAK',
        'Miami': 'MIA',
        'Minnesota': 'MIN',
        'New England': 'NE',
        'New Orleans': 'NO',
        'New York': 'NYG',
        'New York': 'NYJ',
        'Philadelphia': 'PHI',
        'Pittsburgh': 'PIT',
        'San Francisco': 'SF',
        'Seattle': 'SEA',
        'Tampa Bay': 'TB',
        'Tennessee': 'TEN',
        r'Washington.*': 'WAS'  # Include regex to handle variations of Washington's name
    }
    for name, abbrev in team_mapping.items():
        if isinstance(name, str) and name == team_name:  # Check for direct match
            return abbrev
        elif re.match(name, team_name): # Check if the team name matches the regex pattern
            return abbrev

    return team_name #If no match is found, return the original team name

def get_playoff_teams(df):
    """Extracts unique playoff teams from a DataFrame based on game_id range."""
    playoff_games = df[(df['game_id'] >= 257) & (df['game_id'] <= 267)]  # Filter playoff games
    playoff_teams = set(playoff_games['home_team'].unique()).union(playoff_games['away_team'].unique())  # Get unique teams
    return list(playoff_teams)

# Get playoff teams for each year
playoff_teams_2017 = get_playoff_teams(dataset17)
playoff_teams_2018 = get_playoff_teams(dataset18)
playoff_teams_2019 = get_playoff_teams(dataset19)
playoff_teams_2020 = get_playoff_teams(dataset20)

def calculate_avg_scores(df):
    home_scores = df.groupby('home_team')['home_score'].mean().reset_index()
    away_scores = df.groupby('away_team')['away_score'].mean().reset_index()
    # Merge the home and away scores
    avg_scores = pd.merge(home_scores, away_scores, left_on='home_team', right_on='away_team')
    avg_scores = avg_scores.rename(columns={'home_team': 'team', 'home_score': 'avg_home_score', 'away_score': 'avg_away_score'})

    # Handle missing teams (Modified)
    all_teams = set(df['home_team'].unique()).union(df['away_team'].unique())
    missing_teams = all_teams - set(avg_scores['team'])

    for team in missing_teams:
        avg_scores = pd.concat([avg_scores, pd.DataFrame({'team': [team], 'avg_home_score': [0], 'avg_away_score': [0]})], ignore_index=True)

    # avg_scores = avg_scores.dropna()  # Remove this line to keep all teams

    return avg_scores

rs_avg_scores_17 = calculate_avg_scores(reg_season_17)
rs_avg_scores_18 = calculate_avg_scores(reg_season_18)
rs_avg_scores_19 = calculate_avg_scores(reg_season_19)
rs_avg_scores_20 = calculate_avg_scores(reg_season_20)

p_avg_scores_17 = calculate_avg_scores(playoff_17)
p_avg_scores_18 = calculate_avg_scores(playoff_18)
p_avg_scores_19 = calculate_avg_scores(playoff_19)
p_avg_scores_20 = calculate_avg_scores(playoff_20)

# Create subplots; 17-20_rs_ppg_HvA.png
fig, axes = plt.subplots(1, 4, figsize=(15, 5))

# Set the x and y limits for all subplots
for ax in axes:
    ax.set_xlim(7, 40)
    ax.set_ylim(7, 40)

# Scatterplot for 2017 with playoff teams highlighted
ax = axes[0]  # Assign the current axes object
for i, row in rs_avg_scores_17.iterrows():
    team_name = row['team']
    team_abbrev = team_id(team_name)
    # Updated highlighting condition
    is_playoff_team = team_name in playoff_teams_2017 or team_abbrev in playoff_teams_2017
    color = 'red' if is_playoff_team else 'blue'
    ax.scatter(row['avg_home_score'], row['avg_away_score'], color=color)
    ax.annotate(team_abbrev, (row['avg_home_score'], row['avg_away_score']))

# Do the same updates to the plotting loops for 2018, 2019 and 2020

ax.set_title('2017 RS: avg home score vs avg away score')
ax.set_xlabel('Average RS Home Score')
ax.set_ylabel('Average RS Away Score')

# Scatterplot for 2018 with playoff teams highlighted
ax = axes[1]  # Assign the current axes object
for i, row in rs_avg_scores_18.iterrows():
    team_name = row['team']
    team_abbrev = team_id(team_name)
    # Updated highlighting condition
    is_playoff_team = team_name in playoff_teams_2018 or team_abbrev in playoff_teams_2018
    color = 'red' if is_playoff_team else 'blue'
    ax.scatter(row['avg_home_score'], row['avg_away_score'], color=color)
    ax.annotate(team_abbrev, (row['avg_home_score'], row['avg_away_score']))

# Do the same updates to the plotting loops for 2018, 2019 and 2020

ax.set_title('2018 RS: avg home score vs avg away score')
ax.set_xlabel('Average RS Home Score')
ax.set_ylabel('Average RS Away Score')

# Scatterplot for 2019 with playoff teams highlighted
ax = axes[2]  # Assign the current axes object
for i, row in rs_avg_scores_19.iterrows():
    team_name = row['team']
    team_abbrev = team_id(team_name)
    # Updated highlighting condition
    is_playoff_team = team_name in playoff_teams_2019 or team_abbrev in playoff_teams_2019
    color = 'red' if is_playoff_team else 'blue'
    ax.scatter(row['avg_home_score'], row['avg_away_score'], color=color)
    ax.annotate(team_abbrev, (row['avg_home_score'], row['avg_away_score']))

# Do the same updates to the plotting loops for 2018, 2019 and 2020

ax.set_title('2019 RS: avg home score vs avg away score')
ax.set_xlabel('Average RS Home Score')
ax.set_ylabel('Average RS Away Score')

# Scatterplot for 2020 with playoff teams highlighted
ax = axes[3]  # Assign the current axes object
for i, row in rs_avg_scores_20.iterrows():
    team_name = row['team']
    team_abbrev = team_id(team_name)
    # Updated highlighting condition
    is_playoff_team = team_name in playoff_teams_2020 or team_abbrev in playoff_teams_2020
    color = 'red' if is_playoff_team else 'blue'
    ax.scatter(row['avg_home_score'], row['avg_away_score'], color=color)
    ax.annotate(team_abbrev, (row['avg_home_score'], row['avg_away_score']))

ax.set_title('2020 RS: avg home score vs avg away score')
ax.set_xlabel('Average RS Home Score')
ax.set_ylabel('Average RS Away Score')

# Create dummy scatter plots for the legend
ax.scatter([], [], color='red', label='Playoff Team')
ax.scatter([], [], color='blue', label='Non-Playoff Team')
ax.legend(loc='best')  # Adjust 'loc' for optimal placement

plt.tight_layout()
plt.show()

num_dots_2017 = len(rs_avg_scores_17)
num_dots_2018 = len(rs_avg_scores_18)
num_dots_2019 = len(rs_avg_scores_19)
num_dots_2020 = len(rs_avg_scores_20)

print(f"Number of dots in 2021: {num_dots_2017}")
print(f"Number of dots in 2022: {num_dots_2018}")
print(f"Number of dots in 2023: {num_dots_2019}")
print(f"Number of dots in 2024: {num_dots_2020}")

# Create subplots for spread countplots; 17-20_spread_distr.png
fig, axes = plt.subplots(1, 4, figsize=(15, 5))

# Set the x and y limits for all subplots
for ax in axes:
    ax.set_xlim(-18.5, 0)
    ax.set_ylim(0, 75)

# Spread countplot for 2017
sns.histplot(dataset17['spread'], bins=20, ax=axes[0], color='skyblue')  # Using histplot from seaborn
axes[0].set_title('2017 Spread Distribution')
axes[0].set_xlabel('Spread')
axes[0].set_ylabel('Frequency')
axes[0].spines[['top', 'right']].set_visible(False)

# Spread countplot for 2018
sns.histplot(dataset18['spread'], bins=20, ax=axes[1], color='salmon')
axes[1].set_title('2018 Spread Distribution')
axes[1].set_xlabel('Spread')
axes[1].set_ylabel('Frequency')
axes[1].spines[['top', 'right']].set_visible(False)

# Spread countplot for 2019
sns.histplot(dataset19['spread'], bins=20, ax=axes[2], color='lightgreen')
axes[2].set_title('2019 Spread Distribution')
axes[2].set_xlabel('Spread')
axes[2].set_ylabel('Frequency')
axes[2].spines[['top', 'right']].set_visible(False)

# Spread countplot for 2020
sns.histplot(dataset20['spread'], bins=20, ax=axes[3], color='yellow')
axes[3].set_title('2020 Spread Distribution')
axes[3].set_xlabel('Spread')
axes[3].set_ylabel('Frequency')
axes[3].spines[['top', 'right']].set_visible(False)

plt.tight_layout()
plt.show()

# avg_total_ppg.png
years = [2017, 2018, 2019, 2020]
avg_total_points = []

for year in years:
  dataset = pd.read_csv(f'{year}.csv')
  avg_total_points.append(dataset[['home_score', 'away_score']].sum(axis=1).mean())

plt.plot(years, avg_total_points, marker='o')
plt.title('Average Total Points Scored per Game')
plt.xlabel('Year')
plt.ylabel('Average Points')
plt.grid(True)
plt.show()

def count_wins(df, playoff_games=False):
    """Counts the number of wins for each team, optionally filtering for playoff games."""
    if playoff_games:
        games_df = df[df['game_id'] >= 257]  # Filter for playoff games
    else:
        games_df = df[df['game_id'] <= 256]  # Filter for regular season games

    # Create a 'winner' column based on scores
    games_df['winner'] = games_df.apply(
        lambda row: row['home_team'] if row['home_score'] > row['away_score'] else row['away_team'],
        axis=1
    )

    wins_by_team = games_df.groupby('winner')['game_id'].count().reset_index()
    wins_by_team = wins_by_team.rename(columns={'winner': 'team', 'game_id': 'wins'})
    return wins_by_team

# Get regular season wins for each year
wins_2017 = count_wins(dataset17, playoff_games=False)
wins_2018 = count_wins(dataset18, playoff_games=False)
wins_2019 = count_wins(dataset19, playoff_games=False)
wins_2020 = count_wins(dataset20, playoff_games=False)

# Get playoff wins for each year
playoff_wins_2017 = count_wins(dataset17, playoff_games=True)
playoff_wins_2018 = count_wins(dataset18, playoff_games=True)
playoff_wins_2019 = count_wins(dataset19, playoff_games=True)
playoff_wins_2020 = count_wins(dataset20, playoff_games=True)

# Get all unique teams across all years
all_teams = set(wins_2017['team']).union(wins_2018['team']).union(wins_2019['team']).union(wins_2020['team'])

team_performance = {}
for year, wins_df, playoff_wins_df, playoff_teams in zip(
    [2017, 2018, 2019, 2020],
    [wins_2017, wins_2018, wins_2019, wins_2020],
    [playoff_wins_2017, playoff_wins_2018, playoff_wins_2019, playoff_wins_2020],
    [playoff_teams_2017, playoff_teams_2018, playoff_teams_2019, playoff_teams_2020],
):
    for team in all_teams:  # Iterate through all teams
        wins = wins_df.loc[wins_df['team'] == team, 'wins'].values[0] if team in wins_df['team'].values else 0
        playoff_wins = playoff_wins_df.loc[playoff_wins_df['team'] == team, 'wins'].values[0] if team in playoff_wins_df['team'].values else 0
        made_playoffs = team in playoff_teams

        # Adjust criteria to include playoff wins (example)
        if wins >= 10 and made_playoffs and playoff_wins >= 1:  # Example: Requires at least 2 playoff wins
            team_performance[team] = team_performance.get(team, 0) + 1
        else:
            team_performance[team] = team_performance.get(team, 0)  # Initialize to 0 if not meeting criteria

team_classifications = {}
for team, playoff_count in team_performance.items():
    # Calculate average wins over 4 years (including playoff wins)
    yearly_wins = [wins_df.loc[wins_df['team'] == team, 'wins'].values[0] if team in wins_df['team'].values else 0
                   for wins_df in [wins_2017, wins_2018, wins_2019, wins_2020]]
    yearly_playoff_wins = [playoff_wins_df.loc[playoff_wins_df['team'] == team, 'wins'].values[0] if team in playoff_wins_df['team'].values else 0
                           for playoff_wins_df in [playoff_wins_2017, playoff_wins_2018, playoff_wins_2019, playoff_wins_2020]]

    avg_wins = sum(yearly_wins) / len(yearly_wins)
    avg_playoff_wins = sum(yearly_playoff_wins) / len(yearly_playoff_wins)

    # Introduce tolerance for average wins
    if playoff_count == 4 and avg_wins >= 10 and avg_playoff_wins >= 2:
        team_classifications[team] = "Dynasty"
    elif playoff_count >= 3 and avg_wins >= 10 and avg_playoff_wins >=1:
        team_classifications[team] = "Dominant"
    elif playoff_count >= 2 and avg_wins >= 10:
        team_classifications[team] = "Annual Contender"
    elif playoff_count >= 2 or avg_wins >= 10:
        team_classifications[team] = "Inconsistent Contender"
    elif (8 <= avg_wins < 10):  # Tolerance for Mediocre category
        team_classifications[team] = "Mediocre"
    elif (1 <= avg_wins <= 6):
        team_classifications[team] = "BOTB" # 'bottom of the barrel' teams
    else:
        team_classifications[team] = "Non-Contender"

team_classification_df = pd.DataFrame(
    list(team_classifications.items()), columns=["Team", "Classification"]
)
print(team_classification_df)

!pip install plotly==5.15.0
import plotly.express as px
import plotly.graph_objects as go

# Create a list of years
years = [2017, 2018, 2019, 2020]

# Create an empty list to store the data for the chart
chart_data = []

# Iterate through the years and teams to accumulate the data
for year, wins_df, playoff_wins_df in zip(
    years,
    [wins_2017, wins_2018, wins_2019, wins_2020],
    [playoff_wins_2017, playoff_wins_2018, playoff_wins_2019, playoff_wins_2020],
):
    for team in wins_df['team']:
        wins = wins_df.loc[wins_df['team'] == team, 'wins'].values[0]
        playoff_wins = playoff_wins_df.loc[
            playoff_wins_df['team'] == team, 'wins'
        ].values[0] if team in playoff_wins_df['team'].values else 0

        chart_data.append([team, year, wins, playoff_wins])

# Create a Pandas DataFrame from the chart data
df_chart = pd.DataFrame(
    chart_data, columns=['Team', 'Year', 'Wins', 'Playoff Wins']
)

# Calculate total wins for each team across all seasons
df_chart['Total Wins'] = df_chart.groupby('Team')['Wins'].transform('sum')

# Create a list of unique teams
teams = df_chart['Team'].unique()

# Create the initial figure using graph_objects
fig = go.Figure()

# Show legend
fig.update_layout(showlegend=True)

# Add the regular season wins bars and playoff wins bars for all teams within the same loop
traces = []  # Create a list to store traces

for team in teams:
    team_data = df_chart[df_chart['Team'] == team]

    # Create a 'Playoffs' column based on whether the team is in playoff_teams for the year
    team_data['Playoffs'] = team_data['Year'].apply(lambda year: team in globals()[f'playoff_teams_{year}'])

    # Add regular season bars (blue)
    traces.append(
        go.Bar(
            x=team_data['Year'],
            y=team_data['Wins'],
            name=team,
            marker_color='blue',  # Set color to blue for regular season wins
            hovertemplate='<b>%{data.name}</b><br>Season: %{x}<br>Regular Season Wins: %{y}<br>Total Wins: %{customdata[0]}<br>Playoffs: %{customdata[1]}<br>Playoff Wins: %{customdata[2]}',
            customdata=team_data[['Total Wins', 'Playoffs', 'Playoff Wins']].values,
            offsetgroup=team,
            visible=False,  # All traces are initially hidden
            showlegend=False  # Hide individual team legends
        )
    )

    # Add playoff wins bars (red, only if there are playoff wins)
    if team_data['Playoff Wins'].sum() > 0:
        traces.append(
            go.Bar(
                x=team_data['Year'][team_data['Playoffs'] & (team_data['Playoff Wins'] > 0)],
                y=team_data['Playoff Wins'][team_data['Playoffs'] & (team_data['Playoff Wins'] > 0)],
                name=team + ' Playoffs',
                marker_color='red',  # Set color to red for playoff wins
                showlegend=False,  # Hide individual team legends for playoffs
                offsetgroup=team,
                hovertemplate='<b>%{data.name}</b><br>Season: %{x}<br>Playoff Wins: %{y}',
                visible=False  # All traces are initially hidden
            )
        )

# Add traces to the figure
fig.add_traces(traces)

# Create dummy scatter plots for the legend
fig.add_trace(go.Scatter(x=[None], y=[None], mode='markers',
                         marker=dict(size=10, color='blue'),
                         name='Regular Season Wins', visible='legendonly'))  # Visible only in legend
fig.add_trace(go.Scatter(x=[None], y=[None], mode='markers',
                         marker=dict(size=10, color='red'),
                         name='Playoff Wins', visible='legendonly'))  # Visible only in legend

# Make the first team's data visible initially
fig.data[0].visible = True
fig.data[1].visible = True if len(fig.data) > 1 and fig.data[1].name == fig.data[0].name + ' Playoffs' else False

# Calculate maximum wins and set y-axis range
max_wins = df_chart[['Wins', 'Playoff Wins']].max().max()  # Find max across both columns
fig.update_layout(yaxis_range=[0, max_wins + 1])  # Set y-axis range

# Update layout
fig.update_layout(
    barmode='stack',  # Changed to 'stack' to stack bars
    title='Regular Season and Playoff Wins by Team (2021-2024)',
    xaxis={'type': 'category', 'categoryorder': 'array', 'categoryarray': [2021, 2022, 2023, 2024]},
    yaxis_title='Wins',
    yaxis_range=[0, 20],
    showlegend=True,  # Legend is already shown
    updatemenus=[
        dict(
            type="dropdown",
            active=0,
            buttons=[
                dict(
                    label=team,
                    method="update",
                    args=[{"visible": [(trace.name == team or trace.name == team + ' Playoffs') for trace in fig.data]}]
                )
                for team in teams
            ]
        )
    ]
)

# Show the chart
fig.show()