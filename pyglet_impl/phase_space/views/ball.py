from math import pi
from pyglet import shapes
from ..core import *

class Ball(View):
    def __init__(self,field:Field,viewport:Viewport=default_viewport):
        super().__init__(field,viewport)
        self._body=shapes.Circle(0,0,6,color=(255, 255, 0),batch=self._batch)
    
    def moveto(self,sp:SamplePoint):
        px,py=sp.position
        x,y=self.get_pos(px,py)
        self._body.position=(x,y)


       

