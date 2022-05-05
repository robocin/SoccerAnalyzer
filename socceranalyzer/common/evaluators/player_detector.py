from socceranalyzer.common.basic.match import Match
from socceranalyzer.common.enums.sim2d import SIM2D
from socceranalyzer.common.enums.ssl import SSL 
from socceranalyzer.common.enums.vss import VSS

class PlayerDetector:
    def __init__(self, match: Match) -> None:
        self.__match: Match = match
        self.__category: SIM2D | SSL | VSS = match.category
        self.__left_players: list[bool] = [False for x in range(0, 11)]
        self.__right_players: list[bool] = [False for x in range(0, 11)] 

        if self.__match is None:
            print("No Match object was given, please provide one.")

    @property
    def left_players(self):
        return self.__left_players

    @property
    def right_players(self):
        return self.__right_players

    def count_left(self):
        players = 0
        for player_active in self.__left_players:
            if player_active:
                players += 1
        
        return players 

    def count_right(self):
        players = 0
        for player_active in self.__right_players:
            if player_active:
                players += 1
        
        return players

    def count(self):
        players = self.count_left() + self.count_right()
        
        return players
