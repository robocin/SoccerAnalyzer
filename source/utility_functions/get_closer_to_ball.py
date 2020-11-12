
from Classes import Position
from utility_functions import get_distance_between_two_points

def get_closer_to_ball(dataframe, showtime, n): # n = number of players you want to get (return array = [1st most closer, 2nd most closer, 3rd mos closer... to n )
    # get ball position
    ball_position = Position.Position(dataframe.iloc[showtime-1, 10], dataframe.iloc[showtime-1, 11])

    # get position of all players in a array
    players_position = []
    for i in range(0,23):
        player_number = i if i<=11 else i-11
        player_side = "l" if i<=11 else "r"
            # this code below is recorrent, it can be improved (ex: find_last_kickable)
        is_player_1_l = True if (player_number==0 and player_side=="l") else False
        player_x_column = 18 if is_player_1_l else 18 + (31*11 if player_side=="r" else 0 ) + (31*(player_number-1))  
        player_y_column = 19 if is_player_1_l else 19 + (31*11 if player_side=="r" else 0 ) + (31*(player_number-1))  
        player_x = dataframe.iloc[showtime-1, (player_x_column)]
        player_y = dataframe.iloc[showtime-1, (player_y_column)]
        players_position.append(Position.Position(player_x, player_y))

    # make an array with the distances of the players to the ball
    distances = []
    for i in range(0,23):
        distances.append(get_distance_between_two_points.get_distance_between_two_points(players_position[i].get_x(), players_position[i].get_y(), ball_position.get_x(), ball_position.get_y()))

    # for n times, determine the n player whom where closer to the ball when the foul happended 
    return_array = []
    for i in range(n):
        return_array.append(min(distances))
        distances.pop(0)
        
    print(return_array[0])
    return return_array