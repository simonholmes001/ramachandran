#!/usr/bin/env python

"""Tests for `ramachandran` package."""

import numpy as np
import unittest
import numpy as np
from ramachandran.ramachandran import Ramachandran


class TestRamachandran(unittest.TestCase):
    """Tests for `ramachandran` package."""

    def setUp(self):
        """Set up test fixtures, if any."""

    def tearDown(self):
        """Tear down test fixtures, if any."""

    def test_001_vector_norm_dihedral(self):
        """Test something."""
        P = np.array([1, -2, 0])
        Q = np.array([3, 1, 4])
        R = np.array([0, -1, 2])
        S = np.array([0, 22, 2])

        rama = Ramachandran()
        x = rama.vector_norm(P, Q, R)
        y = rama.vector_norm(Q, R, S)
        z = rama.dihedral(x, y)

        # test calculation of vector normal to the plane containing the points P, Q & R
        PQ = np.array([Q[0]-P[0], Q[1]-P[1], Q[2]-P[2]])
        PR = np.array([R[0]-P[0],R[1]-P[1], R[2]-P[2]])
        normal_1 = np.array([PQ[1]*PR[2]-PQ[2]*PR[1], PQ[2]*PR[0]-PQ[0]*PR[2], PQ[0]*PR[1]-PQ[1]*PR[0]])

        # test calculation of vector normal to the plane containing the points Q, R & S
        QR = np.array([R[0]-Q[0], R[1]-Q[1], R[2]-Q[2]])
        QS = np.array([S[0]-Q[0],S[1]-Q[1], S[2]-Q[2]])
        normal_2 = np.array([QR[1]*QS[2]-QR[2]*QS[1], QR[2]*QS[0]-QR[0]*QS[2], QR[0]*QS[1]-QR[1]*QS[0]])

        # claculate the dihedral angle between the two planes by calculating the angle between the two normal vectors

        cos_test_numerator = np.absolute((normal_1[0]*normal_2[0]) + (normal_1[1]*normal_2[1]) + (normal_1[2]*normal_2[2]))
        cos_test_denominator = np.sqrt(normal_1[0]**2 + normal_1[1]**2 + normal_1[2]**2) * np.sqrt(normal_2[0]**2 + normal_2[1]**2 + normal_2[2]**2)
        cos_test = -cos_test_numerator / cos_test_denominator
        theta_test = np.arccos(cos_test)

        print("x: \n{}".format(x))
        print("normal_1: \n{}".format(normal_1))
        print("y: \n{}".format(y))
        print("normal_2: \n{}".format(normal_2))
        print("z: \n{}".format(z))
        print("cos_test: \n{}".format(cos_test))
        print("theta_test: \n{}".format(theta_test))

        for i in range(0,3):
            self.assertEqual(x[i], normal_1[i])
            self.assertAlmostEqual(y[i], normal_2[i])

        self.assertAlmostEqual(z[1], theta_test)




    # def test_002_dot_product(self):
    #     """Test something."""

def main():
    tester = TestRamachandran()
    tester.test_001_vector_norm_dihedral()


if __name__ == '__main__':
    main()
