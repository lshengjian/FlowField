from typing import Dict,List
from ..utils import State
from .data_def import *

class Field:
    def __init__(
        self,
        measures: List[Measure],
        isTwoOrder=False,
        # x_index=0,
        # y_index=1
    ):
        self.name=type(self).__name__
        self.isTwoOrder=isTwoOrder
        self.description=''
        self.measures=measures
        # self.x_axis=measures[x_index]
        # self.y_axis=measures[y_index]
        self.set_description()

        self._args:Dict[str,ArgInfo]={'step':ArgInfo('step',0.02,0.01,0.5,0.01)}
        self.config_args()
        self.reset()
    
    def get_state_zero(self):
        names=self.get_measure_names()
        return Vector(names)
    
    def get_measure(self,name):
        for m in self.measures:
            if m.name==name:
                return m
    def get_sampleing_measures(self):
        return list(
            filter(lambda item:item.is_sampling,
            self.measures)
        )
    def get_measure_names(self):
        return ','.join(map(
            lambda item:item.name,
            self.measures
        ))
      
    def reset(self):
        pass

    def limit(self,xs): 
        rt=[]
        for i,m in enumerate(self.measures):
            rt.append(m.bound.limit(xs[i]))
        # x=self.x_axis.bound.limit(x)
        # y=self.y_axis.bound.limit(y)  
        return rt 
        
    # @property
    # def size(self):
    #     dx=self.x_axis.bound.distance
    #     dy=self.y_axis.bound.distance
    #     return (dx,dy)
    
    def arg_value(self,name:str):
        return self._args[name].value
    

    
    def set_args(self,args:List[ArgInfo]):
        for arg in args:
            self._args[arg.name]=arg


    # def __iter__(self):
    #     yield from self._ds

    def set_description(self):
        pass
        
    def config_args(self):
        pass

    def constraint(self,state:Vector):
        pass