from socceranalyzer.common.enums.sim2d import SIM2D
from socceranalyzer.common.enums.ssl import SSL
from socceranalyzer.common.enums.vss import VSS
from socceranalyzer.common.collections.collections import StringListPositions
from socceranalyzer.common.collections.collections import StringListItem

class Mediator:
    """
        Mediator is a class context dependent that provides values
        based on the parameters (context) given to it. This class
        provides attributes or lists of attributes for specific SIM2D, 
        SSL or VSS categories.

        Static Methods
        --------------
            players_right/left_position: StringListPositions
                A list of strings containing the name of player position attributes
                in SIM2D, SSL or VSS.
            players_right/left_stamina_attr: StringListPositions
                A list of strings containing the name of players stamina attributes in 
                SIM2D.
    """
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

        # For SSL this is the RoboCIn team
        elif category is SSL:
            if gkeeper:
                for i in range(0, 6):
                    slp.items.append(StringListItem(f'ally_{i}_position_x', f'ally_{i}_position_y'))
            else:
                for i in range(1, 6):
                    slp.items.append(StringListItem(f'ally_{i}_position_x', f'ally_{i}_position_y'))

            return slp

        elif category is VSS:
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
        
        # For SSL this is the enemy team
        elif category is SSL:
            if gkeeper:
                for i in range(0, 6):
                    slp.items.append(StringListItem(f'enemy_{i}_position_x', f'enemy_{i}_position_y'))
            else:
                for i in range(1, 6):
                    slp.items.append(StringListItem(f'enemy_{i}_position_x', f'enemy_{i}_position_y'))

            return slp

        elif category is VSS:
            raise NotImplementedError

    @staticmethod
    def ball_position(category):

        slp = StringListPositions()

        if category is SIM2D:
            raise NotImplementedError
            
        
        # For SSL this is the enemy team
        elif category is SSL:
            slp.items.append(StringListItem(f'ball_position_x', f'ball_position_y'))

            return slp

        elif category is VSS:
            raise NotImplementedError


    @staticmethod
    def players_left_stamina_attr(category):
        string_list = []
        if category is SIM2D:
            for i in range(1, 12):
                string_list.append(f'player_l{i}_attribute_stamina')
        elif category is VSS:
            raise NotImplementedError

        elif category is SSL:
            raise NotImplementedError

        return string_list

    @staticmethod
    def players_right_stamina_attr(category):
        string_list = []
        if category is SIM2D:
            for i in range(1, 12):
                string_list.append(f'player_r{i}_attribute_stamina')
        elif category is VSS:
            raise NotImplementedError

        elif category is SSL:
            raise NotImplementedError

        return string_list