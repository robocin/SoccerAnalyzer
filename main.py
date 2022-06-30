import pandas as pd
from socceranalyzer import Match, SSL, MatchAnalyzer
from socceranalyzer import MatchAnalyzer, Match, SIM2D

SIM2D_LOGFILE_PATH = "../output_log/RoboCIn_2-vs-Razi2018_3.rcg.csv"
dataframe = pd.read_csv(SIM2D_LOGFILE_PATH)

match_object = Match(dataframe, SIM2D)
match_analyzer = MatchAnalyzer(match_object)
