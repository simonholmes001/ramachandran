#!/usr/bin/env python

"""Tests for `ramachandran` package."""

import unittest

import numpy as np
import pandas as pd
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

        x = Ramachandran.vector_norm(self, P, Q, R)
        y = Ramachandran.vector_norm(self, Q, R, S)
        z = Ramachandran.dihedral(self, x, y)

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

    def test_002_calculate_psi(self):
        """"""
        test_sample = '2j5p_dihedral_matrix_.csv'
        test_df = pd.read_csv(test_sample, header=None)
        self.test_array = test_df[[2, 3, 4]].to_numpy() # numpy array containing only the atomic coordinate information
        Ramachandran.vectorise(self)
        Ramachandran.psi(self)

        a = np.array([13.085,11.834,6.526])
        b = np.array([13.538,10.454,6.211])
        c = np.array([12.726,9.855,5.067])
        d = np.array([12.964,8.579,4.784])
        e = np.array([12.246,7.911,3.714])
        f = np.array([12.416,6.405,3.752])
        g = np.array([13.316,5.892,2.920])
        h = np.array([13.573,4.458,2.859])
        i = np.array([14.002,3.911,4.219])
        j = np.array([14.502,4.793,5.080])

        # test calculation of vector normal to the plane containing the points a, b, c & d
        ab = np.array([b[0]-a[0], b[1]-a[1], b[2]-a[2]])
        ac = np.array([c[0]-a[0], c[1]-a[1], c[2]-a[2]])
        normal_abc = np.cross(ab,ac)
        bc = np.array([c[0]-b[0], c[1]-b[1], c[2]-b[2]])
        bd = np.array([d[0]-b[0], d[1]-b[1], d[2]-b[2]])
        normal_bcd = np.cross(bc,bd)
        de = np.array([e[0]-d[0], e[1]-d[1], e[2]-d[2]])
        df = np.array([f[0]-d[0], f[1]-d[1], f[2]-d[2]])
        normal_def = np.cross(de,df)
        ef = np.array([f[0]-e[0], f[1]-e[1], f[2]-e[2]])
        eg = np.array([g[0]-e[0], g[1]-e[1], g[2]-e[2]])
        normal_efg = np.cross(ef,eg)
        gh = np.array([h[0]-g[0], h[1]-g[1], h[2]-g[2]])
        gi = np.array([i[0]-g[0], i[1]-g[1], i[2]-g[2]])
        normal_ghi = np.cross(gh,gi)
        hi = np.array([i[0]-h[0], i[1]-h[1], i[2]-h[2]])
        hj = np.array([j[0]-h[0], j[1]-h[1], j[2]-h[2]])
        normal_hij = np.cross(hi,hj)

        cos_test_numerator_1 = np.absolute((normal_abc[0]*normal_bcd[0]) + (normal_abc[1]*normal_bcd[1]) + (normal_abc[2]*normal_bcd[2]))
        cos_test_denominator_1 = np.sqrt(normal_abc[0]**2 + normal_abc[1]**2 + normal_abc[2]**2) * np.sqrt(normal_bcd[0]**2 + normal_bcd[1]**2 + normal_bcd[2]**2)
        cos_test_1 = -cos_test_numerator_1 / cos_test_denominator_1
        theta_test_1 = np.arccos(cos_test_1)

        cos_test_numerator_2 = np.absolute((normal_def[0]*normal_efg[0]) + (normal_def[1]*normal_efg[1]) + (normal_def[2]*normal_efg[2]))
        cos_test_denominator_2 = np.sqrt(normal_def[0]**2 + normal_def[1]**2 + normal_def[2]**2) * np.sqrt(normal_efg[0]**2 + normal_efg[1]**2 + normal_efg[2]**2)
        cos_test_2 = -cos_test_numerator_2 / cos_test_denominator_2
        theta_test_2 = np.arccos(cos_test_2)

        cos_theta_3 = np.dot(normal_ghi, normal_hij) / (np.linalg.norm(normal_ghi) * np.linalg.norm(normal_hij))
        theta_test_3 = np.arccos(cos_theta_3)

        for v in self.vectors[0:9]:
            print(v)
        print("Normal_abc: {}".format(normal_abc))
        print("Normal_bcd: {}".format(normal_bcd))
        print("Normal_def: {}".format(normal_def))
        print("Normal_efg: {}".format(normal_efg))
        print("Normal_ghi: {}".format(normal_ghi))
        print("Normal_hij: {}".format(normal_hij))

        for p in self.psi_angle[0:3]:
            print(p)
        print("Theta_1: {}".format(theta_test_1))
        print("Theta_2: {}".format(theta_test_2))
        print("Theta_3: {}".format(theta_test_3))

        elements_0 = []
        for i in self.vectors[0]:
            elements_0.append(i)
        for j in range(len(elements_0)):
            self.assertAlmostEqual(elements_0[j],normal_abc[j])
        elements_1 = []
        for i in self.vectors[1]:
            elements_1.append(i)
        for j in range(len(elements_1)):
            self.assertAlmostEqual(elements_1[j],normal_bcd[j])
        elements_3 = []
        for i in self.vectors[3]:
            elements_3.append(i)
        for j in range(len(elements_3)):
            self.assertAlmostEqual(elements_3[j],normal_def[j])
        elements_4 = []
        for i in self.vectors[4]:
            elements_4.append(i)
        for j in range(len(elements_4)):
            self.assertAlmostEqual(elements_4[j],normal_efg[j])
        elements_6 = []
        for i in self.vectors[6]:
            elements_6.append(i)
        for j in range(len(elements_6)):
            self.assertAlmostEqual(elements_6[j],normal_ghi[j])
        elements_7 = []
        for i in self.vectors[7]:
            elements_7.append(i)
        for j in range(len(elements_7)):
            self.assertAlmostEqual(elements_7[j],normal_hij[j])

        self.assertAlmostEqual(self.psi_angle[0], theta_test_1)
        self.assertAlmostEqual(self.psi_angle[1], theta_test_2)
        self.assertAlmostEqual(self.psi_angle[2], theta_test_3)


def main():
    tester = TestRamachandran()
    tester.test_001_vector_norm_dihedral()
    tester.test_002_calculate_psi()


if __name__ == '__main__':
    main()
