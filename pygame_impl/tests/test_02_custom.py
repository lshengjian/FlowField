import  sys
from os import path
dir=path.abspath(path.dirname(__file__) + './..')
sys.path.append(dir)

import numpy as np
from numba import jit
from flowfield.demos import F1
from flowfield.utils import apply_fun

def test_demos():
    data=np.array([3+4j,6+8j])
    rs=apply_fun(F1,data)
    
    assert len(rs)==2
    assert rs[0]==0.0 and rs[1]==-1.0


    