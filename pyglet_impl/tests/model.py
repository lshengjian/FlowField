from abc import ABC, abstractmethod
from math import atan,pi,atan2,tan
from pyglet.math import Vec2
from typing import Callable,Dict
from math import sin


def dydt(p:Vec2,time:float,args:Dict[str,float]):
  x,y=p.x,p.y
  return -args['K1']*sin(x)-args['K2']*y



class Space: #(ABC)
    def __init__(self,start:Vec2,end:Vec2,offset:Vec2):
        self._ps=[]
        max_x,max_y=end.x,end.y
        x,y=start.x,start.y
        while(y<=max_y):
            while(x<=max_x):
                self._ps.append(SamplePoint(Vec2(x,y)))
                x+=offset.x
            y+=offset.y
            x=start.x
            
    def reset(self): 
        for sp in self:
            sp.update()

    # @abstractmethod
    # @property
    # def points(self):
    #     return self._ps  
    
    def __iter__(self):
        yield from self._ps
    # @abstractmethod
    # def get(self, item):
    #     """Returns an object with a .items() call method
    #     that iterates over key,value pairs of its information."""
    #     pass








  