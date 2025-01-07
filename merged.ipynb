import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df1 = pd.read_csv('272.csv')
df2 = pd.read_csv('betting.csv')

# Convert 'week' column in both dataframes to the same data type (e.g., int)
df1['week'] = pd.to_numeric(df1['week'], errors='coerce').astype('Int64') #errors='coerce' to handle potential non-numeric values
df2['week'] = pd.to_numeric(df2['week'], errors='coerce').astype('Int64') #errors='coerce' to handle potential non-numeric values

# Remove leading/trailing spaces from 'home_team' and 'away_team'
df1['home_team'] = df1['home_team'].str.strip()
df1['away_team'] = df1['away_team'].str.strip()
df2['home_team'] = df2['home_team'].str.strip()
df2['away_team'] = df2['away_team'].str.strip()

# Remove duplicate rows
df1.drop_duplicates(subset=['week', 'home_team', 'away_team'], inplace=True)
df2.drop_duplicates(subset=['week', 'home_team', 'away_team'], inplace=True)

data = pd.merge(df1, df2, on=['week','home_team','away_team'])
data
