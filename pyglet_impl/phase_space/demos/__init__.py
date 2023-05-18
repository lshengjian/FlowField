from ..core import Bound,Measure
from .fall import *
from .fish import *
from .pendulum import *
from .spring  import *
from .spiral import *
SPIRAL=Spiral([
    Measure('time',Bound(0,6),101),
    Measure('x',Bound(-5,5),101),
    Measure('y',Bound(-5,5),101),
    Measure('z',Bound(0,1),2)
    ])
FALL=Fall([
    Measure('time',Bound(0,10),41),
    Measure('velocity',Bound(3,7),41)]
    )
FISH=Fish([
    Measure('time',Bound(0,10),41),
    Measure('amount',Bound(-1,7),41)
    ])

SPRING=Spring([
    Measure('time',Bound(0,8),101),
    Measure('pos',Bound(-2,2),101),
    Measure('velocity',Bound(-4,4),101)
    ],False)

PENDULUM=Pendulum([
    Measure('angle',Bound(-10,10),33),
    Measure('angle_velocity',Bound(-8,8),33)
    ],False)


