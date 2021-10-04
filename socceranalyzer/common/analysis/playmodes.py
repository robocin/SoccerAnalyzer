from SoccerAnalyzer.socceranalyzer.common.abstract.abstract_analysis import AbstractAnalysis


class Playmodes(AbstractAnalysis):
    def __init__(self, dataframe, category):
        self.__category = category
        self.__df = dataframe
        self.__playmode_dictionary = {}

        self._analyze()

    @property
    def category(self):
        return self.__category

    def values(self):
        playmode = []
        counts = []

        for k, v in self.results().items():
            playmode.append(k)
            counts.append(v)

        return playmode, counts

    def _analyze(self):
        data = self.__df[str(self.category.PLAYMODE)].value_counts()

        playmodes = data.index.to_list()
        values = data.values.tolist()

        while playmodes:
            key = playmodes.pop(0)
            value = values.pop(0)

            self.__playmode_dictionary[key] = value

    def results(self):
        return self.__playmode_dictionary
