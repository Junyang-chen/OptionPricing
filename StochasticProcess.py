
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
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
    def __init__(self, timetoexp=1, mu=0, vol=1):
        self._numofPoints = int(timetoexp*252)
        self.timetoexp = timetoexp
        self.mu = mu
        self.vol = vol
        self.dt = timetoexp/self._numofPoints

    @abstractclassmethod
    def generatePath(self):
        pass

    @abstractclassmethod
    def generatePaths(self, numofPaths):
        pass


class GeneralizedWienerProcessGenerator(StochasticProcessGenerator):

    def __init__(self, timetoexp=1, mu=0, vol=1):
        super().__init__(timetoexp, mu, vol)

    def generatePath(self):
        initialseries = self.vol*np.random.normal(0, 1, self._numofPoints)*np.sqrt(self.dt) + self.dt * self.mu
        initialseries = np.cumsum(initialseries)
        result = pd.DataFrame(initialseries)
        result.index = result.index/252
        return result

    def generatePaths(self, numofPaths):
        initialseries = self.vol*np.random.randn(numofPaths, self._numofPoints)*np.sqrt(self.dt) + self.dt * self.mu
        initialseries = np.transpose(initialseries)
        initialseries = np.cumsum(initialseries, axis=0)
        result = pd.DataFrame(initialseries)
        result.index = result.index / 252
        return result

class GeometricBrownianMotionGenerator(StochasticProcessGenerator):

    def __init__(self, timetoexp=1, mu=0, vol=1):
        super().__init__(timetoexp, mu, vol)

    def generatePath(self):
        initialseries = self.vol*np.random.normal(0, 1, self._numofPoints)*np.sqrt(self.dt)\
                        + self.dt * (self.mu - self.vol**2/2)
        initialseries = np.cumsum(initialseries)
        expfunc = lambda t: np.exp(t)
        vfunc = np.vectorize(expfunc)
        initialseries = vfunc(initialseries)
        result = pd.DataFrame(initialseries)
        result.index = result.index/252
        return result

    def generatePaths(self, numofPaths):
        initialseries = self.vol*np.random.randn(numofPaths, self._numofPoints)*np.sqrt(self.dt)\
                        + self.dt * (self.mu - self.vol**2/2)
        initialseries = np.transpose(initialseries)
        initialseries = np.cumsum(initialseries, axis=0)
        expfunc = lambda t: np.exp(t)
        vfunc = np.vectorize(expfunc)
        initialseries = vfunc(initialseries)
        result = pd.DataFrame(initialseries)
        result.index = result.index / 252
        return result

if __name__ == '__main__':
    brownianmotion = GeneralizedWienerProcessGenerator(1, 0.3, 1.5)
    onepath = brownianmotion.generatePath()
    fig, ax = plt.subplots(2,2)
    onepath.plot(ax=ax[0,0], title='GeneralizedWienerProcess')
    multiplepaths = brownianmotion.generatePaths(10)
    multiplepaths.plot(ax=ax[0,1], title='GeneralizedWienerProcess multiple')

    geometricbrownianmotion = GeometricBrownianMotionGenerator(1, 0.3, 0.1)
    onepath = geometricbrownianmotion.generatePath()
    onepath.plot(ax=ax[1, 0], title='geometricbrownianmotion')
    multiplepaths = geometricbrownianmotion.generatePaths(10)
    multiplepaths.plot(ax=ax[1,1], title='geometricbrownianmotion multiple')
    plt.show()