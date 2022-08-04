from abc import ABCMeta, abstractmethod

class AbstractAnalysis(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self, match):
        self._dataframe = match.dataframe
        self._category = match.category
        self._match = match

    @property
    @abstractmethod
    def category(self):
        return self.__category

    @abstractmethod
    def _analyze(self):
        pass

    @abstractmethod
    def describe(self):
        pass

    @abstractmethod
    def results(self):
        pass

    @abstractmethod
    def serialize(self):
        pass