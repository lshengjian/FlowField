from typing import Dict,List
from ..core import View
from ..fields import *
from ..core.sample_point import *
from .grid import Grid
# from .ball import Ball
from .pole import Pole
from .pilot import Pilot
CASES:List[Field]=[FALL] #,SPRING,FISH,PENDULUM,
def get_views()->Dict[str,List[View]]:
    return  {
    'AirDrag':[Grid(FALL)],
    # 'Fish':[Grid(FISH),Ball(FISH)],
    # 'Pendulum':[Grid(PENDULUM),Ball(PENDULUM),Pole(PENDULUM)],
    # 'Spring':[Pilot(SPRING)]
}