import pandas as pd

logpath = "/home/ronald/Documents/Code/SoccerAnalyzer/20190704111046-RoboCIn_2-vs-Razi2018_3.rcg.csv"

df = pd.read_csv(logpath)
print(df.loc[0 , "showtime"] - df.loc[1, "showtime"])