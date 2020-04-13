"""
See:
https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2440669/
https://byjus.com/maths/dihedral-angle/
http://tutorial.math.lamar.edu/Classes/CalcIII/EqnsOfPlanes.aspx
http://tutorial.math.lamar.edu/Classes/CalcII/CrossProduct.aspx#Vectors_CrossProd_Ex2
"""
import numpy as np
import pandas as pd
import pickle

class Ramachandran:
    def __init__(self, walk_path, test_sample, name):
        self.walk_path = walk_path
        self.test_sample = test_sample # a pandas dataframe
        self.name = name

    def vector_norm(self, o, p, q):
        """
        Calculates a vector normal to the plane containing the points o, p, & q).
        The φ angle is computed between the normal to the plane made by three atoms Ci−1, Ni, and Cαi
        and the normal to the plane made by the three atoms Ni, Cαi, and Ci.
        The ψ angle is calculated between the normals made by the Ni, Cαi, Ci plane and the Cαi, Ci, Ni+1
        plane.
        :param o: np array containing atomic coordinate positions
        :param p: np array containing atomic coordinate positions
        :param q: np array containing atomic coordinate positions
        :return: vector normal to each plane for φ & ψ angle calculation
        """
        op = np.array([p[0]-o[0], p[1]-o[1], p[2]-o[2]]) # Calculates the vector between the point o & the point p. Points o & p lie in the same plance
        oq = np.array([q[0]-o[0], q[1]-o[1], q[2]-o[2]]) # Calculates the vector between the point o & the point q. Points o & q lie in the same plance
        norm = np.cross(op, oq) # Calculates the vector normal to vectors op & oq

        return norm

    def dihedral(self, x, y):
        """
        Returns the dihedral angle between two vectors
        :param x: numpy array of coordinates for vector #1
        :param y: numpy array of coordinates for vector #2
        :return: the cosine of the dihedral angle between the two vectors & the dihedral angle itself in radians
        """
        try:
            cos_theta = np.dot(x, y) / (np.linalg.norm(x) * np.linalg.norm(y))
        except:
            pass
        try:
            theta = np.arccos(cos_theta)
        except:
            pass
        try:
            return cos_theta, theta # Outputs the angle theta in radians
        except:
            pass

    def make_test_array(self, test_sample):
        """
        Takes as input a pandas dataframe of protein atomic coordinate information & returns a numpy array of atomic coordinates
        :param test_sample: a pandas dataframe
        :return: a numpy array
        """
        try:
            self.test_df = pd.read_csv(self.test_sample, header=None)
            self.test_array = self.test_df[[2, 3, 4]].to_numpy() # numpy array containing only the atomic coordinate information
        except:
            pass
        try:
            return self.test_array
        except:
            pass

    def vectorise_psi(self):
        """
        Takes as input a numpy array of atomic coordinates and returns a list of normal vectors between consecutive pairs of atomic coordinate points
        :param test_array: a numpy array
        :return: a list of vectors normal to two consecutive points of atomic coordinates
        """
        self.vectors_psi = []
        try:
            for i in range(0,len(self.test_array)-2,1):
                p = np.array([self.test_array[i][0], self.test_array[i][1], self.test_array[i][2]])
                q = np.array([self.test_array[i+1][0], self.test_array[i+1][1], self.test_array[i+1][2]])
                r = np.array([self.test_array[i+2][0], self.test_array[i+2][1], self.test_array[i+2][2]])
                x = Ramachandran.vector_norm(self, p, q, r)
                self.vectors_psi.append(x)
        except:
            pass
        try:
            return self.vectors_psi
        except:
            pass

    def psi(self):
        """
        Calculates the psi angle between the Ni, Cαi, Ci plane and the Cαi, Ci, Ni+1 plane.
        :param vectors: a list of vectors normal to two consecutive points of atomic coordinates
        :return: a list of psi angles
        """
        self.psi_input = []
        self.psi_angle = []
        for i in range(0,len(self.vectors_psi)-2, 3):
            self.psi_input.append(self.vectors_psi[i])
            self.psi_input.append(self.vectors_psi[i+1])
        for i in range(0,len(self.psi_input)-1,2):
            x = self.psi_input[i]
            y = self.psi_input[i+1]
            z = Ramachandran.dihedral(self,x,y)
            # z = rama.dihedral(x,y)
            self.psi_angle.append(z[1])
        return self.psi_angle

    def save_psi(self, walk_path, name):
        with open(self.walk_path + '/' + self.name.split('_')[0] + '_psi.pickle', 'wb', buffering=500000000) as file:
            pickle.dump(self.psi_angle, file, protocol=4) # Save as a pickle object

    def vectorise_phi(self):
        """
        Takes as input a numpy array of atomic coordinates and returns a list of normal vectors between consecutive pairs of atomic coordinate points
        :param test_array: a numpy array
        :return: a list of vectors normal to two consecutive points of atomic coordinates
        """
        self.vectors_phi = []
        try:
            for i in range(0,len(self.test_array)-2,1):
                p = np.array([self.test_array[i][0], self.test_array[i][1], self.test_array[i][2]])
                q = np.array([self.test_array[i+1][0], self.test_array[i+1][1], self.test_array[i+1][2]])
                r = np.array([self.test_array[i+2][0], self.test_array[i+2][1], self.test_array[i+2][2]])
                x = Ramachandran.vector_norm(self, p, q, r)
                self.vectors_phi.append(x)
        except:
            pass
        try:
            return self.vectors_phi
        except:
            pass

    def phi(self):
        """
        Calculates the phi angle between the Ci−1, Ni, and Cαi plane and the Ni, Cαi, and Ci plane.
        :param vectors: a list of vectors normal to two consecutive points of atomic coordinates
        :return: a list of psi angles
        """
        self.phi_input = []
        self.phi_angle = []
        for i in range(2,len(self.vectors_phi)-2, 3):
            self.phi_input.append(self.vectors_phi[i])
            self.phi_input.append(self.vectors_phi[i+1])
        for i in range(0,len(self.phi_input)-1,2):
            x = self.phi_input[i]
            y = self.phi_input[i+1]
            z = Ramachandran.dihedral(self,x,y)
            # z = rama.dihedral(x,y)
            self.phi_angle.append(z[1])
        return self.phi_angle

    def save_phi(self, walk_path, name):
        with open(self.walk_path + '/' + self.name.split('_')[0] + '_phi.pickle', 'wb', buffering=500000000) as file:
            pickle.dump(self.phi_angle, file, protocol=4) # Save as a pickle object
