import pandas as pd
import matplotlib.pyplot as plt
from socceranalyzer import Match, SSL, MatchAnalyzer

from socceranalyzer import Match, SIM2D, SSL, MatchAnalyzer
from socceranalyzer.jupyter.jupyter_adapter import JupyterAdapter

logpath = "../../logs/simulation2d/20220525201055-RoboCIn_2-vs-RandomTeam_2.rcg.csv"

df = pd.read_csv(logpath)
m = Match(df, SIM2D)
ma = MatchAnalyzer(m)

ja = JupyterAdapter(ma)

ja.fault_position(10,10)
ja.ball_possession(10,10)