from typing import Dict,List
from ..core import View
from ..demos import *
from ..core.sample_point import *
from .grid import Grid
from .tip import Tip
# from .pole import Pole
# from .pilot import Pilot
CASES:List[Space]=[FALL] #,SPRING,FISH,PENDULUM,
def get_views()->Dict[str,List[View]]:
    return  {
    'Fall':[Grid(FALL),Tip(FALL)],#,'time velocity'
    # 'Fish':[Grid(FISH),Ball(FISH)],
    # 'Pendulum':[Grid(PENDULUM),Ball(PENDULUM),Pole(PENDULUM)],
    # 'Spring':[Pilot(SPRING)]
}