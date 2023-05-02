from typing import Tuple,Callable
import numpy as np
#from flowfield.demos import F1
from flowfield.utils import apply_fun 
from flowfield.utils import linear_gradient
import math

CS=linear_gradient("#0000FF","#FF0000",100)
class Grid:
    def __init__(self,fun:Callable[[complex], float],xs:Tuple,ys:Tuple,n:int=20 ):
        Y, X = np.ogrid[ys[1] : ys[0] :n*1j, xs[0] : xs[1] : n * 1j]
        Z=X + Y * 1j
        assert Y.shape==(n,1)
        assert Y[0,0]==ys[1] and Y[n-1,0]==ys[0]
        assert X.shape==(1,n)
        assert X[0,0]==xs[0] and X[0,n-1]==xs[1]
        assert Z.shape==(n,n)
        self.K = apply_fun(fun,Z)
        assert self.K.shape==(n,n)
        #print(self.K)

    def slop(self,row:int,col:int):
        return self.K[row,col]

    def angle(self,row:int,col:int):
        return math.atan(self.K[row,col])
    
    def color(self,row:int,col:int):
        a = math.atan(self.K[row,col])+math.pi/2
        n =round(a/math.pi*99)
        return CS[n]