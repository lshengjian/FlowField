import  sys
from os import path
dir=path.abspath(path.dirname(__file__) + './..')
sys.path.append(dir)

from flowfield.demos import F1
from flowfield.Grid import Grid
def test_grid():
    grid=Grid(F1,(-1,1),(-2,2),3)
    assert grid.K[0,0]==1-1-2 and grid.K[2,2]==1+1-(-2)



    