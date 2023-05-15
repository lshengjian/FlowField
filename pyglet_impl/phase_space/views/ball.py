# from math import pi
from pyglet import shapes
from ..core import *

class Ball(View):
        
    def reset(self):
        super().reset()
        self._body=shapes.Circle(0,0,6,color=(255, 255, 0),batch=self._batch)

    def moveto(self,sp:SamplePoint):
        px,py,_=sp.state
        x,y=self.get_pos(px,py)
        self._body.position=(x,y)


       

