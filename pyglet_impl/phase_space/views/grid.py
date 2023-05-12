from typing import Tuple
from pyglet import shapes,graphics
from pyglet.text import Label
from ..core import *
from phase_space.utils import linear_gradient
from math import pi,atan

class Grid(View):
    N_COLORS:int = 8
    def __init__(self,field:Field,viewport:Viewport=default_viewport):
        super().__init__(field,viewport)
        self._view_port=viewport
    

    def reset(self):
        super().reset()
        self._tips=[
            Label('TIP: ',font_size=20,color=(0,255,8,210),x=20,y=64,batch=self._batch),
            Label('arrow key show onather case',font_size=18,color=(5,235,28,210),x=20,y=44,batch=self._batch),
            Label('right mouse reset the ball',font_size=18,color=(5,235,28,210),x=20,y=24,batch=self._batch)
        ]
        w,h=self._viewport.size
        self._name=Label(self._field.name,font_size=20,x=20,y=h-20,batch=self._batch)
        self._ylable=Label(self._field.y_axis.name,font_size=20,x=20,y=h/2,batch=self._batch)
        self._xlable=Label(self._field.x_axis.name,font_size=20,x=w/2,y=20,batch=self._batch)
        self._desc=Label(self._field.description,font_size=16,color=(255,255,255,255),x=w*0.618,y=h-32,batch=self._batch)

        self._lines=[]
        self._colors=linear_gradient('#0000FF','#FF0000',self.N_COLORS)
        w,h=self._viewport.size
        self.cell_side=(w/(self._field.x_axis.numSampling-1)+(self._field.y_axis.numSampling-1))*0.5*0.618
        #print(w,h,self.cell_side)
        for p in self._field:
            self.add_line(p)
        
    def rotate(self, slop, shape:shapes.Rectangle,auto_color=False):
        a = -atan(slop)
        d= a*180.0/pi
        shape.rotation=d
        if not auto_color:
            return
        a = -a+pi/2
        n =round(a/pi*self.N_COLORS)
        
        if n>self.N_COLORS-1:
            n=self.N_COLORS-1
        shape.color=self._colors[n]

    def add_line(self,sp:Tuple): #sp:(row,col,slop)
        x,y=self._field.get_pos(sp[0],sp[1])      
        sx,sy=self.get_pos(x,y)
        rect=shapes.Rectangle(sx, sy,self.cell_side ,1,color=(50, 45, 30),batch=self._batch)
        rect.anchor_position=(rect.width/2,rect.height/2)
        #c=shapes.Circle(sx, sy,1,color=(5, 245, 13),batch=self._batch)
        c=shapes.Rectangle(sx, sy,self.cell_side/2 ,1,color=(255, 245, 235),batch=self._batch)
        c.anchor_position=(0,0)
        self.rotate(sp[2], rect,True)
        self.rotate(sp[2], c)
        self._lines.append((c,rect))

        



