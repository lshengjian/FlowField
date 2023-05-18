from abc import ABC, abstractmethod
from ..utils import *
from .state import *
from pyglet import shapes,graphics
from phase_space.core import Measure,Space,ArgInfo

WIDTH = 1024
HEIGHT = 768
FPS = 60
default_viewport=Viewport(Point(0,0),Size(WIDTH,HEIGHT))
class View(ABC):
    def __init__(self,space:Space,axis:str=None,viewport:Viewport=default_viewport):#,bg_color=None
        self._viewport=viewport
        self._space:Space=space
        ms=space.names
        if axis is None:
            ms=space.names[:2]
            
        else:
            ms=axis.split(' ')
        
        #print(ms)
        self.x_axis:Measure=space.get_measure(ms[0])
        self.y_axis:Measure=space.get_measure(ms[1])
        #self._bg_color=bg_color
        w,h=self._viewport.size
        ox,oy=self._viewport.start
        kx=w/self.x_axis.bound.distance
        ky=h/self.y_axis.bound.distance
        lx,ly=self.x_axis.bound.low,self.y_axis.bound.low
        self._ox,self._oy=ox,oy
        self._kx,self._ky=kx,ky
        self._lx,self._ly=lx,ly
        self._w,self._h=w,h
        
    def get_vec_zero(self):
        ns=f'{self.x_axis.name},{self.y_axis.name}'
        return State(ns)

    def on_click(self,sx,sy):
        pass
    #@abstractmethod  
    def update(self):
        pass

    def reset(self):
        self._batch = graphics.Batch()
        #print('View Reset')
        # if self._bg_color is not  None:
        #     self._bg=shapes.Rectangle(self._lx,self._ly,self.w,self.h,color=self._bg_color ,batch=self._batch)
    

    def render(self):
        self._batch.draw()
    
    def get_space_pos(self,sx,sy):
        x=(sx-self._ox)/self._kx+self._lx
        y=(sy-self._oy)/self._ky+self._ly
        return x,y

    def get_pos(self,x,y):
        x=self.x_axis.bound.limit(x)
        y=self.y_axis.bound.limit(y)
        sx=self._ox+(x-self._lx)*self._kx
        sy=self._oy+(y-self._ly)*self._ky
        return round(sx),round(sy)


