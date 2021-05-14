import sys
import os
import pandas as pd
import math
"""
    Pandas is needed to run this script.
    py retreat.py "location_to_log"
"""
PATH = sys.argv[1]

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
        self.__findUniqueEventOcurrences('back_pass_' + self.__side)
        
        
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


    def getwRetreat(self):
        return self.__wRetreat

    def getFaultRetreat(self):
        
        second_playmode = 'indirect_free_kick_' + self.__opSide
        
        for cycle in self.__ocurrencesIndexes:
            
            mode =  self.__df.loc[cycle]['playmode']
            nextMode = mode
            fCycle = cycle

            ''' 
                depois de pegar as ocorrencias de um back_pass_ 
                verifica se a flag de sequencia é um indirect_free_kick
                e se for está sabemos que foi falta por recuo aliado.
            '''
            while(mode == nextMode):
                fCycle = fCycle + 1
                nextMode = self.__df.loc[fCycle]['playmode']
                
            if nextMode == 'indirect_free_kick_' + self.__opSide:
                self.__wRetreat = self.__wRetreat + 1
                self.__wRetreatAt.append(cycle)
            
        #print("{} wrong retreats\nAt cycles: {}".format(self.__wRetreat, self.__wRetreatAt))
        

def main():
    totwRetreats = 0
    totFiles = 0
    bad_files = []
    for _, _, files in os.walk(PATH):
        for file in files:
            if(".csv" in file):
                #print("Looking in file {}".format(file))
                
                totFiles = totFiles + 1
                log = pd.read_csv(os.path.join(PATH, file))
                
                gk = Goalkeeper(log)
                gk.getFaultRetreat()

                if gk.getwRetreat() > 0:
                    bad_files.append(file)
                    totwRetreats = totwRetreats + gk.getwRetreat()

    print("Total files:", totFiles)
    print("Total wrong retreats {}".format(totwRetreats))

if __name__ == "__main__":
    main()

