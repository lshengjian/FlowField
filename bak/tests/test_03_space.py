import  sys
from os import path
dir=path.abspath(path.dirname(__file__) + './..')
sys.path.append(dir)
from phase_space.core import State
from phase_space.demos.fall import FALL

def test_space():
    names=FALL.names
    assert 2==len(names) and 'time'==names[0] and 'velocity'==names[1]
    time=FALL.get_measure('time')
    assert time.bound.distance==(time.bound.high-time.bound.low)

    assert time.bound.limit(11)==0

    state=FALL.get_state_zero()
    assert 0==state.time and 0==state.velocity

    state.set_data(1,1.23)
    assert 1==state.time and 1.23==state.velocity

    acc=FALL.constraint(state)
    assert acc>0

def test_clone():
    state=FALL.get_state_zero()
    s2=state.set_data(11,22)
    assert 11==s2.time and 22==s2.velocity
    