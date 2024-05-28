import  sys
from os import path
dir=path.abspath(path.dirname(__file__) + './..')
sys.path.append(dir)
from phase_space.core import State
def test_unpack():
    data=[1,2,3,4]
    print(*data)


def test_state():
    d=State('x y')
    d.set_data(1,2)
    assert 1==d[0] and 2==d[1]
    assert 1==d.value('x') and 2==d.value('y')
    assert [1,2]==list(d)
    assert 1==d.x and 2==d.y

    v2=State('time pos')
    assert [0,0]==list(v2)
    v2.set_data(1.1,2.2)
    assert [1.1,2.2]==list(v2)
    assert 1.1==v2.time and 2.2==v2.pos

    

