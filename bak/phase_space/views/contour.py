from math import pi
from pyglet import shapes
from ..core import *
from math import exp
class Contour(View):
    N_COLORS:int = 8
    def reset(self,cfg):
        super().reset(cfg)
        self._colors=linear_gradient('#0000FF','#FF0000',self.N_COLORS)
        names=self._space.names
        self.t_axis=self._space.get_measure(names[0])
        self.x_axis=self._space.get_measure(names[1])
        self.y_axis=self._space.get_measure(names[2])
        w,h=self._viewport.size
        ns=self.t_axis.num_sampling
        #DX=self.t_axis.bound.distance/(ns-1)
        step=self._space.arg_value('step')#DX/10#
        self._ps=[]
        self.add_line(step)

    def add_line(self,step):
        time_bound=self.t_axis.bound
        x_bound=self.x_axis.bound
        y_bound=self.y_axis.bound
        
        state=self._space.get_state_zero()
        
        t=0
        dx=0
        while t<time_bound.high:
            self._space.constraint(state)
            x,y=self.get_pos(state[1],state[2])
            d=2*(1/(1+exp(-state[3]))-0.5)  #0~1
            c=self._colors[round(d*(self.N_COLORS-1))]
            self._ps.append(shapes.Circle(x,y,2,color=c,batch=self._batch))
            t,*_=state 
            t=t+step
            state.set_data(t,0,0,0)

                





    


       

