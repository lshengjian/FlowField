from math import pi
from pyglet import shapes
from ..core import SamplePoint,Field
from .config import WIDTH,HEIGHT
from ..core.view import View

class Ball(View):
    def __init__(self,field:Field=None):
        super().__init__(field)
        self._body=shapes.Circle(0, 0,6,color=(255, 25, 13),batch=self._batch)
        dx,dy=field.size
        self._kx=WIDTH/dx
        self._ky=HEIGHT/dy
        
        if field.name=='Pendulum':
            self.rope=shapes.Rectangle(WIDTH/2,HEIGHT-100,6,200,color=(205, 155, 44),batch=self._batch)
            self.rope.anchor_x=self.rope.width/2
            self.rope.anchor_y=self.rope.height
            

    
    def moveto(self,sp:SamplePoint):
        px,py=sp.position
        x=(px-self._field.x_axis.bound.low)*self._kx
        y=(py-self._field.y_axis.bound.low)*self._ky
        self._body.position=(x,y)
        if self._field.name=='Pendulum':
            self.rope.rotation=-px/pi*180

    def reset(self):
        pass   
       

    def get_screen_pos(self,x,y):
        px=x/self._kx+self._field.x_axis.bound.low
        py=y/self._ky+self._field.y_axis.bound.low
        return (px,py)
