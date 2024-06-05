import  sys
from os import path
dir=path.abspath(path.dirname(__file__) + './..')
sys.path.append(dir)

from src.utils import load_config,get_config
from src import Space

def test_space():
    names=load_config()
    assert '01_fall'==names[0]
    cfg=get_config(names[0])
    space=Space(cfg)
    assert 'time'==space.x_name
    assert 'speed'==space.y_name
    x,y=space.ball_pos
    x1,y1=space.next_pos_dir(x,y)
    assert x1>x and y1<y

    
    



    