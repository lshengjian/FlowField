from numba import jit

@jit
def F1(z:complex):
  return 1+z.real-z.imag

@jit
def F2(z:complex):
  x,y=z.real,z.imag
  return x**2-y**2
