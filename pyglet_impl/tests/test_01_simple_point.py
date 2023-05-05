import  sys
from os import path
dir=path.abspath(path.dirname(__file__) + './..')
sys.path.append(dir)
from phase_space import SamplePoint
from pyglet.math import Vec2

def test_stable():
    sp=SamplePoint()
    assert 0==sp.position.x and 0==sp.position.y
    sp.update()
    sp.move()
    assert 0==sp.position.x and 0==sp.position.y

def test_normal():
    sp=SamplePoint(Vec2(1,0))
    assert 1==sp.position.x and 0==sp.position.y
    assert 0==sp.velocity.x and sp.velocity.y<0
    sp.move(dt=0.01)
    assert sp.position.y<0

def test_degree():
    sp=SamplePoint(Vec2(1,1))
    #sp.update()
    assert -70==round(sp.degree)
    sp=SamplePoint(Vec2(-1,1))
    #sp.update()
    assert 34==round(sp.degree)
  
  
    




    