
from typing import Dict,List
from .data_def import *

class Field:
    def __init__(
        self,
        x_measure: Measure,
        y_measure: Measure,
        isTwoOrder=False,
        
        
    ):
        self.name=type(self).__name__
        self.isTwoOrder=isTwoOrder
        self.description=''
        self.set_description()
        self.x_axis=x_measure
        self.y_axis=y_measure
        self._args:Dict[str,ArgInfo]={'step':ArgInfo('step',0.02,0.01,0.5,0.01)}
        self.config_args()
        self.reset()

    def reset(self):
        self._ds=[]
        i,j=0,0
        for y in  self.y_axis:
            j=0
            for x in  self.x_axis:
                s=self.gradient(x,y)
                if self.isTwoOrder:
                    s=s/y if abs(y)>0 else 9999
                self._ds.append((i,j,s))
                j+=1
            i+=1
    def force(self,x,y): 
        x=self.x_axis.bound.force(x)
        y=self.y_axis.bound.force(y)  
        return x,y  
        
    @property
    def size(self):
        dx=self.x_axis.bound.distance
        dy=self.y_axis.bound.distance
        return (dx,dy)
    
    def arg_value(self,name:str):
        return self._args[name].value
    def get_pos(self,row:int,col:int):
        px=self.x_axis.get_position(col)
        py=self.y_axis.get_position(row)
        return (px,py)
    
    def set_args(self,args:List[ArgInfo]):
        for arg in args:
            self._args[arg.name]=arg


    def __iter__(self):
        yield from self._ds

    def set_description(self):
        pass
        
    def config_args(self):
        pass

    def gradient(self,x:float,y:float):
        pass