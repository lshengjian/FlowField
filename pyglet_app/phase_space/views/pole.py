from math import pi
from pyglet import shapes
from ..core import *


class Pole(View):
    def reset(self,cfg):
        super().reset(cfg)
        self.sp=self._space.sample_point
        w,h=cfg['WIDTH'],cfg['HEIGHT']
        L=9.8/(self._space.arg_value('a')**2)
        self.rope=shapes.Rectangle(w/2,h-50,6,60*L,color=(205, 155, 44),batch=self._batch)
        self.rope.anchor_x=self.rope.width/2
        self.rope.anchor_y=self.rope.height


    
    def update(self):
        if not hasattr(self,'sp') :
            return
        
        px,_=self.sp.state
        self.rope.rotation=px/pi*180

       
