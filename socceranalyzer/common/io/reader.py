import json
from socceranalyzer.utils.logger import Logger

class Reader:
    def __init__(self, games=None, games_count=0):
        self._games = games
        self._games_count = games_count

    @staticmethod
    def read(self, path):
        raise NotImplementedError
    
    @staticmethod
    def how_many(self):
        return self._games_count
        
class JsonReader:
    @staticmethod
    def read(path:str):
        file = open(path)
        file_data = json.load(file)
        
        if JsonReader.isValid(file_data):
            for key, value in file_data.items():
                print(key, value)
            Logger.info("Json parsed.")

        file.close()
        

    @staticmethod
    def isValid(file_data):
        for key, value in file_data.items():
            if key == "" or value not in [True, False]:
                Logger.error(f"Json invalid argument: {key, value}")
                return False
            
        return True