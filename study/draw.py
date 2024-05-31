import pyglet
from pyglet.text import Label
import imgui
from pyglet.window import key
from imgui.integrations.pyglet import create_renderer
from pyglet import shapes,graphics
from math import cos,sin,sqrt
from random import randint
cs=[]
selectNumColor=[6,44,710]
COL_INDEX=0
W,H=800,800
FPS=60
K=0.1
N=2000 
JustPrimer=False


def make_colors(num_colors):
    cs.clear()
    for i in range(num_colors):
        c=(randint(0,256),randint(0,256),randint(0,256))
        cs.append(c)

def isPrimer(n):
    for i in range(2,round(sqrt(n)+1)):
        if n>2 and n%i==0 :
            return False
    return True

def make_points(batch,ps):
    global K,N
    ps.clear()
    for i in range(2,N+1):
        flag=isPrimer(i)
        if JustPrimer and not flag:
            continue
        r=2 if flag else 1
        x,y=W//2+i*cos(i)*K, H//2+i*sin(i)*K
        val_colors=selectNumColor[COL_INDEX]
        circle = shapes.Circle(x=x,y=y,radius=r,color=cs[i%val_colors],batch=batch)
        ps.append(circle)

def update(batch,ps):
    global val_colors,K,N,JustPrimer

    imgui.new_frame()
    imgui.begin("MyGame")
    changed, N = imgui.slider_int("N", N, min_value = 3, max_value = 9000)
    changed1, JustPrimer = imgui.checkbox(
            "Only Show Primer", # Label
            JustPrimer # Input current state
        )
    if changed or changed1 :
        K=min(W,H)/(2*N)
        make_colors(selectNumColor[COL_INDEX])
        make_points(batch,ps)
    imgui.end()


def main():
    window = pyglet.window.Window(width=W, height=H)
    @window.event
    def on_key_press(symbol, modifiers):
        global COL_INDEX
        if symbol==key.TAB :
            COL_INDEX=(COL_INDEX+1)%len(selectNumColor)
            tip.text=str(selectNumColor[COL_INDEX])
            make_colors(selectNumColor[COL_INDEX])
            make_points(batch,ps)

    batch=graphics.Batch()
    tip=Label('press TAB change colors',font_size=18,color=(5,235,28,210),x=20,y=H-40,batch=batch)
    imgui.create_context()
    impl = create_renderer(window)

    ps=[]
    make_colors(selectNumColor[COL_INDEX])
    make_points(batch,ps)

        
    def draw(dt):
        update(batch,ps)
        window.clear()
        batch.draw()
        imgui.render()
        impl.render(imgui.get_draw_data())

    pyglet.clock.schedule_interval(draw, 1 / FPS)
    pyglet.app.run()


if __name__ == "__main__":
    main()