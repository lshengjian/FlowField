from omegaconf import OmegaConf
import numpy as np
from omegaconf import OmegaConf,DictConfig
from sympy import symbols, sympify, lambdify
from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
from scipy.interpolate import interp2d
from matplotlib.colors import Normalize
from matplotlib.cm import ScalarMappable
# 初始化小球的位置
ball_x = 0.5
ball_y = 0.5
def load_config(fname='conf/app.yaml')->DictConfig:
    cfg = OmegaConf.load(fname)
    problem_config = f"conf/problems/{cfg.problem}.yaml"

    # 将数据库配置文件的内容合并到主配置中
    problem_config = OmegaConf.load(problem_config)
    cfg = OmegaConf.merge(cfg, problem_config)

    # 现在 config 中包含了主配置和数据库配置
    print(OmegaConf.to_yaml(cfg))
    return cfg

def show(cfg,x,y,X,Y,U,V):
    global ball_x, ball_y
    title,xname,yname=cfg.desc,cfg.X.name,cfg.Y.name
    
    # 创建插值函数
    u_interp = interp2d(x, y, U*np.ones_like(V), kind='linear')
    v_interp = interp2d(x, y, V, kind='linear')
    ball_x,ball_y=x[0],y[-1]
    step=(x[-1]-x[0])/cfg.cells_side/2,(y[-1]-y[0])/cfg.cells_side/2
    #print('ball pos:',ball_x,ball_y)

    # 计算矢量的大小
    magnitude = np.sqrt(U**2 + V**2)

    # 归一化矢量的大小
    norm = Normalize(magnitude.min(), magnitude.max())

    # 创建颜色映射对象
    cmap = plt.cm.coolwarm

    # # 创建一个ScalarMappable对象，用于颜色映射和颜色条
    sm = ScalarMappable(norm=norm, cmap=cmap)
    colors = [sm.to_rgba(m) for m in magnitude.ravel()]

    # 创建图形和轴
    fig, ax = plt.subplots(figsize=(7, 6))

    # 绘制矢量场，为每个箭头指定颜色
    if cfg.normalize:
        ax.quiver(X, Y, U/magnitude, V/magnitude, color=colors)
    else:
        ax.quiver(X, Y, U, V, color=colors)
    #

    ball, = ax.plot(ball_x, ball_y, 'bo')  # 'bo' 表示蓝色圆点

    def update(frame):
        global ball_x, ball_y
        # 使用插值函数获取当前位置的矢量分量
        u = u_interp(ball_x, ball_y) 
        v = v_interp(ball_x, ball_y) 
        # 更新小球的位置
        dis=np.sqrt(u**2+v**2)
        ball_x += u/(dis+1e-10) * step[0]
        ball_y += v/(dis+1e-10) * step[1]
        # 确保小球不会离开绘图区域
        ball_x = np.clip(ball_x, min(x), max(x))
        ball_y = np.clip(ball_y, min(y),  max(y))
        ball.set_data(ball_x, ball_y)
        return ball,
    # 显示图形
    plt.xlabel(xname)
    plt.ylabel(yname)
    plt.title(title)
    ani = FuncAnimation(fig, update, frames=np.linspace(0, 1, cfg.animate_time*1000//16), blit=True,interval=16)
    plt.show()

def main(cfg):
    N=cfg.cells_side
    # pname=cfg.show
    # p=cfg.problems[pname]
    x1,x2=cfg.X.range
    y1,y2=cfg.Y.range
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
            ds.append(cfg.args[arg])

    func1 = lambdify((x,y,*ks), u, 'numpy')
    func2 = lambdify((x,y,*ks), v, 'numpy')
    U=func1(X,Y,*ds)
    V=func2(X,Y,*ds)
    show(cfg,xs,ys,X,Y,U,V)

# def check_config(cfg):
#     print(cfg.cells_side)
#     print(list(cfg.problems.keys()))
#     print(cfg.problems.P1.X)
#     print(cfg.problems.P1.U)
#     print(cfg.problems.P1.args[0])

# def demo_exp():
#     # 定义符号变量
#     x = symbols('x')

#     # 用户输入的表达式字符串，例如 "k*np.cos(x)"
#     expr_str ='k*sin(x)'# input("请输入表达式（例如 'k*np.cos(x)'）：")

#     # 解析字符串为Sympy表达式
#     expr = sympify(expr_str)
#     expr = expr.subs('k', 0.5)

#     # 创建一个numpy数组
#     x_values = np.linspace(0, 2*np.pi, 3)  # 从0到2π的100个点
#     func = lambdify(x, expr, 'numpy')
#     # 计算结果
#     result = func(x_values)

#     # 打印结果
#     print("计算结果：", result)    
if __name__ == '__main__':
    cfg=load_config()
    main(cfg)
