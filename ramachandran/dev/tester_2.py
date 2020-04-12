import numpy as np
import pandas as pd

# Help to test the Ramachandran class

from ramachandran import Ramachandran

test_sample = '../dihedral_coordinates/2j5p_dihedral_matrix_.csv'
test_df = pd.read_csv(test_sample, header=None)
test_array = test_df[[2, 3, 4]].to_numpy() # numpy array containing only the atomic coordinate information
vectors = []

def vector_norm(o, p, q):
    op = np.array([p[0]-o[0], p[1]-o[1], p[2]-o[2]]) # Calculates the vector be
    oq = np.array([q[0]-o[0], q[1]-o[1], q[2]-o[2]]) # Calculates the vector be
    norm = np.cross(op, oq) # Calculates the vector normal to vectors op & oq
    return norm

for i in range(0,len(test_array)-2,1):
    p = np.array([test_array[i][0], test_array[i][1], test_array[i][2]])
    q = np.array([test_array[i+1][0], test_array[i+1][1], test_array[i+1][2]])
    r = np.array([test_array[i+2][0], test_array[i+2][1], test_array[i+2][2]])
    x = vector_norm(p, q, r)
    vectors.append(x)
# print(vectors[0:20])

def dihedral(x, y):
    cos_theta = np.dot(x, y) / (np.linalg.norm(x) * np.linalg.norm(y))
    theta = np.arccos(cos_theta)
    return cos_theta, theta # Outputs the angle theta in radians

psi_input = []
psi_angle = []
for i in range(0,len(vectors)-2, 3):
    psi_input.append(vectors[i])
    psi_input.append(vectors[i+1])
# print(psi_input)
for i in range(0,len(psi_input)-1,2):
    x = psi_input[i]
    y = psi_input[i+1]
    # print(x)
    # print(y)
    z = dihedral(x,y)
    psi_angle.append(z[1])
print(psi_angle)
print(len(psi_angle))
print(len(test_array))
# return psi_angle
