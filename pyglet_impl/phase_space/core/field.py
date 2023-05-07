from dataclasses import dataclass
from typing import Dict

from phase_space.utils import Bound
#User = collections.namedtuple('User', 'name age id')

@dataclass
class ArgInfo:
    """可变参数定义."""
    name: str
    value: float
    low: float
    high: float
    step: float=0 
    def __post_init__(self):
        if self.step<=0:
            self.step==(self.high-self.low)/10

@dataclass
class Measure:
    """坐标轴度量的物理量信息."""
    name: str
    bound:Bound
    numSampling:int =10

    def __post_init__(self):
        self._ds=[self.bound.low]
        if self.numSampling<2:
            self.numSampling=2
        self._step=(self.bound.high-self.bound.low)/(self.numSampling-1)
        for i in range(1,self.numSampling):
            self._ds.append(self.bound.low+i*self._step)
    
    def get_position(self,index):
        return self._step*index+self.bound.low

    def __iter__(self):
        yield from self._ds



class Field:
    def __init__(
        self,
        x_measure: Measure,
        y_measure: Measure
        
    ):
        self._xs=x_measure
        self._ys=y_measure
        self._args:Dict[str,ArgInfo]=None
        self.config_args()
        self._ds=[]
        i,j=0,0
        for y in  self._ys:
            j=0
            for x in  self._xs:
                self._ds.append((j,i,self.slop(x,y)))
                j+=1
            i+=1

    def __iter__(self):
        yield from self._ds
    def config_args(self):
        pass

    def slop(self,x:float,y:float):
        pass