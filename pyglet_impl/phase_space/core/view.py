from abc import ABC, abstractmethod
from typing import Tuple
from pyglet import shapes,graphics
from phase_space.core import Measure,Field,ArgInfo
from phase_space.utils import linear_gradient
from math import pi,atan

class View(ABC):
    CS:int = 8
    def __init__(self,field:Field=None):
        self._batch = graphics.Batch()
        #self._size=size
        self._field=field
        self._colors=linear_gradient('#0000FF','#FF0000',View.CS)
        

    @abstractmethod
    def reset(self):
        pass
    
    def render(self):
        #self.circle.position=(p.x,p.y)
        self._batch.draw()


    def set_color(self, slop, shape):
        a = -atan(slop)
        d= a*180.0/pi
        shape.rotation=d
        a = -a+pi/2
        n =round(a/pi*View.CS)
        if n>View.CS-1:
            n=View.CS-1
        shape.color=self._colors[n]

