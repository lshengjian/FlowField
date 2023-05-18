from typing import List,Dict
from phase_space.core import Measure,Bound,View
from phase_space.demos import *
from phase_space.views import *

WIDTH=1024
HEIGHT=600
cache_space={}
cache_view={}
def get_space(name):
    if name not in cache_space:
        cache_space[name]=make_space(name,*args[name])
    return cache_space[name]

def make_views(name)->Dict[str,List[View]]:
    space=get_space(name)
    vs=None
    if name not in cache_view:
        if 'Spiral'==name:
            vs=[Contour(space,axis='x y'),Tip(space,axis='x y')]
        elif name in('Fish','Fall') :
            vs=[Grid(space),Tip(space)]
        elif 'Spring'==name:
            vs=[Pilot(space),Tip(space)]
        elif 'Pendulum'==name:
            vs=[Grid(space),Pole(space),Tip(space)] 
        cache_view[name]=vs
    return space,cache_view[name]


args={
    'Fall':([Measure('time',Bound(0,10),41),Measure('velocity',Bound(3,7),41)],True),
    'Fish':([Measure('time',Bound(0,10),41),Measure('amount',Bound(-1,7),41)],True),
    'Spiral':([
        Measure('time',Bound(0,6),101),
        Measure('x',Bound(-5,5),101), 
        Measure('y',Bound(-5,5),101),
        Measure('z',Bound(0,1),2)
        ],True),
    'Spring':([
        Measure('time',Bound(0,8),101),
        Measure('pos',Bound(-2,2),101),
        Measure('velocity',Bound(-4,4),101)
        ],True),
    'Pendulum':([
        Measure('angle',Bound(-10,10),33),
        Measure('angle_velocity',Bound(-8,8),33)
        ],False)
    
}
   
if __name__ == "__main__":
    print(demo_names)
    space=get_space(demo_names[0])
    print(space.name)