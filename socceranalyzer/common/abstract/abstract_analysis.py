from abc import ABCMeta, abstractmethod

class AbstractAnalysis(metaclass=ABCMeta):

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