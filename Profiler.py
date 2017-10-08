"""
This file will contain analysis of python program performance using profiler
http://python.jobbole.com/87621/
"""

import cProfile, pstats
import OptionPricer, StochasticProcess

class GoodProfiler(object):

    def __init__(self, func):
        self.func = func
        self.profiler = cProfile.Profile()

    def run_and_show(self):
        self.profiler.runcall(self.func)
        stats = pstats.Stats(self.profiler)
        stats.strip_dirs()
        stats.sort_stats('cumulative')
        stats.print_stats()


if __name__ == '__main__':
    Europeanoptionpricer_func = lambda: OptionPricer.Europeanoptionpricer(None).calcOptionPremium(*[True, 65.00, 60.00, 0.08, 0.25, 0.30])
    GoodProfiler(Europeanoptionpricer_func).run_and_show()

    geometricbrownianmotion = StochasticProcess.GeometricBrownianMotionGenerator(1, 0.3, 0.1)
    geometricbrownianmotion_func = lambda:geometricbrownianmotion.generatePaths(100)
    GoodProfiler(geometricbrownianmotion_func).run_and_show()