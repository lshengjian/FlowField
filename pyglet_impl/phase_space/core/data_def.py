from dataclasses import dataclass
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
    '''
    def __init__(
        self,
        name: str,
        value: float,
        low: float,
        high: float,
        step: float=0
        
    ):
        self._name=name
        self._value=value
        self._low=low
        self._high=high
        self._step=step
        self._callbaks=[]

    def notify(self):
        for cb in self._callbaks:
            cb(self)
    def attach(self,callback):
        self._callbaks.append(callback)

    def detach(self,callback):
        self._callbaks.remove(callback)
    @property
    def name(self):
        return self._name
    @property
    def low(self):
        return self._low        
    @property
    def high(self):
        return self._high
    @property
    def step(self):
        return self._step
    @property
    def value(self):
        return self._value
    @value.setter
    def value(self,val):
        self._value=val
        self.notify()
    '''


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

