# Betting and Team stats for the 2022 NFL season **incomplete

Raw data (*raw_data*) acquired and derived from: 

272: https://www.kaggle.com/datasets/ruendymendozachavez/nfl-2023-season-dataset

betting: https://www.kaggle.com/datasets/tobycrabtree/nfl-scores-and-betting-data?select=spreadspoke_scores.csv (spreadspoke_scores.csv)

note: the first dataset says '2023-season', but this is mislabeled, as it contains the games/scores from the 2022 season, which ended in early 2023
______________________________________________________________________________________________________________________________________________________
The *merged-2022.csv* dataset contains key variables from both *272.csv* and *betting.csv* and was used for most if not all, visualizations in folder *viz*.

note: the dataset from which *272.csv* was derived only includes data on the 2022 regular season; the remaining playoff data was added when merging with *betting.csv*

note: when analyzing game spreads, you view it in the context of the favored team (see below)
______________________________________________________________________________________________________________________________________________________

key terms:
- regular season (reg_season): all 32 teams in the NFL play 17 games over 18 weeks during the regular season; all stats with the *reg_season* label are from those first 272 games
- playoffs: of those 32 teams, 14 move on to the playoffs, where they compete in 4 rounds to hopefully win the Superbowl, the final goal of every season; rounds are as follows: Wildcard Round (WC; 12 teams (top team from each conference gets a bye week)), Divisional Round (DIV; 8 teams), Conference Championship Games (AFCCG/NFCCG; 4 teams), and the Superbowl (SB; 2 teams (one from AFC, one from NFC)); all stats with the *playoffs* label are from those final 13 games
- *over/under* (o-u): the total scoring line (both scores combined) on which people can bet money; if the over/under is 49.5, and both teams combine for 50 points, the over hits, and vice versa (note: over/under's will almost always have a half-point projection to avoid a 'push', where the bettor gets their money back; a 'push' would occur in a scenario where the final score is the same as the projected over/under)
- *spread*: to account for discrepancies in the quality of teams on a week-to-week basis, oddsmakers identify a spread that the favored team can cover, or the unfavored team can outperform; an example would look similar to this: BAL vs CIN(-6.5), which means that 6.5 points favor CIN; if CIN wins by more than 6.5 points, they cover the spread, but if BAL loses by less than 6.5, or they win, they outperform their spread (note: another way of representing this spread is BAL(+6.5) vs CIN, and most spreads will have a half-point projection to avoid a 'push')
- *team_vs_spread*: this data seeks to identify how well teams play against the spread (ATS); if a team is projected to win by 3.5, and they win by 7, they beat the spread, or if a team is projected to lose by 5.5, and they only lose by 3 (or win), they beat the spread that week; on the flip side, if a team is projected to win by 3.5, and they win by 1 (or lose), they lost against the spread, or if a team is projected to lose by 5.5, and they lose by 14, they lost against the spread that week (note: this provides oddsmakers with a second record for each team (a team could have a 9-5 record, but be 6-8 ATS), which doesn't have any tangible impact on the game or the team, but can serve as useful information for future betting lines)
