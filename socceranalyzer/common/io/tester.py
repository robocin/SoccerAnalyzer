import os
import glob
import time

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
    
    @staticmethod
    def statistics_from_filenames(rcg_files: list[str]):
        __class__._get_team_names(rcg_files)
        
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