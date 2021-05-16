import pandas as pd

def kicks_radial(): # inefficient
    print('hi')
"""    positions = []
    attempts = [0,0,0]
    for i in range(1, Reader.how_many()): # games
        for j in range(len(games[i])): # cycle
            for k in range(1,12): # players
                if games[i].iloc[j]['player_l{}_counting_kick'.format(k)] != games[i].iloc[j-1]['player_l{}_counting_kick'.format(k)]:
                    spot = Point(games[i].iloc[j]['ball_x'],games[i].iloc[j]['ball_y'])
                    positions.append(spot)
                    if area_1.is_inside(spot):
                        attempts[0] += 1
                    elif area_2.is_inside(spot):
                        attempts[1] += 1
                    elif area_3.is_inside(spot):
                        attempts[2] += 1
    
    return attempts"""