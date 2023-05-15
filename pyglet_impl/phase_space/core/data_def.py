#import numpy as np
from dataclasses import dataclass
from phase_space.utils import Bound
#User = collections.namedtuple('User', 'name age id')


class Vector:
    def __init__(self,props:str='x1,x2'):
        ss=props.split(',')
        dim=len(ss)
        self._data=[0]*dim #np.zeros(n)
        self._dim=dim
        self._props=ss
        self._prop_map={}
        for i in range(dim):
            key=ss[i]
            self._prop_map[key]=i

    def get_value(self,name):
        idx=self._prop_map[name]
        return self._data[idx]
    def set_data(self,*ds):
        n=min(self._dim,len(ds))
        for i in range(n):
            self._data[i]=ds[i]

    def __getattr__(self, name):
        #print(name)
        if name not in self._prop_map.keys():
            return
        idx=self._prop_map[name]
        return self._data[idx]
         
    # def __setattr__(self, name, value):
    #     if name not in self._prop_map.keys():
    #         return
    #     idx=self._prop_map[name]
    #     self._data[idx] = value

    def __iter__(self):
        yield from self._data


@dataclass
class ArgInfo:
    """可变参数定义."""
    name: str
    value: float
    low: float
    high: float
    step: float=0 
    desc: str=None
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
    num_sampling:int =10

    @property
    def is_sampling(self):
        return self.num_sampling>1
    def __post_init__(self):
        self._ds=[self.bound.low]
        if self.num_sampling<2:
            self.num_sampling=2
        self._step=(self.bound.high-self.bound.low)/(self.num_sampling-1)
        for i in range(1,self.num_sampling):
            self._ds.append(self.bound.low+i*self._step)
    
    def get_position(self,index):
        return self._step*index+self.bound.low

    def __iter__(self):
        yield from self._ds

