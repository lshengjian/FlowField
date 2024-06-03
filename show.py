import numpy as np
from omegaconf import OmegaConf,DictConfig
from sympy import symbols, sympify, lambdify,sin,cos
from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
from scipy.interpolate import interp2d
from matplotlib.colors import Normalize
from matplotlib.cm import ScalarMappable


ball_x = 0.5
ball_y = 0.5

def load_config(fname='conf/app.yaml')->DictConfig:
    cfg = OmegaConf.load(fname)
    problem_config = f"conf/problems/{cfg.problem}.yaml"

    problem_config = OmegaConf.load(problem_config)
    cfg = OmegaConf.merge(cfg, problem_config)

    print(OmegaConf.to_yaml(cfg))
    return cfg

def show(cfg,x,y,X,Y,U,V):
    global ball_x, ball_y
    title,xname,yname=cfg.desc,cfg.X[0],cfg.Y[0]
    x1,x2=cfg.X[1:3]
    y1,y2=cfg.Y[1:3]
    
    u_interp = interp2d(x, y, U*np.ones_like(V), kind='linear')
    v_interp = interp2d(x, y, V, kind='linear')
    ball_x=x1+(x2-x1)*cfg.ball_pos[0]
    ball_y=y1+(y2-y1)*cfg.ball_pos[1]
    
    step=(x2-x1)/cfg.cells_side/2,(y2-y1)/cfg.cells_side/2

    magnitude = np.sqrt(U**2 + V**2)
    norm = Normalize(magnitude.min(), magnitude.max())
    cmap = plt.cm.coolwarm
    sm = ScalarMappable(norm=norm, cmap=cmap)
    colors = [sm.to_rgba(m) for m in magnitude.ravel()]
    fig, ax = plt.subplots(figsize=(7, 6))

    if cfg.normalize:
        ax.quiver(X, Y, U/magnitude, V/magnitude, color=colors)
    else:
        ax.quiver(X, Y, U, V, color=colors)

    ball, = ax.plot(ball_x, ball_y, 'bo') 

    def update(frame):
        global ball_x, ball_y
        u = u_interp(ball_x, ball_y) 
        v = v_interp(ball_x, ball_y) 
        dis=np.sqrt(u**2+v**2)
        ball_x += u/(dis+1e-10) * step[0]
        ball_y += v/(dis+1e-10) * step[1]
        ball_x = np.clip(ball_x, min(x), max(x))
        ball_y = np.clip(ball_y, min(y),  max(y))
        ball.set_data(ball_x, ball_y)
        return ball,
    plt.xlabel(xname)
    plt.ylabel(yname)
    plt.title(title)
    ani = FuncAnimation(fig, update, frames=np.linspace(0, 1, cfg.animate_time*1000//16), blit=True,interval=16)
    plt.show()

def main(cfg):
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
    show(cfg,xs,ys,X,Y,U,V)


if __name__ == '__main__':
    cfg=load_config()
    main(cfg)
