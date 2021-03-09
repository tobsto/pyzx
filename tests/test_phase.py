import unittest
import sys
if __name__ == '__main__':
    sys.path.append('..')
    sys.path.append('.')

try:
    import numpy as np
    from pyzx.tensor import tensorfy, compare_tensors
except ImportError:
    np = None

from pyzx.phase import Phase
from fractions import Fraction
from sympy import Symbol

class TestPhase(unittest.TestCase):

    def setUp(self):
        self.phase_fraction = Phase(Fraction(1, 10))
        self.phase_int = Phase(2)
        self.phase_float = Phase(0.2)
        self.phase_sym = Phase(Symbol('gamma'))

    def test_addition(self):
        p = Phase(Fraction(2, 10))
        self.assertEqual(p + self.phase_fraction, Phase(Fraction(3, 10)))

        self.assertEqual(p + self.phase_int, Phase(Fraction(11, 5)))
        self.assertEqual(self.phase_int + self.phase_float, Phase(2 + 0.2))

        self.assertEqual(self.phase_int + self.phase_sym, Phase(Symbol('gamma') + 2))

if __name__ == '__main__':
    unittest.main()
