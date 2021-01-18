def closest_player_side(t0,df):  # inefficient 
        
        i = t0
        
        BALL_X_COL = 10
        BALL_Y_COL = 11
        
        ball_x = df.iloc[i][BALL_X_COL]
        ball_y = df.iloc[i][BALL_Y_COL]

        l_di = 1000
        r_di = 1000
        prev_ldi = l_di + 1
        prev_rdi = r_di + 1

        for j in range(1,11):
            pl_x_row = "player_l{}_x".format(j)
            pl_y_row = "player_l{}_y".format(j)

            pr_x_row = "player_r{}_x".format(j)
            pr_y_row = "player_r{}_y".format(j)

            pr_x = df.iloc[i][pr_x_row]
            pr_y = df.iloc[i][pr_y_row]

            pl_x = df.iloc[i][pl_x_row]
            pl_y = df.iloc[i][pl_y_row]

            l_di = distance(ball_x,ball_y,pr_x,pr_y)
            r_di = distance(ball_x,ball_y,pl_x,pl_y)
            
            if l_di < r_di:
                return 'l'
            else:
                return 'r'


def game_ball_possession(t0,df): # inefficient
    start = t0
    cycles = 0
    closest = closest_player_side(t0,df)
    
    while(closest == 'l'):
        
        cycles += 1
        t0 += 1
        closest = closest_player_side(t0,df)
    
    print("from {} counted {} cycles\n".format(start,cycles))
    return cycles