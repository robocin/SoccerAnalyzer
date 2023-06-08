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
    @staticmethod
    def statistics_from_filenames(rcg_files: list[str]):
        pass