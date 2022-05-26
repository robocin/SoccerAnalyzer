import pandas as pd
from socceranalyzer import Match, SSL, MatchAnalyzer

from socceranalyzer import Match, SIM2D, SSL, MatchAnalyzer

logpath = "../../logs/ssl/robocin-er-force-robocup2021.csv"

df = pd.read_csv(logpath)
m = Match(df, SSL)
ma = MatchAnalyzer(m)


