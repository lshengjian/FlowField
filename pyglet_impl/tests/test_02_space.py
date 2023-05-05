import  sys
from os import path
dir=path.abspath(path.dirname(__file__) + './..')
sys.path.append(dir)
from phase_space import Space
from pyglet.math import Vec2

def test_space():
   space=Space(start=Vec2(0,0),end=Vec2(1,1),offset=Vec2(0.5,0.5))
   assert 9==len(list(space))
   for sp in space:
      print(sp)

  
  
    




    