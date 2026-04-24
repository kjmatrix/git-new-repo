import numpy as np
a = np.array([[1,2,3], [1, 23 , 34]])
print(a)
#a.ndim
#a.shape
#a.dtype
#a.itemsize
#a.size
#a.nbytes
a[0,:]
a[0,1] = 11
print(a)
np.zeros((2,3))
np.full_like(a.shape, 5)
np.random.rand(4, 2)
np.random.randint(1, 5, size=(4, 4))