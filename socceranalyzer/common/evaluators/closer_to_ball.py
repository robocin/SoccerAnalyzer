from SoccerAnalyzer.socceranalyzer.common.geometric.point import Point
from SoccerAnalyzer.socceranalyzer.common.operations.measures import distance


def closer_to_ball(cycle, df):
    cycle = cycle

    ball_x = df.loc[cycle, "ball_x"]
    ball_y = df.loc[cycle, "ball_y"]

    ball_position = Point(ball_x, ball_y)

    closest_right = 1000
    closest_left = 1000

    for i in range(1, 12):
        player_left_x = df.loc[cycle, "player_l{}_x".format(i)]
        player_left_y = df.loc[cycle, "player_l{}_y".format(i)]
        player_left_position = Point(player_left_x, player_left_y)

        player_left_distance = distance(player_left_position, ball_position)

        if player_left_distance <= closest_left:
            closest_left = player_left_distance

        player_right_x = df.loc[cycle, "player_r{}_x".format(i)]
        player_right_y = df.loc[cycle, "player_r{}_y".format(i)]
        player_right_position = Point(player_right_x, player_right_y)

        player_right_distance = distance(player_right_position, ball_position)

        if player_right_distance <= closest_right:
            closest_right = player_right_distance

    if closest_left < closest_right:
        return "left"
    else:
        return "right"
