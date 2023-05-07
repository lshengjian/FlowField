from typing import Dict
from pyglet.math import Vec2
from math import sin

def F1(p:Vec2,time:float,args:Dict[str,float]):
  return 1+p.x-p.y


def F2(p:Vec2,time:float,args:Dict[str,float]):
  x,y=p.x,p.y
  return x**2-y**2


def F3(p:Vec2,time:float,args:Dict[str,float]):
  x,y=p.x,p.y
  return -args['K1']*sin(x)-args['K2']*y