import  sys
from os import path
dir=path.abspath(path.dirname(__file__) + './..')
sys.path.append(dir)
from phase_space.core import Vector
from phase_space.fields import FALL

def test_field():
    ms=FALL.get_sampleing_measures()
    assert 2==len(ms)
    names=FALL.get_measure_names()
    assert 'time,velocity'==names

    state=FALL.get_state_zero()
    assert 0==state.time and 0==state.velocity

    state.set_data(1,1.23)
    assert 1==state.time and 1.23==state.velocity

    acc=FALL.constraint(state)
    assert acc>0
    