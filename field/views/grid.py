from typing import Tuple
from pyglet import shapes,graphics
from pyglet.text import Label

from field.utils import linear_gradient
from math import pi,atan2,tan,exp,inf
from .view import View
class Grid(View):
    #N_COLORS:int = 8
      
    def on_click(self,sx,sy):
        if sx<self._ox or sy<self._oy or sx>self._ox+self.w or sy>self._oy+self.h:
            return
        x,y=self.get_space_pos(sx,sy)
        self._space.ball_pos=[x,y]

    def render(self):
        x,y=self._space.ball_pos
        x,y=self.get_screen_pos(x,y)
        self._ball.position=[x,y]
        super().render()


    def reset(self):
        #self._colors=linear_gradient('#0000FF','#FF4500',self.N_COLORS)
        w,h=self._viewport.size
        x,y=self._space.ball_pos
        x,y=self.get_screen_pos(x,y)
        self._ball=shapes.Circle(x,y,6,color=(255, 255, 0),batch=self._batch)
        self._lines=[]
        N=self.cfg.cells_side
        dx=(self._space.x_limit[1]-self._space.x_limit[0])/N
        dy=(self._space.y_limit[1]-self._space.y_limit[0])/N

        for i in range(N):
            for j in range(N):
                x=self._space.x_limit[0]+j*dx
                y=self._space.y_limit[0]+i*dy
                x1,y1=self._space.next_pos(x,y,1.2)
                self.add_line_segment(x,y,x1,y1)

    
    def add_line_segment(self,x,y,x1,y1): 
        x,y=self.get_screen_pos(x,y)
        x2,y2=self.get_screen_pos(x1,y1)
        k=0.618
        x1=x*(1-k)+x2*k
        y1=y*(1-k)+y2*k
        line1=shapes.Line(x,y,x1,y1,color=(223, 223, 223),batch=self._batch)
        line2=shapes.Line(x1,y1,x2,y2,color=(250, 50, 34),batch=self._batch)

        self._lines.append((line1,line2))







        



