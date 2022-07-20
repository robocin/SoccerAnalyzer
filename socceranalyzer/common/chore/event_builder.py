import pandas as pd

from socceranalyzer.common.events.corner_kick_event import CornerKickEvent
from socceranalyzer.common.events.foul_event import FoulEvent
from socceranalyzer.common.events.free_kick_event import FreeKickEvent
from socceranalyzer.common.events.goal_event import GoalEvent
from socceranalyzer.common.events.penalty_event import PenaltyEvent

from socceranalyzer.common.basic.match import Match

from socceranalyzer.common.geometric.point import Point
from socceranalyzer.common.geometric.rectangle import Rectangle
from socceranalyzer.common.basic.field import Field
from socceranalyzer.common.basic.team import Team 
from socceranalyzer.common.basic.ball import Ball
from socceranalyzer.agent2D.agent import Agent2D

from socceranalyzer.common.enums.vss import VSS
from socceranalyzer.common.enums.sim2d import SIM2D, Landmarks
from socceranalyzer.common.enums.ssl import SSL

class EventBuilder:
    def __init__(self, match: Match):
        self.__match =  match
        self.__df = match.dataframe
        self.__category = match.category
        """
            A class to instanciate the events that happened in a given match
        """

    def get_goal_events(self):
        """
        Create goal events using the dataframe and returns a list of GoalEvent's
        """
        goal_events = []
        
        goal_occurences_l = self.__df[self.__df[str(self.__category.PLAYMODE)] == str(self.__category.GOAL_SCORED_L)]
        goal_occurences_r = self.__df[self.__df[str(self.__category.PLAYMODE)] == str(self.__category.GOAL_SCORED_R)]
    
        goal_occurences_l = goal_occurences_l.drop_duplicates(subset=str(self.__category.GAME_TIME))
        goal_occurences_r = goal_occurences_r.drop_duplicates(subset=str(self.__category.GAME_TIME))

        for i, row in goal_occurences_l.iterrows():
            event = GoalEvent(self.__match,
                            (row[str(self.__category.GAME_TIME)], row[str(self.__category.GAME_TIME)]),
                            [], 
                            [],
                            self.__match.team_left)
            goal_events.append(event)
        for i, row in goal_occurences_r.iterrows():
            event = GoalEvent(self.__match, 
                            (row[str(self.__category.GAME_TIME)], row[str(self.__category.GAME_TIME)]),
                            [], 
                            [],
                            self.__match.team_right)
            goal_events.append(event)

        return goal_events
    
    def get_penalty_events(self):
        """
        Create penalty events using the dataframe and returns a list of PenaltyEvent's
        """
        penalty_events = []

        penalty_occurences_l = self.__df[self.__df[str(self.__category.PLAYMODE)] == str(self.__category.PENALTY_TO_LEFT)]
        penalty_occurences_r = self.__df[self.__df[str(self.__category.PLAYMODE)] == str(self.__category.PENALTY_TO_RIGHT)]
    
        penalty_occurences_l = penalty_occurences_l.drop_duplicates(subset=str(self.__category.GAME_TIME))
        penalty_occurences_r = penalty_occurences_r.drop_duplicates(subset=str(self.__category.GAME_TIME))

        for i, row in penalty_occurences_l.iterrows():
            event = PenaltyEvent(self.__match, 
                            (row[str(self.__category.GAME_TIME)], row[str(self.__category.GAME_TIME)]),
                            [], 
                            [],
                            self.__match.team_left)
            penalty_events.append(event)
        for i, row in penalty_occurences_r.iterrows():
            event = PenaltyEvent(self.__match, 
                            (row[str(self.__category.GAME_TIME)], row[str(self.__category.GAME_TIME)]),
                            [], 
                            [],
                            self.__match.team_right)
            penalty_events.append(event)

        return penalty_events

    def get_corner_kick_events(self):
        """
        Create goal events using the dataframe and returns a list of CornerKickEvent's
        """     
        corner_kick_events = []
        
        corner_kick_occurences_l = self.__df[self.__df[str(self.__category.PLAYMODE)] == str(self.__category.TEAM_LEFT_CORNER)]
        corner_kick_occurences_r = self.__df[self.__df[str(self.__category.PLAYMODE)] == str(self.__category.TEAM_RIGHT_CORNER)]

        corner_kick_occurences_l = corner_kick_occurences_l.drop_duplicates(subset=str(self.__category.GAME_TIME))
        corner_kick_occurences_r = corner_kick_occurences_r.drop_duplicates(subset=str(self.__category.GAME_TIME))


        corner_kick_occurences_l = corner_kick_occurences_l.reset_index()
        corner_kick_occurences_r = corner_kick_occurences_r.reset_index()
        if len(corner_kick_occurences_l) != 0:
            first_cycle = corner_kick_occurences_l[str(self.__category.GAME_TIME)][0]
            for i, row in corner_kick_occurences_l.iterrows():
                if i == 0:
                    continue
                previous_cycle = corner_kick_occurences_l.iloc[i-1][str(self.__category.GAME_TIME)]
                current_cycle = row[str(self.__category.GAME_TIME)]

                if previous_cycle != current_cycle - 1:
                    event = CornerKickEvent(self.__match,
                                            (first_cycle, previous_cycle),
                                            [],
                                            [],
                                            self.__match.team_left)
                    corner_kick_events.append(event)

                    first_cycle = current_cycle

            event = CornerKickEvent(self.__match,
                                    (first_cycle, current_cycle),
                                    [],
                                    [],
                                    self.__match.team_left)
            corner_kick_events.append(event)

        if len(corner_kick_occurences_r) != 0:
            first_cycle = corner_kick_occurences_r[str(self.__category.GAME_TIME)][0]
            for i, row in corner_kick_occurences_r.iterrows():
                if i == 0:
                    continue
                previous_cycle = corner_kick_occurences_r.iloc[i-1][str(self.__category.GAME_TIME)]
                current_cycle = row[str(self.__category.GAME_TIME)]

                if previous_cycle != current_cycle - 1:
                    event = CornerKickEvent(self.__match,
                                            (first_cycle, previous_cycle),
                                            [],
                                            [],
                                            self.__match.team_right)
                    corner_kick_events.append(event)

                    first_cycle = current_cycle
            event = CornerKickEvent(self.__match,
                                    (first_cycle, current_cycle),
                                    [],
                                    [],
                                    self.__match.team_right)
            corner_kick_events.append(event)

        return corner_kick_events

    def get_foul_events(self):
        """
        Create foul events using the dataframe and returns a list of FoulEvent's
        """
        foul_events = []
        
        foul_occurences_l = self.__df[self.__df[str(self.__category.PLAYMODE)] == str(self.__category.FAULT_COMMITED_L)]
        foul_occurences_r = self.__df[self.__df[str(self.__category.PLAYMODE)] == str(self.__category.FAULT_COMMITED_R)]
    
        foul_occurences_l = foul_occurences_l.drop_duplicates(subset=str(self.__category.GAME_TIME))
        foul_occurences_r = foul_occurences_r.drop_duplicates(subset=str(self.__category.GAME_TIME))

        for i, row in foul_occurences_l.iterrows():
            event = FoulEvent(self.__match,
                            (row[str(self.__category.GAME_TIME)], row[str(self.__category.GAME_TIME)]),
                            [], 
                            [],
                            self.__match.team_left)
            foul_events.append(event)
        for i, row in foul_occurences_r.iterrows():
            event = FoulEvent(self.__match, 
                            (row[str(self.__category.GAME_TIME)], row[str(self.__category.GAME_TIME)]),
                            [], 
                            [],
                            self.__match.team_right)
            foul_events.append(event)

        return foul_events
    
    def get_free_kick_events(self):
        """
        Create free kick events using the dataframe and returns a list of FreeKickEvent's
        """

        free_kick_events = []
        
        free_kick_occurences_l = self.__df[self.__df[str(self.__category.PLAYMODE)] == str(self.__category.FK_LEFT)]
        free_kick_occurences_r = self.__df[self.__df[str(self.__category.PLAYMODE)] == str(self.__category.FK_RIGHT)]

        free_kick_occurences_l = free_kick_occurences_l.drop_duplicates(subset=str(self.__category.GAME_TIME))
        free_kick_occurences_r = free_kick_occurences_r.drop_duplicates(subset=str(self.__category.GAME_TIME))


        free_kick_occurences_l = free_kick_occurences_l.reset_index()
        free_kick_occurences_r = free_kick_occurences_r.reset_index()
        if len(free_kick_occurences_l) != 0:
            first_cycle = free_kick_occurences_l[str(self.__category.GAME_TIME)][0]
            for i, row in free_kick_occurences_l.iterrows():
                if i == 0:
                    continue
                previous_cycle = free_kick_occurences_l.iloc[i-1][str(self.__category.GAME_TIME)]
                current_cycle = row[str(self.__category.GAME_TIME)]

                if previous_cycle != current_cycle - 1:
                    event = FreeKickEvent(self.__match,
                                            (first_cycle, previous_cycle),
                                            [],
                                            [],
                                            self.__match.team_left)
                    free_kick_events.append(event)

                    first_cycle = current_cycle

            event = FreeKickEvent(self.__match,
                                    (first_cycle, current_cycle),
                                    [],
                                    [],
                                    self.__match.team_left)
            free_kick_events.append(event)

        if len(free_kick_occurences_r) != 0:
            first_cycle = free_kick_occurences_r[str(self.__category.GAME_TIME)][0]
            for i, row in free_kick_occurences_r.iterrows():
                if i == 0:
                    continue
                previous_cycle = free_kick_occurences_r.iloc[i-1][str(self.__category.GAME_TIME)]
                current_cycle = row[str(self.__category.GAME_TIME)]

                if previous_cycle != current_cycle - 1:
                    event = FreeKickEvent(self.__match,
                                            (first_cycle, previous_cycle),
                                            [],
                                            [],
                                            self.__match.team_right)
                    free_kick_events.append(event)

                    first_cycle = current_cycle
            event = FreeKickEvent(self.__match,
                                    (first_cycle, current_cycle),
                                    [],
                                    [],
                                    self.__match.team_right)
            free_kick_events.append(event)

        return free_kick_events


