from typing import Tuple
from pyglet import shapes,graphics
from pyglet.text import Label
from ..core import *
from field.utils import linear_gradient
from math import pi,atan2,tan,exp,inf
from ..core.sample_point import SamplePoint
class Grid(View):
    N_COLORS:int = 8
    def __init__(self,space:Space,axis:str=None):
        super().__init__(space,axis)
        self.sp:SamplePoint=SamplePoint(self)
        space.sample_point=self.sp
        self._colors=linear_gradient('#0000FF','#FF4500',self.N_COLORS)

    def set_data(self,state:State,x:float,y:float):
        idx_x=self.sp._x_index
        idx_y=self.sp._y_index
        data=list(state)
        data[idx_x]=x
        data[idx_y]=y
        state.set_data(*data)


    def reset(self,cfg):
        super().reset(cfg)
        w,h=self._viewport.size
        self._body=shapes.Circle(w/2,h/2,6,color=(255, 255, 0),batch=self._batch)
        self._lines=[]
        self.cell_side=(w/(self.x_axis.num_sampling-1)+(self.y_axis.num_sampling-1))*0.5*0.618
        i,j=0,0
        for y in  self.y_axis:
            j=0
            for x in  self.x_axis:
                state=self._space.get_state_zero()
                self.set_data(state,x,y) #todo
                dy=self._space.constraint(state)
                dx=1 if self._space._isFirstOrder else y
                self.add_line_segment((i,j,dy,dx))
                j+=1
            i+=1
    
    def add_line_segment(self,sp:Tuple): #sp:(row,col,slop)
        x,y=self.get_pos_by_indexs(sp[0],sp[1])      
        sx,sy=self.get_pos(x,y)
        rect=shapes.Rectangle(sx, sy,self.cell_side ,2,color=(50, 45, 30),batch=self._batch)
        rect.anchor_position=(rect.width/2,rect.height/2)
        #c=shapes.Circle(sx, sy,1,color=(5, 245, 13),batch=self._batch)
        c=shapes.Rectangle(sx, sy,self.cell_side/2 ,2,color=(255, 245, 235),batch=self._batch)
        c.anchor_position=(0,0)
        ang=atan2(sp[2],sp[3])
        
        self.rotate(ang, rect,True)
        self.rotate(ang, c,False)
        self._lines.append((c,rect))

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
        
    def rotate(self,ang:float, shape:shapes.Rectangle,auto_color=False):
        d=round(ang*180.0/pi)
        d= (d+360)%360
        shape.rotation=0-d
        if not auto_color:
            return
        slop=tan(ang)
        try:
            result = exp(-slop)
        except OverflowError:
            result = inf
        k=1.0/(1.0+result)
        n =round(k*(self.N_COLORS-1))
        shape.color=self._colors[n]

    def get_pos_by_indexs(self,row:int,col:int):
        px=self.x_axis.value_at(col)
        py=self.y_axis.value_at(row)
        return (px,py)


        


