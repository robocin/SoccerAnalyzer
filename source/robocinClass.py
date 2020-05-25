import numpy as np
import pandas as pd

import teamClass

LOG = pd.read_csv('./files/t1.rcg.csv')

class Robocin(teamClass.Team):
    def __init__(self):
        super().__init__()
        
        #initialization of values from the dataframe
    def start_values(self):
        pass
    
    #these implementations are not correct!
    def init_RBCNName(self):
            if name != "RoboCIn":
               
            team_left = LOG.iloc[0].team_name_l
            
            if team_left != "RoboCIn":
                self.__name = team_left
            else:
                self.__name = LOG.iloc[0].team_name_r
        else:
            self.__name = name

    def init_RBCNSide(self):
                team_left = LOG.iloc[0].team_name_l
        
        if team_left == self.getName():
            self.__side = "left"
        else:
            self.__side = "right"

    def init_RBCNGoalsPro(self):
        end_row = LOG.loc[LOG["playmode"] == "time_over"]

        if self.getSide == "left":
            score = end_row.team_score_l.to_list()
            return score[0]
        else:
            score = end_row.team_score_r.to_list()
            return score[0]

    
