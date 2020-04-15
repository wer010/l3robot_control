import numpy as np

a = np.array([40.643,0.915])
b = np.array([-0.665,34.855])
print(np.arccos(np.dot(a,b)/(np.sqrt(np.dot(a,a))*np.sqrt(np.dot(b,b))))*180/np.pi)