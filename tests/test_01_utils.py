import  sys
from os import path
dir=path.abspath(path.dirname(__file__) + './..')
sys.path.append(dir)
from src.utils import linear_gradient,RGB_to_hex


def test_linear_gradient():
    cs=linear_gradient('#100000','#300000',3)
    assert 3==len(cs)
    assert '#100000'==RGB_to_hex(cs[0]) and '#300000'==RGB_to_hex(cs[2])
    assert '#200000'==RGB_to_hex(cs[1])