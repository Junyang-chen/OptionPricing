from scipy.stats import norm
from abc import ABCMeta, abstractclassmethod
import numpy as np

class OptionPricer(metaclass=ABCMeta):
    """
    Abstract class interface for an OptionPricer

    Derived class contain properties:
        1. OptionPricerArugments

    and methods:
        1. CalcOptionPremium
        2. calcImpliedVol
        3. calcDeltadVol

    """

    @abstractclassmethod
    def calcOpotionPremium(self):
        raise NotImplementedError

    @abstractclassmethod
    def calcImpliedVol(self):
        raise NotImplementedError

    @abstractclassmethod
    def calcDeltadVol(self):
        raise NotImplementedError


class Optionargument(metaclass=ABCMeta):
    
    @abstractclassmethod
    def __init__(self, s=0, t2m=0, r=0, vol=0, iscall=True, strike=0):
        """

        Args:
            s(float):       underlying price
            t2m(float):     time to maturity
            r(float):       annual interest rate
            vol(float):     volatility
            iscall(bool):
            strike(float):  strike price
        """
        self.s = s
        self.t2m = t2m
        self.r = r
        self.vol = vol
        self.iscall = iscall
        self.strike = strike
        
class Vanillaoptionargument(Optionargument):
    """
    Vanillaoptionargument for european options and ameriacan optoins
    """
    def __init__(self, s=0, t2m=0, r=0, vol=0, iscall=True, strike=0):
        """

        Args:
            s(float):       underlying price
            t2m(float):     time to maturity
            r(float):       annual interest rate
            vol(float):     volatility
            iscall(bool):
            strike(float):  strike price
        """
        super.__init__(s, t2m, r, vol, iscall, strike)


class Europeanoptionpricer(OptionPricer):
    """
    Defined vanilla european option pricer
    """

    def __init__(self, optionargument):
        self.optionargument = optionargument

    def calcOpotionPremium(self):
        return self.europeancallprice() if self.iscall else self.europeanputprice()

    def europeancallprice(self):
        d1 = (np.log(self.s/self.strike) + (self.r + self.vol**2)*self.t2m)/self.vol/np.sqrt(self.t2m)
        d2 = d1 - self.vol/np.sqrt(self.t2m)
        call = self.s*norm.cdf(d1) - self.strike*np.exp(-self.r*self.t2m)*norm.cdf(d2)
        return call

    def europeanputprice(self):
        d1 = (np.log(self.s/self.strike) + (self.r + self.vol**2)*self.t2m)/self.vol/np.sqrt(self.t2m)
        d2 = d1 - self.vol/np.sqrt(self.t2m)
        put = -self.s*norm.cdf(-d1) + self.strike*np.exp(-self.r*self.t2m)*norm.cdf(-d2)
        return put

    def calcImpliedVol(self):
        raise NotImplementedError

    def calcDeltadVol(self):
        raise NotImplementedError