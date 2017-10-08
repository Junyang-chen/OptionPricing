from scipy.stats import norm
from abc import ABCMeta, abstractmethod
import numpy as np
import scipy.optimize as opt

class OptionPricer(metaclass=ABCMeta):
    """
    Abstract class interface for an OptionPricer

    Derived class contain properties:
        1. OptionPricerArugments

    and methods:
        1. CalcOptionPremium
        2. calcImpliedVol
        3. calcDeltadVol
        4. calcVega

    """

    @abstractmethod
    def calcOptionPremium(self):
        raise NotImplementedError

    @abstractmethod
    def calcImpliedVol(self):
        raise NotImplementedError

    @abstractmethod
    def calcDeltadVol(self):
        raise NotImplementedError

    @abstractmethod
    def calcVega(self):
        raise NotImplementedError

class Optionargument(metaclass=ABCMeta):
    
    @abstractmethod
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
        super().__init__(s, t2m, r, vol, iscall, strike)


class Europeanoptionpricer(OptionPricer):
    """
    Defined vanilla european option pricer black scholes model
    """

    def __init__(self, optionargument):
        """

        Args:
            optionargument:     inputs are optionargument class
        """
        self.optionargument = optionargument

    def calcOptionPremium(self, iscall, strike, s, r, t2m,  vol):
        """

        Returns: option price(float)

        """
        return self.europeancallprice(s, t2m, r, vol, strike) if iscall \
            else self.europeanputprice(s, t2m, r, vol, strike)

    def d1(self, s, t2m, r, vol, strike):
        return (np.log(s/strike) + (r + vol**2/2)*t2m)/vol/np.sqrt(t2m)

    def d2(self, s, t2m, r, vol, strike):
        return self.d1(s, t2m, r, vol, strike) - vol*np.sqrt(t2m)

    def europeancallprice(self, s, t2m, r, vol, strike):
        d1 = self.d1(s, t2m, r, vol, strike)
        d2 = self.d2(s, t2m, r, vol, strike)
        call = s*norm.cdf(d1) - strike*np.exp(-r*t2m)*norm.cdf(d2)
        return call

    def europeanputprice(self, s, t2m, r, vol, strike):
        d1 = self.d1(s, t2m, r, vol, strike)
        d2 = self.d2(s, t2m, r, vol, strike)
        put = -s*norm.cdf(-d1) + strike*np.exp(-r*t2m)*norm.cdf(-d2)
        return put

    def calcImpliedVol(self, s=0, t2m=0, r=0, price=0, iscall=True, strike=0, method = 'BISECT'):
        objfunc = lambda vol: self.calcOpotionPremium(s, t2m, r, vol, strike, iscall) - price
        if price <=0:
            return np.NaN
        if method == 'BISECT':
            return opt.bisect(objfunc, 0, 5)
        elif method == 'NewTon':
            fprime = lambda vol: self.calcVega(s, t2m, r, price, iscall, strike)
            return opt.newton(objfunc, 1, fprime)
        elif method == 'BRENTQ':
            return opt.brentq(objfunc, 0, 5)

    def calcDeltadVol(self, s=0, t2m=0, r=0, vol=0, iscall=True, strike=0):
        d1 = (np.log(s / strike) + (r + vol ** 2) * t2m) / vol / np.sqrt(t2m)
        return norm.cdf(d1) if self.iscall else -norm.cdf(-d1)

    def calcVega(self, s=0, t2m=0, r=0, vol=0, iscall=True, strike=0):
        d1 = (np.log(s / strike) + (r + vol ** 2) * t2m) / vol / np.sqrt(t2m)
        return np.sqrt(t2m) * strike * norm.pdf(d1)