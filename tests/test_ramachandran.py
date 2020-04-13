#!/usr/bin/env python

"""Tests for `ramachandran` package."""

import unittest

import numpy as np
import pandas as pd
from ramachandran.ramachandran import Ramachandran

class TestRamachandran(unittest.TestCase):
    """Tests for `ramachandran` package."""
    def __init__(self, test_sample):
        self.test_sample = test_sample

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
        # test_sample = './2j5p_dihedral_matrix_.csv'
        test_df = pd.read_csv(self.test_sample, header=None)
        self.test_array = test_df[[2, 3, 4]].to_numpy() # numpy array containing only the atomic coordinate information
        Ramachandran.vectorise_psi(self)
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

        for v in self.vectors_psi[0:9]:
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
        for i in self.vectors_psi[0]:
            elements_0.append(i)
        for j in range(len(elements_0)):
            self.assertAlmostEqual(elements_0[j],normal_abc[j])
        elements_1 = []
        for i in self.vectors_psi[1]:
            elements_1.append(i)
        for j in range(len(elements_1)):
            self.assertAlmostEqual(elements_1[j],normal_bcd[j])
        elements_3 = []
        for i in self.vectors_psi[3]:
            elements_3.append(i)
        for j in range(len(elements_3)):
            self.assertAlmostEqual(elements_3[j],normal_def[j])
        elements_4 = []
        for i in self.vectors_psi[4]:
            elements_4.append(i)
        for j in range(len(elements_4)):
            self.assertAlmostEqual(elements_4[j],normal_efg[j])
        elements_6 = []
        for i in self.vectors_psi[6]:
            elements_6.append(i)
        for j in range(len(elements_6)):
            self.assertAlmostEqual(elements_6[j],normal_ghi[j])
        elements_7 = []
        for i in self.vectors_psi[7]:
            elements_7.append(i)
        for j in range(len(elements_7)):
            self.assertAlmostEqual(elements_7[j],normal_hij[j])

        self.assertAlmostEqual(self.psi_angle[0], theta_test_1)
        self.assertAlmostEqual(self.psi_angle[1], theta_test_2)
        self.assertAlmostEqual(self.psi_angle[2], theta_test_3)

    def test_003_calculate_phi(self):
        """"""
        # test_sample = './2j5p_dihedral_matrix_.csv'
        test_df = pd.read_csv(self.test_sample, header=None)
        self.test_array = test_df[[2, 3, 4]].to_numpy() # numpy array containing only the atomic coordinate information
        Ramachandran.vectorise_phi(self)
        Ramachandran.phi(self)

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
        k = np.array([14.949,4.394,6.411])
        l = np.array([13.843,3.666,7.168])
        m = np.array([12.609,4.120,6.978])

        # test calculation of vector normal to the plane containing the points c, d, e & f
        cd = np.array([d[0]-c[0], d[1]-c[1], d[2]-c[2]])
        ce = np.array([e[0]-c[0], e[1]-c[1], e[2]-c[2]])
        normal_cde = np.cross(cd,ce)
        de = np.array([e[0]-d[0], e[1]-d[1], e[2]-d[2]])
        df = np.array([f[0]-d[0], f[1]-d[1], f[2]-d[2]])
        normal_def = np.cross(de,df)
        fg = np.array([g[0]-f[0], g[1]-f[1], g[2]-f[2]])
        fh = np.array([h[0]-f[0], h[1]-f[1], h[2]-f[2]])
        normal_fgh = np.cross(fg,fh)
        gh = np.array([h[0]-g[0], h[1]-g[1], h[2]-g[2]])
        gi = np.array([i[0]-g[0], i[1]-g[1], i[2]-g[2]])
        normal_ghi = np.cross(gh,gi)
        ij = np.array([j[0]-i[0], j[1]-i[1], j[2]-i[2]])
        ik = np.array([k[0]-i[0], k[1]-i[1], k[2]-i[2]])
        normal_ijk = np.cross(ij,ik)
        jk = np.array([k[0]-j[0], k[1]-j[1], k[2]-j[2]])
        jl = np.array([l[0]-j[0], l[1]-j[1], l[2]-j[2]])
        normal_jkl = np.cross(jk,jl)

        cos_theta_4 = np.dot(normal_cde, normal_def) / (np.linalg.norm(normal_cde) * np.linalg.norm(normal_def))
        theta_test_4 = np.arccos(cos_theta_4)

        cos_theta_5 = np.dot(normal_fgh, normal_ghi) / (np.linalg.norm(normal_fgh) * np.linalg.norm(normal_ghi))
        theta_test_5 = np.arccos(cos_theta_5)

        cos_theta_6 = np.dot(normal_ijk, normal_jkl) / (np.linalg.norm(normal_ijk) * np.linalg.norm(normal_jkl))
        theta_test_6 = np.arccos(cos_theta_6)

        for v in self.vectors_phi[0:10]:
            print(v)
        print("Normal_cde: {}".format(normal_cde))
        print("Normal_def: {}".format(normal_def))
        print("Normal_fgh: {}".format(normal_fgh))
        print("Normal_ghi: {}".format(normal_ghi))
        print("Normal_ijk: {}".format(normal_ijk))
        print("Normal_jkl: {}".format(normal_jkl))

        for p in self.phi_angle[0:3]:
            print(p)
        print("Theta_4: {}".format(theta_test_4))
        print("Theta_5: {}".format(theta_test_5))
        print("Theta_6: {}".format(theta_test_6))

        elements_2 = []
        for i in self.vectors_phi[2]:
            elements_2.append(i)
        for j in range(len(elements_2)):
            self.assertAlmostEqual(elements_2[j],normal_cde[j])
        elements_3 = []
        for i in self.vectors_phi[3]:
            elements_3.append(i)
        for j in range(len(elements_3)):
            self.assertAlmostEqual(elements_3[j],normal_def[j])
        elements_5 = []
        for i in self.vectors_phi[5]:
            elements_5.append(i)
        for j in range(len(elements_5)):
            self.assertAlmostEqual(elements_5[j],normal_fgh[j])
        elements_6 = []
        for i in self.vectors_phi[6]:
            elements_6.append(i)
        for j in range(len(elements_6)):
            self.assertAlmostEqual(elements_6[j],normal_ghi[j])
        elements_8 = []
        for i in self.vectors_phi[8]:
            elements_8.append(i)
        for j in range(len(elements_8)):
            self.assertAlmostEqual(elements_8[j],normal_ijk[j])
        elements_9 = []
        for i in self.vectors_phi[9]:
            elements_9.append(i)
        for j in range(len(elements_9)):
            self.assertAlmostEqual(elements_9[j],normal_jkl[j])

        self.assertAlmostEqual(self.phi_angle[0], theta_test_4)
        self.assertAlmostEqual(self.phi_angle[1], theta_test_5)
        self.assertAlmostEqual(self.phi_angle[2], theta_test_6)

    def test_004_test_on_coordinates(self):
        # Coordinate data from PDB entry 1a11
        z = np.array([14.402,4.670,-9.708])
        a = np.array([14.637,5.953,-9.674])
        b = np.array([13.825,6.883,-10.510])
        c = np.array([12.385,6.909,-9.995])
        d = np.array([11.572,7.782,-10.525])
        e = np.array([10.156,7.859,-10.065])
        f = np.array([9.466,6.514,-10.300])
        g = np.array([10.011,5.698,-11.161])
        h = np.array([9.385,4.373,-11.430])
        i = np.array([9.476,3.506,-10.174])
        j = np.array([10.667,3.212,-9.730])
        k = np.array([10.817,2.375,-8.507 ])
        l = np.array([10.231,3.125,-7.310])
        m = np.array([10.055,4.411,-7.436])
        n = np.array([9.488,5.201,-6.309])
        o = np.array([7.971,4.999,-6.259])

        # Calculate psi angles
        ab = np.array([b[0]-a[0], b[1]-a[1], b[2]-a[2]])
        ac = np.array([c[0]-a[0], c[1]-a[1], c[2]-a[2]])
        normal_abc = np.cross(ab,ac)
        bc = np.array([c[0]-b[0], c[1]-b[1], c[2]-b[2]])
        bd = np.array([d[0]-b[0], d[1]-b[1], d[2]-b[2]])
        normal_bcd = np.cross(bc,bd)

        cos_theta_1 = np.dot(normal_abc, normal_bcd) / (np.linalg.norm(normal_abc) * np.linalg.norm(normal_bcd))
        theta_test_1 = np.arccos(cos_theta_1)

        de = np.array([e[0]-d[0], e[1]-d[1], e[2]-d[2]])
        df = np.array([f[0]-d[0], f[1]-d[1], f[2]-d[2]])
        normal_def = np.cross(de,df)
        ef = np.array([f[0]-e[0], f[1]-e[1], f[2]-e[2]])
        eg = np.array([g[0]-e[0], g[1]-e[1], g[2]-e[2]])
        normal_efg = np.cross(ef,eg)

        cos_theta_2 = np.dot(normal_def, normal_efg) / (np.linalg.norm(normal_def) * np.linalg.norm(normal_efg))
        theta_test_2 = np.arccos(cos_theta_2)

        gh = np.array([h[0]-g[0], h[1]-g[1], h[2]-g[2]])
        gi = np.array([i[0]-g[0], i[1]-g[1], i[2]-g[2]])
        normal_ghi = np.cross(gh,gi)
        hi = np.array([i[0]-h[0], i[1]-h[1], i[2]-h[2]])
        hj = np.array([j[0]-h[0], j[1]-h[1], j[2]-h[2]])
        normal_hij = np.cross(hi,hj)

        cos_theta_3 = np.dot(normal_ghi, normal_hij) / (np.linalg.norm(normal_ghi) * np.linalg.norm(normal_hij))
        theta_test_3 = np.arccos(cos_theta_3)

        # Calculate phi angles (have to remove first amino acid to align amino acid to phi angle, first amino acid in a list has no phi angle)=
        za = np.array([a[0]-z[0], a[1]-z[1], a[2]-z[2]])
        zb = np.array([b[0]-z[0], b[1]-z[1], b[2]-z[2]])
        normal_zab = np.cross(za,zb)
        # de = np.array([e[0]-d[0], e[1]-d[1], e[2]-d[2]])
        # df = np.array([f[0]-d[0], f[1]-d[1], f[2]-d[2]])
        # normal_def = np.cross(de,df)

        cos_theta_5 = np.dot(normal_zab, normal_abc) / (np.linalg.norm(normal_zab) * np.linalg.norm(normal_abc))
        theta_test_5 = np.arccos(cos_theta_5)

        cd = np.array([d[0]-c[0], d[1]-c[1], d[2]-c[2]])
        ce = np.array([e[0]-c[0], e[1]-c[1], e[2]-c[2]])
        normal_cde = np.cross(cd,ce)
        de = np.array([e[0]-d[0], e[1]-d[1], e[2]-d[2]])
        df = np.array([f[0]-d[0], f[1]-d[1], f[2]-d[2]])
        normal_def = np.cross(de,df)

        cos_theta_6 = np.dot(normal_cde, normal_def) / (np.linalg.norm(normal_cde) * np.linalg.norm(normal_def))
        theta_test_6 = np.arccos(cos_theta_6)

        fg = np.array([g[0]-f[0], g[1]-f[1], g[2]-f[2]])
        fh = np.array([h[0]-f[0], h[1]-f[1], h[2]-f[2]])
        normal_fgh = np.cross(fg,fh)
        gh = np.array([h[0]-g[0], h[1]-g[1], h[2]-g[2]])
        gi = np.array([i[0]-g[0], i[1]-g[1], i[2]-g[2]])
        normal_ghi = np.cross(gh,gi)

        cos_theta_7 = np.dot(normal_fgh, normal_ghi) / (np.linalg.norm(normal_fgh) * np.linalg.norm(normal_ghi))
        theta_test_7 = np.arccos(cos_theta_7)

        theta_test_1_deg = np.rad2deg(theta_test_1)
        theta_test_2_deg = np.rad2deg(theta_test_2)
        theta_test_3_deg = np.rad2deg(theta_test_3)
        theta_test_5_deg = np.rad2deg(theta_test_5)
        theta_test_6_deg = np.rad2deg(theta_test_6)
        theta_test_7_deg = np.rad2deg(theta_test_7)

        print("theta_1 vs psi_1: {} vs {}".format(theta_test_1_deg, 172.8))
        print("theta_2 vs psi_2: {} vs {}".format(theta_test_2_deg, -19.4))
        print("theta_3 vs psi_3: {} vs {}".format(theta_test_3_deg, -61.7))
        print("theta_5 vs phi_1: {} vs {}".format(theta_test_5_deg, 67.5))
        print("theta_6 vs phi_2: {} vs {}".format(theta_test_6_deg, -59.6))
        print("theta_7 vs phi_3: {} vs {}".format(theta_test_7_deg, -66.4))

        self.assertEqual(np.round(theta_test_1_deg, 1),172.8)
        self.assertEqual(np.round(theta_test_2_deg, 1),-19.4*-1)
        self.assertEqual(np.round(theta_test_3_deg, 1),-61.7*-1)
        self.assertAlmostEqual(np.round(theta_test_5_deg, 1),67.5)
        self.assertAlmostEqual(np.round(theta_test_6_deg, 1),-59.6*-1)
        self.assertAlmostEqual(np.round(theta_test_7_deg, 1),-66.4*-1)

def main():
    tester = TestRamachandran('./2j5p_dihedral_matrix_.csv')
    tester.test_001_vector_norm_dihedral()
    tester.test_002_calculate_psi()
    tester.test_003_calculate_phi()
    tester.test_004_test_on_coordinates()

if __name__ == '__main__':
    main()
