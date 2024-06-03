from field.utils import load_config,get_config
from field import Space

if __name__ == "__main__":
    names=load_config()
    assert '01_fall'==names[0]
    cfg=get_config(names[0])
    fd=Space(cfg)
    assert 'time'==fd.x_name
    assert 'speed'==fd.y_name
    print(fd.ball_pos)
    x,y=fd.ball_pos
    print(fd.move(x,y))