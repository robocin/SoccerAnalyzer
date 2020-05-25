import numpy as np
import pandas as pd

import teamClass
import positionClass
import eventClass

LOG = pd.read_csv('./files/t1.rcg.csv')

class Oponent(teamClass.Team):
    def __init__(self):
        super().__init__()
        
    def start_values(self):
        pass
    