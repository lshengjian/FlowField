from abc import ABC, abstractmethod
from ..core.data_def import *
from pyglet import shapes,graphics
from phase_space.core import Measure,Field,ArgInfo
from .sample_point import SamplePoint

class View(ABC):

    def __init__(self,field:Field,viewport:Viewport,bg_color=None):
        
        self._viewport=viewport
        self._field=field
        self._bg_color=bg_color
        self._batch = graphics.Batch()
        self.reset()
      
    def moveto(self,sp:SamplePoint):
        pass

    def reset(self):
        w,h=self._viewport.size
        ox,oy=self._viewport.start
        kx=w/self._field.x_axis.bound.distance
        ky=h/self._field.y_axis.bound.distance
        lx,ly=self._field.x_axis.bound.low,self._field.y_axis.bound.low
        self._ox,self._oy=ox,oy
        self._kx,self._ky=kx,ky
        self._lx,self._ly=lx,ly
        
        if self._bg_color is not  None:
            self._bg=shapes.Rectangle(lx,ly,w,h,color=self._bg_color ,batch=self._batch)
    

    def render(self):
        self._batch.draw()
    
    def get_space_pos(self,sx,sy):
        x=(sx-self._ox)/self._kx+self._lx
        y=(sy-self._oy)/self._ky+self._ly
        return x,y

    def get_pos(self,x,y):
        sx=self._ox+(x-self._lx)*self._kx
        sy=self._oy+(y-self._ly)*self._ky
        return round(sx),round(sy)


