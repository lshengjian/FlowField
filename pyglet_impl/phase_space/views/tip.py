from typing import Tuple
from pyglet import shapes,graphics
from pyglet.text import Label
from ..core import *


class Tip(View):

    def reset(self):
        super().reset()
        self._tips=[
            Label('TIP: ',font_size=20,color=(0,255,8,210),x=20,y=64,batch=self._batch),
            Label('arrow key show onather case',font_size=18,color=(5,235,28,210),x=20,y=44,batch=self._batch),
            Label('right mouse reset the ball',font_size=18,color=(5,235,28,210),x=20,y=24,batch=self._batch)
        ]
        w,h=self._viewport.size
        self._name=Label(self._space._name,font_size=20,x=20,y=h-30,batch=self._batch)
        self._ylable=Label(self.y_axis.name,font_size=20,x=20,y=h/2,batch=self._batch)
        self._xlable=Label(self.x_axis.name,font_size=20,x=w/2,y=20,batch=self._batch)
        self._desc=Label(self._space._description,font_size=16,color=(255,255,255,255),x=w*0.618,y=h-32,batch=self._batch)

        


