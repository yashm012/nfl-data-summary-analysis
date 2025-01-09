import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import difflib

def determine_favored_team(row):
    """Determines the favored team based on team ID similarity."""
    home_team = row['home_team']
    away_team = row['away_team']
    favorite_id = row['favorite']
    
    # Calculate similarity scores between favorite ID and team names
    home_similarity = difflib.SequenceMatcher(None, favorite_id, home_team).ratio()
    away_similarity = difflib.SequenceMatcher(None, favorite_id, away_team).ratio()
    
    # Return the team name with the highest similarity score
    if home_similarity > away_similarity:
        return home_team
    elif away_similarity > home_similarity:
        return away_team
    else:
        return 'Unknown'  # Handle cases where similarity is equal or unclear

# Apply the function to create a new column 'favored_team'
data['favored_team'] = data.apply(determine_favored_team, axis=1)

def determine_coverage(row):
    # Assuming 'spread_favorite' is the column indicating the favorite team's spread.
    if row['favored_team'] == row['home_team']:  # favored team is home team
        if row['home_score'] - row['away_score'] >= abs(row['spread']):  # home team covered
            return 'Covered'
        else:
            return 'Not Covered'
    elif row['favored_team'] == row['away_team']:  # favored team is away team
        if row['away_score'] - row['home_score'] >= abs(row['spread']):  # away team covered
            return 'Covered'
        else:
            return 'Not Covered'
    else:
        return 'Not Covered'  # Tie or unknown favored team - spread not covered

data['covered'] = data.apply(determine_coverage, axis=1)
data['score_diff'] = data[['home_score', 'away_score']].max(axis=1) - data[['home_score', 'away_score']].min(axis=1)

plt.figure(figsize=(8, 6))
sns.boxplot(x='covered', y='score_diff', data=data)
plt.title('Score Difference Distribution for Covered and Not Covered Games')
plt.xlabel('Coverage')
plt.ylabel('Score Difference')
plt.show()
