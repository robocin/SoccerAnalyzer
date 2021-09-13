from SoccerAnalyzer.socceranalyzer.common.abstract.abstract_analysis import AbstractAnalysis\


class Playmodes(AbstractAnalysis):
    def __init__(self, dataframe):
        self.__df = dataframe
        self.__playmode_dictionary = {}

        self._analyze()

    def _analyze(self):
        data = self.__df["playmode"].value_counts()

        playmodes = data.index.to_list()
        values = data.values.tolist()

        while playmodes:
            key = playmodes.pop(0)
            value = values.pop(0)


            self.__playmode_dictionary[key] = value

    def results(self):
        for key, value in self.__playmode_dictionary.items():
            return (key, value)
