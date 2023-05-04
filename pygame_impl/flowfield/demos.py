from numba import jit
from math import cos,sin
CONFIG={
  'K1':2,
  'K2':1
}
@jit
def F1(z:complex):
  x,y=z.real,z.imag
  return 1+x-y

@jit
def F2(z:complex):
  x,y=z.real,z.imag
  return x**2-y**2

@jit
def F3(z:complex):
  x,y=z.real,z.imag
  return -CONFIG['K1']*sin(x)-CONFIG['K2']*y