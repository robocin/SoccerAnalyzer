from socceranalyzer.common.analysis.abstract_analysis import AbstractAnalysis
from socceranalyzer.common.basic.match import Match

class Playmodes(AbstractAnalysis):
    """
        Used to calculate how many unique playmodes happened in the match along with their counts.

        Attributes
        ----------
            private:
                playmode_dictionary : dict
                    a dictionary with playmodes as keys and how many times they appeared as values

            public through @properties:
                dataframe : pandas.Dataframe
                    match's log to be analyzed
                category : enum
                    match's category (2D, VSS or SSL)

        Methods
        -------
            private:
                _analyze() -> None
                    finds every playmode in the match and how many times they appeared

            public:
                results() -> (list[str], list[int])
                    returns which playmodes appeared and their counts, respectively
                describe() -> None
                    provides which playmodes appeared
    """
    def __init__(self, match : Match):
        super().__init__(match)
        self.__playmode_dictionary = {}

        self._analyze()

    @property
    def category(self):
        return self._category

    @property
    def dataframe(self):
        return self._dataframe

    def _analyze(self):
        """
            Finds every playmode in the match and how many times they appeared.
        """
        data = self.dataframe[str(self.category.PLAYMODE)].value_counts()

        playmodes = data.index.to_list()
        values = data.values.tolist()

        while playmodes:
            key = playmodes.pop(0)
            value = values.pop(0)

            self.__playmode_dictionary[key] = value

    def results(self):
        """
            Returns a tuple containing which playmodes appeared and their counts, respectively.
        """
        playmode = []
        counts = []

        for k, v in self.__playmode_dictionary.items():
            playmode.append(k)
            counts.append(v)

        return playmode, counts

    def describe(self):
        """
            Provides which playmodes appeared.
        """
        pms, foo = self.results()

        print(f'This game had {len(pms)} different playmodes which were:\n'
              f' {pms}')

    def serialize(self):
        return NotImplementedError
