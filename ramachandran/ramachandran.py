"""
See:
https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2440669/
https://byjus.com/maths/dihedral-angle/
http://tutorial.math.lamar.edu/Classes/CalcIII/EqnsOfPlanes.aspx
http://tutorial.math.lamar.edu/Classes/CalcII/CrossProduct.aspx#Vectors_CrossProd_Ex2
"""
import numpy as np

class Ramachandran:

    def __init__(self):
        pass

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
        :return: the cosine of the dihedral angle between the two vectors & the dihedral angle itself
        """
        cos_theta = np.dot(x, y) / (np.linalg.norm(x) * np.linalg.norm(y))
        theta = np.arccos(cos_theta)
        return cos_theta, theta

    def phi(self, norm):
        print(norm)
    def psi(self):
        pass


    # def main():
    #
    # if __name__ == '__main__':
    #     main()
