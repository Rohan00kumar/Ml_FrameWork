from abc import ABC, abstractmethod

class BaseAlgorithm(ABC):
    @abstractmethod
    def train(self, model, data):
        pass

    @abstractmethod
    def evaluate(self, model, data):
        pass
