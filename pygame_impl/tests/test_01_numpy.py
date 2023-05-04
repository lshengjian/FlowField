import numpy as np
from numba import jit

@jit
def length(z):
    return abs(z)

def test_numba():
    data=np.array([3+4j,6+8j])
    F=np.frompyfunc(length, 1, 1)
    rs=np.asarray(F(data)).astype(int)
    assert len(rs)==2
    assert rs[0]==5 and rs[1]==10


    