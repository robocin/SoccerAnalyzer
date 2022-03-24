import pandas as pd
from socceranalyzer import MatchAnalyzer, Match, SIM2D

logfile_path = "../data/20190705100545-RoboCIn_1-vs-HillStone_0.rcg.csv"
dataframe = pd.read_csv(logfile_path)

match_object = Match(dataframe, SIM2D)
match_analyzer = MatchAnalyzer(match_object)
match_analyzer.ball_possession.describe()