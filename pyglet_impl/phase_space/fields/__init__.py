from .air_drag import *
from .fish import *
from .pendulum import *
from .spring  import *
from .star import *
from ..core import Bound,Measure

FALL=AirDrag(Measure('time',Bound(0,10),41),Measure('velocity',Bound(3,7),41))
FISH=Fish(Measure('time',Bound(0,10),41),Measure('fish num',Bound(-0.5,3.5),41))
PENDULUM=Pendulum(Measure('theta',Bound(-10,10),33),Measure('omiga',Bound(-8,8),33),True)



# STAR=Star(Measure('time',Bound(0,10),11),Measure('velocity',Bound(-4,4),11))

# SPRING=Spring(Measure('pos',Bound(-1,1),21),Measure('velocity',Bound(-2,2),21),True)


