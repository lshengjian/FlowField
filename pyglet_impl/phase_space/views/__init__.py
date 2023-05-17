from typing import Dict,List
from ..core import View
from ..demos import *
from ..core.sample_point import *
from .grid import Grid
from .tip import Tip
from .pole import Pole
from .pilot import Pilot
CASES:List[Space]=[PENDULUM,FALL,FISH,SPRING,] 
def get_views()->Dict[str,List[View]]:
    return  {
    'Fish':[Grid(FISH),Tip(FISH)],
    'Fall':[Grid(FALL),Tip(FALL)],
    
    'Spring':[Pilot(SPRING),Tip(SPRING)],
    'Pendulum':[Grid(PENDULUM),Pole(PENDULUM),Tip(PENDULUM)] #axis='time pos'
}