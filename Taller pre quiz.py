import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt

dim1, dim2, dim3, dim4 = 10,15,20,400
size = dim1*dim2*dim3*dim4

matriz4D= np.random.rand(dim1,dim2,dim3,dim4)

print("Forma: ", matriz4D.shape)
print("Size: ", matriz4D.size)
