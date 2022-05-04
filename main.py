import pandas as pd

logpath = "../data/vss/rc-vs-thunder.csv"

df = pd.read_csv(logpath)
print(df.loc[0 , "showtime"] - df.loc[1, "showtime"])