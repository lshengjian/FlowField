from math import pi
from pyglet import shapes
from ..core import *


class Pole(View):
    def __init__(self,field:Space,viewport:Viewport=default_viewport,bg_color=None):
        super().__init__(field,viewport,bg_color)
        
    
    def reset(self):
        super().reset()
        w,h=self._viewport.size
        x,y=self._viewport.start
        L=9.8/(self._space.arg_value('a')**2)
        self.rope=shapes.Rectangle(x+w/2,y+h-50,6,60*L,color=(205, 155, 44),batch=self._batch)
        self.rope.anchor_x=self.rope.width/2
        self.rope.anchor_y=self.rope.height
        #print('Pole reset')

    
    # def moveto(self,sp:SamplePoint):
    #     px,_,_=sp.state
    #     self.rope.rotation=px/pi*180

       

