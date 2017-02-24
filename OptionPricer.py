
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

class Optionpricerarugment(metaclass=ABCMeta):
    s = None
    t2m = None
    r = None
    vol = None
    iscall = None
    strike = None