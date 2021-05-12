import sys
import os
import pandas as pd
import math
"""
    Pandas is needed to run this script.
    py retreat.py "location_to_log"
"""
FOLDER = sys.argv[1]

def distance(px, py, bx, by):

    dist = math.sqrt(pow(bx - px, 2) + pow(by - py,2))

    return dist

class Goalkeeper:
    def __init__(self, dataframe):
        self.__wRetreat = 0
        self.__wRetreatAt = []
        self.__side = None
        self.__opSide = None
        self.__df = dataframe
        self.__ocurrencesIndexes = None
        self.__setSide()
        self.__findUniqueEventOcurrences('foul_charge_' + self.__side)
        
        
    def __setSide(self):
        
        if self.__df.iloc[0,2] == 'RoboCIn':
            self.__side = 'l'
            self.__opSide = 'r'
        else:
            self.__side = 'r'
            self.__opSide = 'l'
            
    def __filterPlaymode(self, playmode : str):
        filteredDataframe = self.__df[self.__df['playmode'] == playmode]
        return filteredDataframe
    
    def __findUniqueEventOcurrences(self, event):
    
        event_ocurrences_index = []

        for i in range(len(self.__df)):
            if(event in self.__df.iloc[i,1] and event not in self.__df.iloc[i-1,1] ):
                 event_ocurrences_index.append(i)
                    
        self.__ocurrencesIndexes = event_ocurrences_index

    def getFaultRetreat(self):
        
        for cycle in self.__ocurrencesIndexes:
            
            ball_x = self.__df.loc[cycle - 1]["ball_x"]
            ball_y = self.__df.loc[cycle - 1]["ball_y"]
            
            gk_x = self.__df.loc[cycle - 1]["player_{}1_x".format(self.__side)]
            gk_y = self.__df.loc[cycle - 1]["player_{}1_y".format(self.__side)]
            
            # Parte importante do código
            # Verifica a distância do goleiro para a bola um ciclo antes da falta ser cometida.

            if distance(gk_x, gk_y, ball_x, ball_y) < 5:  # <- distancia do goleiro para bola
                self.__wRetreat = self.__wRetreat + 1
                self.__wRetreatAt.append(cycle - 1)
            
        print("{} wrong retreats\nAt cycles: {}".format(self.__wRetreat, self.__wRetreatAt))
        

def main():

    for _, _, files in os.walk(FOLDER):
        for file in files:
            if(".csv" in file):
                log = pd.read_csv("./{}/{}".format(FOLDER, file))

                gk = Goalkeeper(log)
                gk.getFaultRetreat()


if __name__ == "__main__":
    main()

