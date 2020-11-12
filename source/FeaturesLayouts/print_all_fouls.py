from utility_functions import find_unique_event_ocurrences, get_closer_to_ball, get_distance_between_two_points
from Classes import Position

def print_all_fouls(MainWindow, game_data):
    fouls_array = []

    fouls_showtime = find_unique_event_ocurrences.find_unique_event_ocurrences(game_data.get_dataframe(), "foul")
    for i in range(0,23):
        fouls_array.append(get_closer_to_ball.get_closer_to_ball(game_data.get_dataframe(), fouls_showtime[i], 2))
    
    # for n, get closer to ball (excluding the ones already seen)
    dataframe = game_data.get_dataframe()

    # for i in range(0, 23):
    #     print(fouls_array[i])
