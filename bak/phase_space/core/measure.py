from dataclasses import dataclass
from field.utils import Bound

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
    
    def value_at(self,index):
        return self._step*index+self.bound.low

    def __iter__(self):
        yield from self._ds
    def __str__(self):
        return f'{self.name}({self.bound})'
