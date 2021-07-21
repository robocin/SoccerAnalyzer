from abc import ABCMeta, abstractmethod

class AbstractFactory(metaclass=ABCMeta):

    @abstractmethod
    def _run_analysis(self):
        pass

    @abstractmethod
    def collect_analysis(self):
        pass
