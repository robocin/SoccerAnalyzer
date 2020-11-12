from utility_functions import find_last_who_kicked, find_unique_event_ocurrences


def print_all_goals(MainWindow, game_data):
    goals = find_unique_event_ocurrences.find_unique_event_ocurrences(game_data.get_dataframe(), "goal")
    i=0
    for goal in goals:
        i += 1
        player = find_last_who_kicked.find_last_who_kicked(game_data.get_dataframe(), goal)
        print("Goal {} scored by {}".format(i,player))


