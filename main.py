import pandas as pd
from socceranalyzer import MatchAnalyzer, Match, SIM2D

logpath = "../output_log/GYUVm0P_server2_PYRUS_4-vs-RoboCIn_0.rcg.csv"

df = pd.read_csv(logpath)

match_object = Match(df, SIM2D)
match_analyzer = MatchAnalyzer(match_object)
match_analyzer.passing_accuracy.describe()