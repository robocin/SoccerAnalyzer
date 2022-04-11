import pandas as pd
from socceranalyzer import MatchAnalyzer, Match, SIM2D

logfile_path = "../output_log/20190706112224-HillStone_3-vs-RoboCIn_1.rcg.csv"
dataframe = pd.read_csv(logfile_path)

match_object = Match(dataframe, SIM2D)
match_analyzer = MatchAnalyzer(match_object)
match_analyzer.intercept_counter.describe()