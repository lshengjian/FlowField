from abc import ABC, abstractmethod
from math import atan,pi,atan2,tan
from pyglet.math import Vec2
from typing import Callable,Dict
from math import sin


def dydt(p:Vec2,time:float,args:Dict[str,float]):
  x,y=p.x,p.y
  return -args['K1']*sin(x)-args['K2']*y

class SamplePoint:
    default_args:Dict[str,float]={'K1':2.0,'K2':1}

    def __init__(self,p:Vec2=Vec2(0,0),args:Dict[str,float]=None):
        self._pos=p
        #self._vol=Vec2(p.y,0)
        if args is None:
            self._args=SamplePoint.default_args
        self.update()
    def reset(self,x,y):
        self._pos=Vec2(x,y)
        self.update()


    def __str__(self):
        return f"({self._pos.x:.2f},{self._pos.y:.2f})|({self._vol.x:.4f},{self._vol.y:.4f})"
    
    def move(self,dt:float=0.016):
        self._pos+=self._vol*dt

    def update(self,time:float=0.0):
        self._vol=Vec2(self._pos.y,dydt(self._pos,time,self._args))



    @property
    def position(self):
        return self._pos
    @property
    def velocity(self):
        return self._vol    
    @property
    def angle(self):
        a=atan2(self._vol.y,self._vol.x)
        return -atan(tan(a))  #-pi/2~pi/2
        #return -atan2(self._vol.y,self._vol.x)
    @property
    def degree(self):
        return self.angle*180.0/pi

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








  