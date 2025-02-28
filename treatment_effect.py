from IPython import get_ipython
from IPython.display import display
import pandas as pd
import matplotlib.pyplot as plt
import re
import numpy as np
import seaborn as sns
from scipy import stats

# Assuming your datasets are in CSV format 

#--------16 game seasons---------
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

#--------17 game seasons-------
dataset21 = pd.read_csv('2021.csv')
reg_season_21 = dataset21[dataset21['game_id'] <= 272]
playoff_21 = dataset21[dataset21['game_id'] >= 273]

dataset22 = pd.read_csv('2022.csv')
reg_season_22 = dataset22[dataset22['game_id'] <= 272]
playoff_22 = dataset22[dataset22['game_id'] >= 273]

dataset23 = pd.read_csv('2023.csv')
reg_season_23 = dataset23[dataset23['game_id'] <= 272]
playoff_23 = dataset23[dataset23['game_id'] >= 273]

dataset24 = pd.read_csv('2024.csv')
reg_season_24 = dataset21[dataset21['game_id'] <= 272]
playoff_24 = dataset21[dataset21['game_id'] >= 273]

# Add a 'season' column to each dataset
reg_season_17['season'] = 2017
playoff_17['season'] = 2017

reg_season_18['season'] = 2018
playoff_18['season'] = 2018

reg_season_19['season'] = 2019
playoff_19['season'] = 2019

reg_season_20['season'] = 2020
playoff_20['season'] = 2020

reg_season_21['season'] = 2021
playoff_21['season'] = 2021

reg_season_22['season'] = 2022
playoff_22['season'] = 2022

reg_season_23['season'] = 2023
playoff_23['season'] = 2023

reg_season_24['season'] = 2024
playoff_24['season'] = 2024


all_reg_season_data = pd.concat([reg_season_17, reg_season_18, reg_season_19, reg_season_20,
                                 reg_season_21, reg_season_22, reg_season_23, reg_season_24])
all_playoff_data = pd.concat([playoff_17, playoff_18, playoff_19, playoff_20,
                              playoff_21, playoff_22, playoff_23, playoff_24])

from os import stat
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

# Calculate average over/under by season
average_over_under = all_reg_season_data.groupby('season')['over_under'].mean()

# Calculate pre- and post-treatment averages
pre_treatment_avg = average_over_under.loc[[2017, 2018, 2019, 2020]].mean()
post_treatment_avg = average_over_under.loc[[2021, 2022, 2023, 2024]].mean()

# Print the results
print("Pre-treatment Average Over/Under:", pre_treatment_avg)
print("Post-treatment Average Over/Under:", post_treatment_avg)

# Create the bar chart
plt.bar(average_over_under.index, average_over_under.values, color='skyblue', label='Average Over/Under')

# Fit a linear regression model
x = average_over_under.index.values.reshape(-1, 1)
y = average_over_under.values
model = LinearRegression()
model.fit(x, y)

# Plot the regression line
trend_line = model.predict(x)
plt.plot(average_over_under.index, trend_line, color='red', linestyle='--', label='Trend Line')

# Get the slope and intercept
slope = model.coef_[0]
intercept = model.intercept_

# Add equation and R-squared annotation
equation = f'y = {slope:.2f}x + {intercept:.2f}'
equation_text = plt.text(2017.5, 46, equation, color='red', fontsize=12)

# avg_o-u_over_time.png
plt.xlabel('Season')
plt.ylabel('Average Over/Under')
plt.title('RS Average Over/Under Line Over Time with Trend')
plt.xticks(average_over_under.index)
plt.legend()

plt.show()

# Perform t-test
t_statistic, p_value = stats.ttest_ind( # Changed from scipy.stats.ttest_ind to stats.ttest_ind
    all_reg_season_data[all_reg_season_data['season'].isin([2017, 2018, 2019, 2020])]['over_under'],
    all_reg_season_data[all_reg_season_data['season'].isin([2021, 2022, 2023, 2024])]['over_under']
)



# Calculate average total points scored by season
average_total_points = all_reg_season_data.groupby('season').apply(lambda x: (x['home_score'] + x['away_score']).mean())

# Calculate pre- and post-treatment averages
pre_treatment_avg = average_total_points.loc[[2017, 2018, 2019, 2020]].mean()
post_treatment_avg = average_total_points.loc[[2021, 2022, 2023, 2024]].mean()

# Print the results
print("Pre-treatment Average Total Points:", pre_treatment_avg)
print("Post-treatment Average Total Points:", post_treatment_avg)

# Create the bar chart
plt.bar(average_total_points.index, average_total_points.values, color='skyblue', label='Average Total Points')

# Fit a linear regression model
x = average_total_points.index.values.reshape(-1, 1)
y = average_total_points.values
model = LinearRegression()
model.fit(x, y)

# Plot the regression line
trend_line = model.predict(x)
plt.plot(average_total_points.index, trend_line, color='red', linestyle='--', label='Trend Line')

# Get the slope and intercept
slope = model.coef_[0]
intercept = model.intercept_

# Add equation and R-squared annotation
equation = f'y = {slope:.2f}x + {intercept:.2f}'
equation_text = plt.text(2017.5, 46, equation, color='red', fontsize=12)

# avg_tot_ppg_over_time.png
plt.xlabel('Season')
plt.ylabel('Average Total Points Scored')
plt.title('RS Average Total Points Scored Per Game Over Time with Trend')
plt.xticks(average_total_points.index)
plt.legend()

plt.show()

# Perform t-test
from scipy import stats  # Import stats from scipy
t_statistic, p_value = stats.ttest_ind(
    all_reg_season_data[all_reg_season_data['season'].isin([2017, 2018, 2019, 2020])]['home_score'] + all_reg_season_data[all_reg_season_data['season'].isin([2017, 2018, 2019, 2020])]['away_score'], # Calculating total score here
    all_reg_season_data[all_reg_season_data['season'].isin([2021, 2022, 2023, 2024])]['home_score'] + all_reg_season_data[all_reg_season_data['season'].isin([2021, 2022, 2023, 2024])]['away_score']  # Calculating total score here
)



# Calculate average spread by season
average_spread = all_reg_season_data.groupby('season')['spread'].mean()

# Calculate pre- and post-treatment averages
pre_treatment_avg = average_spread.loc[[2017, 2018, 2019, 2020]].mean()
post_treatment_avg = average_spread.loc[[2021, 2022, 2023, 2024]].mean()

# Print the results
print("Pre-treatment Average Spread:", pre_treatment_avg)
print("Post-treatment Average Spread:", post_treatment_avg)

# Create the bar chart
plt.bar(average_spread.index, average_spread.values, color='skyblue', label='Average Spread')

# Fit a linear regression model
x = average_spread.index.values.reshape(-1, 1)
y = average_spread.values
model = LinearRegression()
model.fit(x, y)

# Plot the regression line
trend_line = model.predict(x)
plt.plot(average_spread.index, trend_line, color='red', linestyle='--', label='Trend Line')

# Get the slope and intercept
slope = model.coef_[0]
intercept = model.intercept_

# Add equation and R-squared annotation
equation = f'y = {slope:.2f}x + {intercept:.2f}'
equation_text = plt.text(2017.5, -2.5, equation, color='red', fontsize=12)  

# avg_spread_over_time.png
plt.xlabel('Season')
plt.ylabel('Average Spread')
plt.title('RS Average Spread Over Time with Trend')
plt.xticks(average_spread.index)
plt.legend()

plt.show()

# Perform t-test
t_statistic, p_value = stats.ttest_ind(
    all_reg_season_data[all_reg_season_data['season'].isin([2017, 2018, 2019, 2020])]['spread'],
    all_reg_season_data[all_reg_season_data['season'].isin([2021, 2022, 2023, 2024])]['spread']
)


# Calculate point margin for each game using the provided formula
all_reg_season_data['point_margin'] = all_reg_season_data[['away_score', 'home_score']].max(axis=1) - all_reg_season_data[['away_score', 'home_score']].min(axis=1)

# Calculate average point margin by season
average_point_margin = all_reg_season_data.groupby('season')['point_margin'].mean()

# Calculate pre- and post-treatment averages
pre_treatment_avg = average_point_margin.loc[[2017, 2018, 2019, 2020]].mean()
post_treatment_avg = average_point_margin.loc[[2021, 2022, 2023, 2024]].mean()

# Print the results
print("Pre-treatment Average Point Margin:", pre_treatment_avg)
print("Post-treatment Average Point Margin:", post_treatment_avg)

# Create the bar chart
plt.bar(average_point_margin.index, average_point_margin.values, color='skyblue', label='Average Point Margin')

# Fit a linear regression model
x = average_point_margin.index.values.reshape(-1, 1)
y = average_point_margin.values
model = LinearRegression()
model.fit(x, y)

# Plot the regression line
trend_line = model.predict(x)
plt.plot(average_point_margin.index, trend_line, color='red', linestyle='--', label='Trend Line')

# Get the slope and intercept
slope = model.coef_[0]
intercept = model.intercept_

# Add equation and R-squared annotation
equation = f'y = {slope:.2f}x + {intercept:.2f}'
equation_text = plt.text(2017.5, 10, equation, color='red', fontsize=12)

# avg_point_margin_over_time.png
plt.xlabel('Season')
plt.ylabel('Average Point Margin')
plt.title('RS Average Point Margin Over Time with Trend')
plt.xticks(average_point_margin.index)
plt.legend()

plt.show()

# Perform t-test
t_statistic, p_value = stats.ttest_ind(
    all_reg_season_data[all_reg_season_data['season'].isin([2017, 2018, 2019, 2020])]['point_margin'],
    all_reg_season_data[all_reg_season_data['season'].isin([2021, 2022, 2023, 2024])]['point_margin']
)
