import pytest
import random
from math import atan2,pi
parametrize_gamma = pytest.mark.parametrize("gamma",[.1, 0.5, 1.0])
parametrize_n = pytest.mark.parametrize("n", [1, 10, 20])

@pytest.fixture
def eps():
    return 10e-3

@parametrize_gamma
@parametrize_n
def test_parametrize(eps, gamma, n):
    random.seed(eps)
    data=gamma*n
    #print(gamma,n,data) # pytest -s
    assert 0.1<=data<=20  

def test_complex():
    z1=1+1j
    z2=complex(1,1)

    #print(z1)
    assert z1.real==1 and z1.imag==1
    assert z1==z2

    z=complex(3,4)
    assert abs(z)==5
    
def test_math():
    a=atan2(0,0)
    assert 0==a
    a=atan2(0,1)
    assert 0==a
    a=atan2(1,1)
    assert pi/4==a
    a=atan2(1,0)
    assert pi/2==a
    a=atan2(1,-1)
    assert pi/2+pi/4==a
    a=atan2(0,-1)
    assert pi==a
    a=atan2(-1,-1)
    assert -pi/2-pi/4==a
    a=atan2(-1,0)
    assert -pi/2==a
    a=atan2(-1,1)
    assert -pi/4==a
    