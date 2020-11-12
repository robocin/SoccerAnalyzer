import math

def find_last_who_kicked(dataframe, current_showtime):
    found_last_kickable = False
    while(True):
        for i in range(1,23):
            player_number = i if i<=11 else i-11
            player_side = "l" if i<=11 else "r"
            # found_last_kickable = is_kickable(dataframe, current_showtime, player_number, player_side)
            found_last_kickable = did_counting_kick_change(dataframe, current_showtime, player_number, player_side)
            if(found_last_kickable == True):
                return "player_{}{}".format(player_side,player_number)

        current_showtime -= 1

def did_counting_kick_change(dataframe, showtime, player_number, player_side):
    showtime -= 1

    is_player_1_l = player_number==1 and player_side=="l"
    player_counting_kick = 34 if is_player_1_l else 34 + (31*11 if player_side=="r" else 0 ) + (31*(player_number-1))  
    return True if dataframe.iloc[showtime, player_counting_kick] == (dataframe.iloc[showtime-1, player_counting_kick]+1) else False

