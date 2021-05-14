import pandas as pd

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
        