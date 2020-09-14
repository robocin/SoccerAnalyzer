from typing import NamedTuple
import pandas as pd

class EntityPositionData(NamedTuple):
    '''Data about a specific moving entity in a specific point in time and space.'''
    timestamp: int
    x: float # entity's x position 
    y: float  # entity's y position 
    vx: float # entity's x velocity
    vy: float # entity's y velocity

class BallData(NamedTuple):
    position: list # list of EntityPositionData

class PlayerData(NamedTuple):
    position: list # list of EntityPositionData

class TeamData(NamedTuple):
    name: str # name of the team
    side: str # side of the team, either "l" for left or "r" for right
    score: list # score (number of favorable goals made)
    pen_score: list # penalties scored
    pen_miss: list # penalties missed
    players: list # list with all players

class EventData(NamedTuple):
    timestamp: list # list of int 
    x: list # list of float / None if there's no important x  
    y: list # lit of float / None if there's no important x  
    category: list # type of event: "goal","foul","kick_off" [type is a reserved word]
    owner: list # player responsible for the occurrance of the event

class GameData(NamedTuple):
    dataframe: list # list containing only the dataframe (TODO: is it possible to use directly the dataframe type here?) 
    event: list # list of specific subclasses of EventData or EventData
    ball: list # list of BallData
    team_1: TeamData #  
    team_1: TeamData # 