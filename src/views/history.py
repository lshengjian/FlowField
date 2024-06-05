
from pyglet import shapes,graphics
from ..space import Space

from .view import View,Viewport
class History(View):
     
    def __init__(self,space:Space,viewPort:Viewport=None):
        super().__init__(space,viewPort)
        N=self._space.trajectory.max_size
        
        kx=self.w/N
        lx=0
        if 'X'==self.cfg.trajectory:
            ky=self.h/(space.x_limit[1]-space.x_limit[0])
            ly=space.x_limit[0]
        else:
            ky=self.h/(space.y_limit[1]-space.y_limit[0])
            ly=space.y_limit[0]

        self._kx,self._ky=kx,ky
        self._lx,self._ly=lx,ly

    def render(self):
        N=self._space.trajectory.max_size
        data=self._space.trajectory.get_data()
        for i,pos in enumerate(data):
            x,y=pos
            y=x if 'X'==self.cfg.trajectory else y
            x,y=self.get_screen_pos(i,y)
            self.cs[i].position=[x,y]
        super().render()


    def reset(self):
        self.cs=[]
        
        w,h=self._viewport.size
        x,y=self._space.ball_pos
        N=self._space.trajectory.max_size
        for i in range(N):
            self.cs.append(shapes.Circle(x,y,1,color=(255, 255, 0),batch=self._batch))
            

    








        



