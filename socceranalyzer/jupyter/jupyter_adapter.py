import matplotlib
import matplotlib.pyplot as plt

from socceranalyzer.common.chore.match_analyzer import MatchAnalyzer


class JupyterAdapter:
    def __init__(self, match_analyzer: MatchAnalyzer) -> None:
        self.__match_analyzer = match_analyzer
        self.__sim2d_figures: list = []
        self.__ssl_figures: list = []
        self.__vss_figures: list = []

        self._build_sim2d()
        self._build_ssl()
        self._build_vss()


    def _build_sim2d(self):
        pass

    def _build_ssl(self):
        pass

    def _build_vss(self):
        pass


    
    