from .fall import *
from .fish import *
from .pendulum import *
from .spring  import *

from ..core import Bound,Measure

FALL=Fall([
    Measure('time',Bound(0,10),41),
    Measure('velocity',Bound(3,7),41)]
    )
FISH=Fish([
    Measure('time',Bound(0,10),41),
    Measure('amount',Bound(3,7),41)
    ])

SPRING=Spring([
    Measure('time',Bound(0,8),101),
    Measure('pos',Bound(-2,2),101),
    Measure('velocity',Bound(-4,4),101)
    ],False)

PENDULUM=Pendulum([
    Measure('theta',Bound(-10,10),33),
    Measure('omiga',Bound(-8,8),33)
    ],False)

# STAR=Star(Measure('time',Bound(0,10),11),Measure('velocity',Bound(-4,4),11))

