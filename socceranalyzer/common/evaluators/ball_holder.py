from SoccerAnalyzer.socceranalyzer.common.geometric.point import Point
from SoccerAnalyzer.socceranalyzer.common.geometric.circle import Circle


def ball_holder(cycle, df):
    possible_l_players = []
    possible_r_players = []

    ball_x = df.loc[cycle, "ball_x"]
    ball_y = df.loc[cycle, "ball_y"]
    ball_position = Point(ball_x, ball_y)

    ball_radius = Circle(2.5, ball_position) # here to define ball area radius

    for i in range(1, 12):
        player_left_x = df.loc[cycle, "player_l{}_x".format(i)]
        player_left_y = df.loc[cycle, "player_l{}_y".format(i)]

        player_right_x = df.loc[cycle, "player_r{}_x".format(i)]
        player_right_y = df.loc[cycle, "player_r{}_y".format(i)]

        player_l_location = Point(player_left_x, player_left_y)
        player_r_location = Point(player_right_x, player_right_y)

        if ball_radius.is_inside(player_l_location):
            possible_l_players.append(i)
        else:
            possible_l_players.append(None)

        if ball_radius.is_inside(player_r_location):
            possible_r_players.append(i)
        else:
            possible_r_players.append(None)

    return (possible_r_players, possible_l_players)

