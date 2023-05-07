import  sys
from os import path
dir=path.abspath(path.dirname(__file__) + './..')
sys.path.append(dir)
from phase_space.utils import Bound
from phase_space.core.field import Field,Measure
from phase_space.core import VelocityDemo
def test_measure():
   m1=Measure('time',Bound(0,10),11)
   ds=list(m1)
   assert 11==len(ds)
   assert 0==ds[0] and 10==ds[10]
   assert 1==ds[1] 

def test_field():
   m1=Measure('time',Bound(0,3),4)
   m2=Measure('velocity',Bound(0,3),4)
   demo=VelocityDemo(m1,m2)
   ds=list(demo)
   assert 4*4==len(ds)
   assert (0,0,10)==ds[0]
   assert (3,3,4)==ds[15]

  
  
    




    