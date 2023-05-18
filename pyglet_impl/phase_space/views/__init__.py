from typing import Dict,List
from ..core import View
from ..demos import *
from ..core.sample_point import *
from .grid import Grid
from .tip import Tip
from .pole import Pole
from .pilot import Pilot
from .contour import Contour
CASES:List[Space]=[SPIRAL,FALL,FISH,SPRING,PENDULUM]
def get_views()->Dict[str,List[View]]:
    return  {
    'Spiral':[Contour(SPIRAL,axis='x y'),Tip(SPIRAL,axis='x y')],
    'Fish':[Grid(FISH),Tip(FISH)],
    'Fall':[Grid(FALL),Tip(FALL)],
    
    'Spring':[Pilot(SPRING),Tip(SPRING)],
    'Pendulum':[Grid(PENDULUM),Pole(PENDULUM),Tip(PENDULUM)] 
}