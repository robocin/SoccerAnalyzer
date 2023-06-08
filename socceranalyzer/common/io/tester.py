import os
import glob
import time
from datetime import datetime

from mdutils.mdutils import MdUtils
from socceranalyzer.utils.logger import Logger

class TeamData:
    def __init__(self) -> None:
        self.data = {
            "name":"",
            "score_count"   :0,
            "score_adv"     :0,
            "victory"       :0,
            "defeat"        :0,
            "draw"          :0,
            "penalti_score" :0 
        }

class Tester:
    team_left = TeamData()
    team_right = TeamData()
    total_games = 0
    
    @staticmethod
    def statistics_from_filenames(rcg_files: list[str]):
        time_start = time.time()
        __class__._get_team_names(rcg_files)
        __class__._get_goal_balance(rcg_files)
        time_end = time.time()
        
    @staticmethod 
    def _get_team_names(rcg_files: list[str]):
        for logname in rcg_files:
            if __class__.__is_valid_file(logname):
                if not __class__.__had_penalti_shotout(logname):
                    team_right = logname.split('-')[3].split('_')[0]
                    team_left = logname.split('-')[1].split('_')[0]

                    team_left_name = team_left
                    team_right_name = team_right

                    __class__.team_left.data["name"] = team_left_name
                    __class__.team_right.data["name"] = team_right_name 
                    break

    @staticmethod
    def __is_valid_file(logname: str):
        if("null" not in logname):
            return True
        
    @staticmethod
    def __had_penalti_shotout(logname: str):
        team_left = logname.split('-')[3].split('.')[0]   
        return False if team_left.count('_') == 1 else True
    
    @staticmethod
    def _get_goal_balance(rcg_files: list[str]):
        for logname in rcg_files:
            if __class__.__is_valid_file(logname):
                left_team_with_score = logname.split('-')[1]
                right_team_with_score = logname.split('-')[3].split('.')[0]

                __class__._update_team_scores(logname, left_team_with_score, right_team_with_score)

    @staticmethod
    def _get_team_dict(team_name):
        if(__class__.team_left.data["name"] == team_name):
            return __class__.team_left
        else:
            return __class__.team_right

    @staticmethod
    def _update_team_scores(logname, left_team, right_team):
        team_left_splitted = left_team.split('_')
        team_right_splitted = right_team.split('_')

        team_left_name = team_left_splitted[0]
        team_right_name = team_right_splitted[0]

        team_left_score = team_left_splitted[1]
        team_right_score = team_right_splitted[1]

        if(__class__.__had_penalti_shotout(logname)):
            team_left_penalti_score = team_left_splitted[2]
            team_right_penalti_score = team_right_splitted[2]
        else:
            team_left_penalti_score = 0
            team_right_penalti_score = 0
        
        __class__._get_team_dict(team_left_name).data["score_count"] += int(team_left_score)
        __class__._get_team_dict(team_left_name).data["score_adv"] += int(team_right_score)
        __class__._get_team_dict(team_left_name).data["penalti_score"] += int(team_left_penalti_score)

        __class__._get_team_dict(team_right_name).data["score_count"] += int(team_right_score)
        __class__._get_team_dict(team_right_name).data["score_adv"] += int(team_left_score)
        __class__._get_team_dict(team_right_name).data["penalti_score"] += int(team_right_penalti_score)

        if int(team_left_score) > int(team_right_score):
            __class__._get_team_dict(team_left_name).data["victory"] += 1
            __class__._get_team_dict(team_right_name).data["defeat"] += 1
        elif int(team_left_score) < int(team_right_score):
            __class__._get_team_dict(team_left_name).data["defeat"] += 1
            __class__._get_team_dict(team_right_name).data["victory"] += 1
        else:
            __class__._get_team_dict(team_left_name).data["draw"] += 1
            __class__._get_team_dict(team_right_name).data["draw"] += 1

    @staticmethod
    def log(rcg_files: list[str], debug=False):
            __class__.total_games = len(rcg_files)
            if debug:
                print("\n")
                print(f'==================================== Debug ===================================')
                print(__class__.team_left.data)
                print(__class__.team_right.data)
                print("\n")

            print(f'================== Detail ==================')
            print(f'|  {__class__.team_left.data["name"]} victories: {(__class__.team_left.data["victory"]/__class__.total_games)*100}%')
            print(f'|  {__class__.team_left.data["name"]} defeats: {(__class__.team_left.data["defeat"]/__class__.total_games)*100}%')
            print(f'|  Draws: {(__class__.team_left.data["draw"]/__class__.total_games)*100}%')
            print(f'|  Goals scored: {__class__.team_left.data["score_count"]}')
            print(f'|  Goals taken: {__class__.team_left.data["score_adv"]}')
            print(f'|  Goal balance: {__class__.team_left.data["score_count"] - __class__.team_left.data["score_adv"]}')
            print(f'|  Score/taken ratio: {(__class__.team_left.data["score_count"] / __class__.team_left.data["score_adv"])}')
            print(f'|  Score per game: {(__class__.team_left.data["score_count"]/__class__.total_games)}')

            print(f'================== Overall ==================')
            print(f'|  {__class__.team_left.data["name"]} victories: {(__class__.team_left.data["victory"]/__class__.total_games)*100}%')
            print(f'|  {__class__.team_right.data["name"]} victories: {(__class__.team_right.data["victory"]/__class__.total_games)*100}%')
            print(f'|  Draws: {(__class__.team_left.data["draw"]/__class__.total_games)*100}%')

    @staticmethod
    def save_to_file(output_file_name: str):
        try:  
            with open(output_file_name, "a") as file:
                title = "{} x {}, {}\n".format(
                    __class__.team_left.data["name"], 
                    __class__.team_right.data["name"], 
                    datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
                
                file.write(title)
                file.write(f'{__class__.team_left.data["name"]} victories: {(__class__.team_left.data["victory"]/__class__.total_games)*100}%\n')
                file.write(f'{__class__.team_left.data["name"]} defeats: {(__class__.team_left.data["defeat"]/__class__.total_games)*100}%\n')
                file.write(f'Draws: {(__class__.team_left.data["draw"]/__class__.total_games)*100}%\n')
                file.write(f'Goals scored: {__class__.team_left.data["score_count"]}\n')
                file.write(f'Goals taken: {__class__.team_left.data["score_adv"]}\n')
                file.write(f'Goal balance: {__class__.team_left.data["score_count"] - __class__.team_left.data["score_adv"]}\n')
                file.write(f'Score/taken ratio: {(__class__.team_left.data["score_count"] / __class__.team_left.data["score_adv"])}\n')
                file.write(f'Score per game: {(__class__.team_left.data["score_count"]/__class__.total_games)}\n')
                file.write(f'=======================================================================================\n')                  
                Logger.success(f"Saved to {output_file_name}")
        except Exception as err:
            Logger.error(f"Could not write to file: {err}")