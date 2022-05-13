import pandas as pd
from socceranalyzer import Match, SSL, MatchAnalyzer

SSL_LOG_PATH = ""
SIM2D_LOG_PATH = ""
VSS_LOG_PATH = ""

dataframe = pd.read_csv(SSL_LOG_PATH)

m = Match(dataframe, SSL)
ma = MatchAnalyzer(m)
