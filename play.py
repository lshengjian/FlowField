from omegaconf import OmegaConf
import numpy as np
from omegaconf import OmegaConf,DictConfig
from sympy import symbols, sympify, lambdify
import matplotlib.pyplot as plt
from matplotlib.colors import Normalize
from matplotlib.cm import ScalarMappable

def load_config(fname='app.yaml')->DictConfig:
    cfg = OmegaConf.load(fname)
    return cfg

def show(title,xname,yname,X,Y,U,V):
    # 计算矢量的大小
    magnitude = np.sqrt(U**2 + V**2)

    # 归一化矢量的大小
    norm = Normalize(magnitude.min(), magnitude.max())

    # 创建颜色映射对象
    cmap = plt.cm.coolwarm

    # 创建一个ScalarMappable对象，用于颜色映射和颜色条
    sm = ScalarMappable(norm=norm, cmap=cmap)

    # 将归一化的大小映射到颜色映射中
    colors = [sm.to_rgba(m) for m in magnitude.ravel()]

    # 创建图形和轴
    _, ax = plt.subplots()

    # 绘制矢量场，为每个箭头指定颜色
    ax.quiver(X, Y, U/magnitude, V/magnitude, color=colors)

    # 显示图形
    plt.xlabel(xname)
    plt.ylabel(yname)
    plt.title(title)
    plt.show()

def main(cfg,pname='P1'):
    N=cfg.cells_side
    p=cfg.problems[pname]
    x1,x2=p.X.range
    y1,y2=p.Y.range
    x = np.linspace(x1,x2, N)
    y = np.linspace(y1,y2, N)
    X, Y = np.meshgrid(x, y)

    x, y = symbols('X Y')
    u=sympify(p.U)
    v=sympify(p.V)
    func1 = lambdify((x,y), u, 'numpy')
    func2 = lambdify((x,y), v, 'numpy')
    U=func1(X,Y)
    V=func2(X,Y)
    show(p.desc,p.X.name,p.Y.name,X,Y,U,V)

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
    main(cfg,'P2')
