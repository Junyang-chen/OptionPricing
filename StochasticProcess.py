
import numpy as np
import pandas as pd
from abc import ABCMeta, abstractclassmethod

"""
Abstract class for Stochastic Process Generator,
Other generator should derive from this, each generator will
have methods of generating one path and multiple paths,
they are designed to return pandas DataFrames
"""


class StochasticProcessGenerator(metaclass=ABCMeta):    
    
    _numofPoints = None

    @abstractclassmethod
    def __init__(self):
        pass

    @abstractclassmethod
    def generatePath(self):
        pass

    @abstractclassmethod
    def generatePaths(self, numofPaths):
        pass


class BrownianMotionGenerator(StochasticProcessGenerator):

    def __init__(self, numofPoints=0):
        self._numofPoints = numofPoints

    def generatePath(self):
        initialseries = np.random.normal(0, 1, self._numofPoints)
        initialseries = np.cumsum(initialseries)
        result = pd.DataFrame(initialseries)
        # result.index = np.arange(1, len(result) + 1)
        return result

    def generatePaths(self, numofPaths):
        initialseries = np.random.randn(numofPaths, self._numofPoints)
        initialseries = np.cumsum(initialseries)
        result = pd.DataFrame(np.random.randn(numofPaths, self._numofPoints))
        # result.index = np.arange(1, len(result) + 1)
        return result