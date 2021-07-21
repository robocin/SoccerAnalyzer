from abc import ABCMeta, abstractmethod

class AbstractAnalysis(metaclass=ABCMeta):

    @abstractmethod
    def _analyze(self):
        pass

    @abstractmethod
    def results(self):
        pass