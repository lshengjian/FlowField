import  sys
from os import path
dir=path.abspath(path.dirname(__file__) + './..')
sys.path.append(dir)
from phase_space.core import Vector

def test_vector():
    v1=Vector('x,y,z')
    assert [0,0,0]==list(v1)
    v1.set_data(1,2,3)
    assert [1,2,3]==list(v1)
    assert 1==v1.x and 2==v1.y and 3==v1.z
    v2=Vector('time,pos')
    assert [0,0]==list(v2)
    v2.set_data(1.1,2.2,3.3)
    assert [1.1,2.2]==list(v2)
    assert 1.1==v2.time and 2.2==v2.pos
    

