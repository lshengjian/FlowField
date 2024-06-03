from typing import Tuple
import numpy as np
from sympy import symbols, sympify, lambdify
from scipy.interpolate import interp2d

class Space():
    def __init__(
        self,
        cfg
    ):
        self.ball_pos=[0,0]
        self.cfg=cfg
        self.reset()
       
    def reset(self):
        cfg=self.cfg
        N=cfg.cells_side
        x1,x2=cfg.X[1:3]
        y1,y2=cfg.Y[1:3]
        
        xs = np.linspace(x1,x2, N)
        ys = np.linspace(y1,y2, N)
        X, Y = np.meshgrid(xs, ys)

        x, y = symbols('X Y')
        u=sympify(cfg.U)
        v=sympify(cfg.V)
        ks=[]
        ds=[]
        args=cfg.get('args',None)
        if args!=None:
            for arg in cfg.args.keys():
                ks.append(symbols(arg))
                ds.append(cfg.args[arg][1]) #[name,value,min,max]

        func1 = lambdify((x,y,*ks), u, 'numpy')
        func2 = lambdify((x,y,*ks), v, 'numpy')
        U=func1(X,Y,*ds)
        V=func2(X,Y,*ds)
        
        v_interp = interp2d(xs, ys, V, kind='cubic')
        u_interp = interp2d(xs, ys, np.ones_like(V)*U, kind='linear')
        ball_x=x1+(x2-x1)*cfg.ball_pos[0]
        ball_y=y1+(y2-y1)*cfg.ball_pos[1]
        self.ball_pos=[ball_x,ball_y]
        self.u_interp=u_interp
        self.v_interp=v_interp
        self.x_name=cfg.X[0]
        self.y_name=cfg.Y[0]
        self.steps=(x2-x1)/cfg.cells_side/2,(y2-y1)/cfg.cells_side/2
        self.x_limit=(min(xs), max(xs))
        self.y_limit=(min(ys), max(ys))

    def move(self,x,y)->Tuple[int,int]:
        #ball_x,ball_y=self.ball_pos
        u = self.u_interp(x, y) 
        v = self.v_interp(x, y) 
        dis=np.sqrt(u**2+v**2)
        x += u/(dis+1e-10) * self.steps[0]
        y += v/(dis+1e-10) * self.steps[1]
        x = np.clip(x, *self.x_limit)
        y = np.clip(y, *self.y_limit)
        return x,y
'''
    def _update1(self,step):#step is dx
        CS=self._space.constraint
        state=self._state
        data=list(state)
        x1=data[self._x_index]
        y1=data[self._y_index]
        s1=CS(state)
        x2,y2=x1+step,y1+step*s1
        data[self._x_index]=x2
        data[self._y_index]=y2
        state.set_data(*data)
        s2=CS(state)
        x3,y3=x2+step,y2+step*s2
        data[self._x_index]=x3
        data[self._y_index]=y3
        state.set_data(*data)
        s3=CS(state)
        x4,y4=x3+step,y3+step*s3
        data[self._x_index]=x4
        data[self._y_index]=y4
        state.set_data(*data) 
        s4=CS(state)
        s = (s1+s4+2*(s2+s3))/6.0
        return x1+step,y1+step*s

'''