def kick(cycle, team, df):
    for player_num in range(1,12):
        if cycle != 0:
            if df[f"player_{team}{player_num}_counting_kick"][cycle] > df[f'player_{team}{player_num}_counting_kick'][cycle-1]:
                return True
    return False