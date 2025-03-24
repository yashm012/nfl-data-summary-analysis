# NFL team and betting stats 2017-2024

Raw data for all 8 years were acquired from: 

https://www.sportsoddshistory.com/nfl-game-season/?y={year}

https://www.pro-football-reference.com/years/{year}/games.htm

**change {year} to season of interest; this repo contains data from seasons before and after the establishment of the 17-game NFL season, the first season being in 2021
______________________________________________________________________________________________________________________________________________________

note: when analyzing game spreads, you view it in the context of the favored team (see below)

note: all odds in *2017-24.csv* are specifically **closing** lines; spreads and over/under's change frequently leading up to a game, depending on how heavily bettors place bets in either direction and closing odds means that all lines present were the last lines offered to bettors before the game started
______________________________________________________________________________________________________________________________________________________

key terms:
- 17 game regular season: all 32 teams in the NFL play 17 games over 18 weeks (one bye week with no game scheduled, typically between Week 5 and Week 14, varies by team & season*) during the regular season; all stats with the *reg_season* label are from those first 272 games
- 16 game regular season: all 32 teams in the NFL play 16 games over 17 weeks (one bye week with no game scheduled, typically between Week 5 and Week 13, varies by team & season*) during the regular season; all stats with the *reg_season* label are from those first 256 games
- playoffs: of those 32 teams, 14 move on to the playoffs, where they compete in 4 rounds to hopefully win the Superbowl, the final goal of every season; rounds are as follows: Wildcard Round (WC; 12 teams (top team from each conference gets a bye week)), Divisional Round (DIV; 8 teams), Conference Championship Games (AFCCG/NFCCG; 4 teams), and the Superbowl (SB; 2 teams (one from AFC, one from NFC)); all stats with the *playoffs* label are from those final 13 games (note: a year before the introduction of the 17 game season, the NFL playoffs were limited to 12 teams, 6 from each conference)
- *over/under* (o-u): the total scoring line (both scores combined) on which people can bet money; if the over/under is 49.5, and both teams combine for 50 points, the over hits, and vice versa (note: over/under's will almost always have a half-point projection to avoid a 'push', where the bettor gets their money back; a 'push' would occur in a scenario where the final score is the same as the projected over/under)
- *spread*: to account for discrepancies in the quality of teams on a week-to-week basis, oddsmakers identify a spread that can be covered by either team, but not both; an example would look similar to this: BAL vs CIN(-6.5), which means that CIN is favored by 6.5 points: if CIN wins by more than 6.5 points, they cover the spread, but if BAL loses by less than 6.5, or they win, they cover the spread (note: another way of representing this spread is BAL(+6.5) vs CIN, and most spreads will have a half-point projection to avoid a 'push')
- *team_vs_spread*: this data seeks to identify how well teams play against the spread (ATS); if a team is projected to win by 3.5, and they win by 7, they beat the spread, or if a team is projected to lose by 5.5, and they only lose by 3 (or win), they beat the spread that week; on the flip side, if a team is projected to win by 3.5, and they win by 1 (or lose), they lost against the spread, or if a team is projected to lose by 5.5, and they lose by 14, they lost against the spread that week (note: this provides oddsmakers with a second record for each team (a team could have a 9-5 record, but be 6-8 ATS), which doesn't have any tangible impact on the game or the team, but can serve as useful information for future betting lines); essentially, if a team covered the spread, they're 1-0 ATS that week, and if they don't, they're 0-1 ATS that week
