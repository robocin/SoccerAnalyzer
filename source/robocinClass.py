import numpy as np
import pandas as pd

import teamClass

LOG = pd.read_csv('./files/t1.rcg.csv')

class Robocin(teamClass.Team):
    def __init__(self):
        super().__init__()
        
        self.setName("Robocin")
