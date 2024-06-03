from typing import Tuple
from pyglet import shapes,graphics
from pyglet.text import Label

from field.utils import linear_gradient
from math import pi,atan2,tan,exp,inf
from .view import View
class Grid(View):
    N_COLORS:int = 8
      

    # def set_data(self,state:State,x:float,y:float):
    #     idx_x=self.sp._x_index
    #     idx_y=self.sp._y_index
    #     data=list(state)
    #     data[idx_x]=x
    #     data[idx_y]=y
    #     state.set_data(*data)


    def reset(self):
        self._colors=linear_gradient('#0000FF','#FF4500',self.N_COLORS)
        w,h=self._viewport.size
        self._body=shapes.Circle(w/2,h/2,6,color=(255, 255, 0),batch=self._batch)
        self._lines=[]
        N=self.cfg.cells_side
        dx=(self._space.x_limit[1]-self._space.x_limit[0])/N
        dy=(self._space.y_limit[1]-self._space.y_limit[0])/N

        for i in range(N):
            for j in range(N):
                x=self._space.x_limit[0]+j*dx
                y=self._space.y_limit[0]+i*dy
                x1,y1=self._space.move(x,y)
                self.add_line_segment(x,y,x1,y1)

    
    def add_line_segment(self,x,y,x1,y1): #sp:(row,col,slop)
        x,y=self.get_screen_pos(x,y)
        x1,y1=self.get_screen_pos(x1,y1)
        line=shapes.Line(x,y,x1,y1,color=(50, 45, 30),batch=self._batch)

        # rect=shapes.Rectangle(sx, sy,self.cells_side ,2,color=(50, 45, 30),batch=self._batch)
        # rect.anchor_position=(rect.width/2,rect.height/2)
        # #c=shapes.Circle(sx, sy,1,color=(5, 245, 13),batch=self._batch)
        # c=shapes.Rectangle(sx, sy,self.cells_side/2 ,2,color=(255, 245, 235),batch=self._batch)
        # c.anchor_position=(0,0)
        # ang=atan2(sp[2],sp[3])
        
        # self.rotate(ang, rect,True)
        # self.rotate(ang, c,False)
        self._lines.append(line)

    # def on_click(self,sx,sy):
    #     x,y=self.get_space_pos(sx,sy)
    #     data=list(self.sp.state)
    #     data[self.sp._x_index]=x
    #     data[self.sp._y_index]=y
    #     self.sp.state.set_data(*data)


    # def update(self):
    #     self.sp.update()
    #     px=self.sp.state.value(self.x_axis.name)
    #     py=self.sp.state.value(self.y_axis.name)
    #     x,y=self.get_pos(px,py)
    #     self._body.position=(x,y)            
        
    # def rotate(self,ang:float, shape:shapes.Rectangle,auto_color=False):
    #     d=round(ang*180.0/pi)
    #     d= (d+360)%360
    #     shape.rotation=0-d
    #     if not auto_color:
    #         return
    #     slop=tan(ang)
    #     try:
    #         result = exp(-slop)
    #     except OverflowError:
    #         result = inf
    #     k=1.0/(1.0+result)
    #     n =round(k*(self.N_COLORS-1))
    #     shape.color=self._colors[n]

    # def get_pos_by_indexs(self,row:int,col:int):
    #     px=self.x_axis.value_at(col)
    #     py=self.y_axis.value_at(row)
    #     return (px,py)


        



