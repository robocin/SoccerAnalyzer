from SoccerAnalyzer.socceranalyzer.common.enums.sim2d import SIM2D
from SoccerAnalyzer.socceranalyzer.common.enums.ssl import SSL
from SoccerAnalyzer.socceranalyzer.common.enums.vss import VSS
from SoccerAnalyzer.socceranalyzer.common.collections.collections import StringListPositions
from SoccerAnalyzer.socceranalyzer.common.collections.collections import StringListItem

class Mediator:
    @staticmethod
    def players_left_position(category, gkeeper=True):

        slp = StringListPositions()

        if category is SIM2D:
            if gkeeper:
                for i in range(1, 12):
                    slp.items.append(StringListItem(f'player_l{i}_x', f'player_l{i}_y'))
            else:
                for i in range(2, 12):
                    slp.items.append(StringListItem(f'player_l{i}_x', f'player_l{i}_y'))

            return slp

        elif category is VSS:
            raise NotImplementedError

        elif category is SSL:
            raise NotImplementedError


    @staticmethod
    def players_right_position(category, gkeeper=True):

        slp = StringListPositions()

        if category is SIM2D:
            if gkeeper:
                for i in range(1, 12):
                    slp.items.append(StringListItem(f'player_r{i}_x', f'player_r{i}_y'))
            else:
                for i in range(2, 12):
                    slp.items.append(StringListItem(f'player_r{i}_x', f'player_r{i}_y'))

            return slp
        elif category is Category.VSS:
            raise NotImplementedError

        elif category is Category.SSL:
            raise NotImplementedError
