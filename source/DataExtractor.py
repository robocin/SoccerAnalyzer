from Classes import GameData, Team, Player
import pandas as pd

def data_extractor(file_path):
    # initializes the game_data class
    game_data = GameData.GameData()
    # saves the pandas.dataFrame object in it
    game_data.set_dataframe(read_file(file_path))

    dataframe = game_data.get_dataframe()

    # extract players data
    extract_players(game_data, dataframe)

    # extract teams data
    extract_teams(game_data, dataframe)



    return game_data

def extract_players(game_data, dataframe):
    # instaciates all players 
    all_players = []
    for i in range(0,22):
        all_players.append(Player.Player("l" if i<11 else "r",i if i<11 else i-11))
    
    game_data.set_players(all_players)

def extract_teams(game_data, dataframe): #TODO: split this into shorter, more specific functions!
    # instaciates the teams and saves them in the game_data object
    game_data.set_teams([Team.Team("l"),Team.Team("r")])

    # get the teams names
    team_left_name = dataframe.iloc[0].team_name_l
    team_right_name =dataframe.iloc[0].team_name_r
    game_data.get_team(0).set_name(team_left_name)
    game_data.get_team(1).set_name(team_right_name)

    # get the teams sides
    team_left_side = "l"
    team_right_side = "r"
    game_data.get_team(0).set_side(team_left_side)
    game_data.get_team(1).set_side(team_right_side)

    # get the players of each team

    # get stamina

    # TODO: temporary. get number of goals scored by the team
    team_l_score = dataframe['team_score_l'].max()
    team_r_score = dataframe['team_score_r'].max()
    game_data.get_team(0).set_number_of_goals_scored(team_l_score)
    game_data.get_team(1).set_number_of_goals_scored(team_r_score)

    # TODO: temporary. get number of fouls commited by the team
    team_l_fouls = 0
    team_r_fouls = 0
    for i in range(len(dataframe)):
        if(dataframe.iloc[i,1] == "foul_charge_l" and dataframe.iloc[i-1,1] != "foul_charge_l"):
            team_l_fouls += 1
        elif(dataframe.iloc[i,1] == "foul_charge_r" and dataframe.iloc[i-1,1] != "foul_charge_r"):
            team_r_fouls += 1
    game_data.get_team(0).set_number_of_fouls_commited(team_l_fouls)
    game_data.get_team(1).set_number_of_fouls_commited(team_r_fouls)


    # TODO: get the goals scored by the players for each team

    # TODO: get the faults commited by the players for each team



def read_file(file_path):
    dataframe = pd.read_csv(file_path)
    return dataframe
