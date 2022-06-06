import pandas as pd

from socceranalyzer import MatchAnalyzer, Match, SIM2D

SIM2D_LOGFILE_PATH = "../../logs/simulation2d/20220525201055-RoboCIn_2-vs-RandomTeam_2.rcg.csv"
dataframe = pd.read_csv(SIM2D_LOGFILE_PATH)

match_object = Match(dataframe, SIM2D)
match_analyzer = MatchAnalyzer(match_object)
print(match_analyzer.ball_possession.results())