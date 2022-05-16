def kick(cycle, team, df, player_who_kicked=False):
    for player_num in range(1,12):
        if cycle != 0:
            if df[f"player_{team}{player_num}_counting_kick"][cycle] > df[f'player_{team}{player_num}_counting_kick'][cycle-1]:
                    if player_who_kicked == True:
                        return True, player_num
                    else:
                        return True
    if player_who_kicked == True:
        return False, -1
    else:
        return False