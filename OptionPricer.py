
from abc import ABCMeta, abstractclassmethod

class OptionPricer(metaclass=ABCMeta):
    """
    Abstract class interface for an OptionPricer

    Derived class contain properties:
        1. OptionPricerArugments

    and methods:
        1. CalcOptionPremium
        2. CalcImpliedVol
        3. CalcDelta

    """

    @abstractclassmethod
    def CalcOpotionPremium(self):
        raise NotImplementedError

    @abstractclassmethod
    def CalcImpliedVol(self):
        raise NotImplementedError

    @abstractclassmethod
    def CalcDelta(self):
        raise NotImplementedError

class Optionargument(metaclass=ABCMeta):
    s = None
    t2m = None
    r = None
    vol = None
    iscall = None
    strike = None

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
        self.s = s
        self.t2m = t2m
        self.r = r
        self.vol = vol
        self.iscall = iscall
        self.strike = strike


class Europeanoptionpricer(OptionPricer):
    """
    Defined vanilla european option pricer
    """

    def __init__(self, optionargument):
        self.optionargument = optionargument

    def CalcOpotionPremium(self):
        pass
