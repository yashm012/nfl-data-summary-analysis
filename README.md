# Betting and Team stats for the 2022 NFl season **incomplete

Raw data (*raw_data*) acquired and derived from: 

272: https://www.kaggle.com/datasets/ruendymendozachavez/nfl-2023-season-dataset

betting: https://www.kaggle.com/datasets/tobycrabtree/nfl-scores-and-betting-data?select=spreadspoke_scores.csv (spreadspoke_scores.csv)

note: the first dataset says '2023-season', but this is mislabeled, as these are the games/scores from the 2022 season, which ended in early 2023


The *merged-2022.csv* dataset contains key variables from both *272.csv* and *betting.csv*, and was used for most, if not all, visualizations in folder *viz*.

key terms:
- over/under (o-u): the total scoring line (both scores combined) on which people can bet money; if the over/under is 49.5, and both teams combine for 50 points, the over hits, and vice versa (note: over/under's will almost always have a half-point projection to avoid a 'push', where the bettor simply gets their money back; a 'push' would occur in a scenario where the final score is the same as the projected over/under)
- spread: 
