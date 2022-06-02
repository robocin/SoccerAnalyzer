import pandas as pd
from socceranalyzer import Match, SSL, MatchAnalyzer

from socceranalyzer import Match, SIM2D, SSL, MatchAnalyzer

logpath = "../output_log/RoboCIn_2-vs-Razi2018_3.rcg.csv"

df = pd.read_csv(logpath)
m = Match(df, SIM2D)
ma = MatchAnalyzer(m)
ma.intercept_counter.describe()