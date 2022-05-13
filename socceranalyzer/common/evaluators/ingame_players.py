import pandas as pd

from socceranalyzer.common.basic.match import Match
from socceranalyzer.common.enums.sim2d import SIM2D
from socceranalyzer.common.enums.ssl import SSL 
from socceranalyzer.common.enums.vss import VSS

class IngamePlayers:
    def __init__(self, match: Match) -> None:
        self.__match: Match = match
        self.__category: SIM2D | SSL | VSS = match.category
        self.__left_players: list[bool, int] = [[False, ith] for ith in range(0, int(str(self.__category.MAX_PLAYERS)) + 1)]
        self.__right_players: list[bool, int] = [[False, ith] for ith in range(0, int(str(self.__category.MAX_PLAYERS)) + 1)]

        self.__detect()

        if self.__match is None:
            print("No Match object was given, please provide one.")

    def players(self):
        return (self.__left_players, self.__right_players)

    @property
    def left_players(self):
        return self.__left_players

    @property
    def right_players(self):
        return self.__right_players

    def __detect(self):
        log = self.__match.dataframe

        for ith in range(0, int(str(self.__category.MAX_PLAYERS)) + 1):
            column = f'player_{ith}_x'
            
            if pd.notna(log.loc[0][column]):
                self.__left_players[ith] = [True, ith]


    def count_left(self) -> int:
        players = 0
        for player_active in self.__left_players:
            if player_active[0]:
                players += 1
        
        return players 

    def count_right(self) -> int:
        players = 0
        for player_active in self.__right_players:
            if player_active[0]:
                players += 1
        
        return players

    def count(self) -> int:
        players = self.count_left() + self.count_right()
        
        return players
