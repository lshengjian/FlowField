import  sys
from os import path
dir=path.abspath(path.dirname(__file__) + './..')
sys.path.append(dir)
from field.utils import Bound,linear_gradient,RGB_to_hex

def test_bound():
    b1=Bound()
    assert 1==b1.distance
    b2=Bound(-1,1)
    assert 2==b2.distance
    b3=Bound(-100,100)
    assert 200==b3.distance

def test_linear_gradient():
    cs=linear_gradient('#100000','#300000',3)
    assert 3==len(cs)
    assert '#100000'==RGB_to_hex(cs[0]) and '#300000'==RGB_to_hex(cs[2])
    assert '#200000'==RGB_to_hex(cs[1])