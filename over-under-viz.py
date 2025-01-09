import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('merged-2022.csv')
data['total_score'] = data['home_score'] + data['away_score']
data['over_under_result'] = data['total_score'] - data['over_under']
data['game_result'] = np.where(data['over_under_result'] > 0, 'Over', 'Under')

# Countplot
plt.figure(figsize=(8, 6))
sns.countplot(x='game_result', data=data)
plt.title('Distribution of Over/Under Games')
plt.xlabel('Game Result')
plt.ylabel('Count')
plt.show()

# Boxplot
plt.figure(figsize=(8, 6))
sns.boxplot(x='game_result', y='over_under_result', data=data)
plt.title('Over/Under Result Distribution')
plt.xlabel('Game Result')
plt.ylabel('Over/Under Result')
plt.show()

