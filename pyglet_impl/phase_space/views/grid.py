from typing import Tuple
from pyglet import shapes,graphics
from pyglet.text import Label
from ..core import Field,ArgInfo
from ..core.view import View

class Grid(View):
    CS:int = 8
    def __init__(self,field:Field=None,width:int=800,height:int=600):
        super().__init__(field)
        self._lines=[]
        self.size=(width,height)
        self.tips=[
            Label('TIP: ',font_size=22,color=(255,255,0,110),x=20,y=height-24,batch=self._batch),
            Label('arrow key show onather case',font_size=18,color=(255,255,0,110),x=20,y=height-44,batch=self._batch),
            Label('right mouse reset the ball',font_size=18,color=(255,255,0,110),x=20,y=height-64,batch=self._batch)
        ]
        self.ylable=Label(self._field.y_axis.name,font_size=20,x=20,y=height/2,batch=self._batch)
        self.xlable=Label(self._field.x_axis.name,font_size=20,x=width/2,y=20,batch=self._batch)
        self.desc=Label(self._field.description,font_size=16,color=(255,235,0,210),x=width*0.618,y=height-32,batch=self._batch)

        self.reset()
        
       

    def reset(self):
        width,height=self.size
        self._lines.clear()
        dx,dy=self._field.size

        self._kx=width/dx
        self._ky=height/dy
         
        self.R=min(self._kx,self._ky)*0.25
        for p in self._field:
            self.add_line(p)
        
         

    def add_line(self,sp:Tuple): #sp:(row,col,slop)
        px,py=self._field.get_pos(sp[0],sp[1])      
        x=(px-self._field.x_axis.bound.low)*self._kx
        y=(py-self._field.y_axis.bound.low)*self._ky
        rect=shapes.Rectangle(x, y,self.R ,2,color=(50, 45, 30),batch=self._batch)
        rect.anchor_position=(rect.width/2,rect.height/2)
        c=shapes.Circle(x, y,2,color=(5, 245, 13),batch=self._batch)
        self.set_color(sp[2], rect)
        self._lines.append((c,rect))

        



