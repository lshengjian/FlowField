import  sys
from os import path
dir=path.abspath(path.dirname(__file__) + './..')
sys.path.append(dir)

from field.utils import load_config,get_config
from field import Space

def test_space():
    names=load_config()
    assert '01_fall'==names[0]
    cfg=get_config(names[0])
    fd=Space(cfg)
    assert 'time'==fd.x_name
    assert 'speed'==fd.y_name
    x,y=fd.ball_pos
    x1,y1=fd.move(x,y)
    assert x1>x and y1<y

    
    



    