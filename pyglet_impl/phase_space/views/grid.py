from typing import Tuple
from pyglet import shapes,graphics
from pyglet.text import Label
from ..core import *
from phase_space.utils import linear_gradient
from math import pi,atan
from ..core.sample_point import SamplePoint
class Grid(View):
    N_COLORS:int = 8
    def reset(self):
        super().reset()
        self.sp:SamplePoint=SamplePoint(self)
        
        w,h=self._viewport.size
        self._body=shapes.Circle(w/2,h/2,6,color=(255, 255, 0),batch=self._batch)

        self._lines=[]
        self._colors=linear_gradient('#0000FF','#FF0000',self.N_COLORS)
        self.cell_side=(w/(self.x_axis.num_sampling-1)+(self.y_axis.num_sampling-1))*0.5*0.618
                # self._ds=[]
        i,j=0,0
        for y in  self.y_axis:
            j=0
            for x in  self.x_axis:
                data=self._space.get_state_zero()
                data.set_data(x,y) #todo
                s=self._space.constraint(data)
                if not self._space._isFirstOrder:
                    s=s/y if abs(y)>0 else 1e16
                self.add_line((i,j,s))
                j+=1
            i+=1
    def on_click(self,sx,sy):
        x,y=self.get_space_pos(sx,sy)
        data=list(self.sp.state)
        data[self.sp._x_index]=x
        data[self.sp._y_index]=y
        self.sp.state.set_data(*data)


    def update(self):
        
        self.sp.update()
        px=self.sp.state.value(self.x_axis.name)
        py=self.sp.state.value(self.y_axis.name)
        x,y=self.get_pos(px,py)
        self._body.position=(x,y)            
        
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
    def get_pos_by_indexs(self,row:int,col:int):
        px=self.x_axis.value_at(col)
        py=self.y_axis.value_at(row)
        return (px,py)
    def add_line(self,sp:Tuple): #sp:(row,col,slop)
        x,y=self.get_pos_by_indexs(sp[0],sp[1])      
        sx,sy=self.get_pos(x,y)
        rect=shapes.Rectangle(sx, sy,self.cell_side ,1,color=(50, 45, 30),batch=self._batch)
        rect.anchor_position=(rect.width/2,rect.height/2)
        #c=shapes.Circle(sx, sy,1,color=(5, 245, 13),batch=self._batch)
        c=shapes.Rectangle(sx, sy,self.cell_side/2 ,1,color=(255, 245, 235),batch=self._batch)
        c.anchor_position=(0,0)
        self.rotate(sp[2], rect,True)
        self.rotate(sp[2], c)
        self._lines.append((c,rect))

        



