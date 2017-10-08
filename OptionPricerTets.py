import unittest
import OptionPricer

class OptionPricerTestCase(unittest.TestCase):
    def test_Vanilla_price(self):
        inputs = \
            [[True,  65.00,  60.00,  0.08, 0.25, 0.30,  2.1334]]
        pricer = OptionPricer.Europeanoptionpricer(OptionPricer.Vanillaoptionargument())
        for parameter in inputs:
            self.assertAlmostEqual(pricer.calcOptionPremium(*parameter[:-1]), parameter[-1], places=4)


if __name__ == '__main__':
    unittest.main()
