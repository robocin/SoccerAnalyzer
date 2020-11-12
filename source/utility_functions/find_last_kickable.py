import math

def find_last_kickable(dataframe, current_showtime):
    found_last_kickable = False
    while(True):
        for i in range(1,23):
            player_number = i if i<=11 else i-11
            player_side = "l" if i<=11 else "r"
            found_last_kickable = is_kickable(dataframe, current_showtime, player_number, player_side)
            if(found_last_kickable == True):
                return "player_{}{}".format(player_side,player_number)

        current_showtime -= 1

def is_kickable(dataframe, showtime, player_number, player_side):
    # Find x and y position for ball and player
    showtime -= 1

    print(showtime)
    ball_x = dataframe.iloc[showtime,10]
    ball_y = dataframe.iloc[showtime,11]

    is_player_1_l = player_number==1 and player_side=="l"
    player_x_column = 18 if is_player_1_l else 18 + (31*11 if player_side=="r" else 0 ) + (31*(player_number-1))  
    player_y_column = 19 if is_player_1_l else 19 + (31*11 if player_side=="r" else 0 ) + (31*(player_number-1))  
    player_x = dataframe.iloc[showtime, (player_x_column)]
    player_y = dataframe.iloc[showtime, (player_y_column)]

    # compute distance and return value
    return compute_is_kickable(player_x, player_y, ball_x, ball_y)


def compute_is_kickable(player_x, player_y, ball_x, ball_y):
    # Distance between two points
    distance  = math.sqrt( ((abs(ball_x-player_x))**2) + ((abs(ball_y-player_y))**2))
    if(distance<=0.25): #<=0.30 n acha, <=0.31 fica preso no player_l_11
        return True
    else:
        return False
