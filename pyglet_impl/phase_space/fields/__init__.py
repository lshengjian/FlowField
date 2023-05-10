from .air_drag import *
from .fish import *
from .pendulum import *
from .spring  import *
from ..core import Bound,Measure


FALL=AirDrag(Measure('time',Bound(0,10),11),Measure('velocity',Bound(3,7),11))
FISH=Fish(Measure('time',Bound(0,10),21),Measure('fish num',Bound(0,4),21))
SPRING=Spring(Measure('pos',Bound(-1,1),21),Measure('velocity',Bound(-2,2),21),True)
PENDULUM=Pendulum(Measure('theta',Bound(-4,7),21),Measure('omiga',Bound(-6,6),21),True)

