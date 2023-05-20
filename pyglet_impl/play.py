import pyglet
from phase_space.app import App
from config import demo_names,make_views,WIDTH,HEIGHT,FPS,TITLE
CFG={
    'WIDTH':WIDTH,
    'HEIGHT':HEIGHT,
    'FPS':FPS,
    'TITLE':TITLE,
    'demo_names':demo_names,
    'make_views':make_views,
}
def main():
    App(CFG)
    pyglet.app.run()

if __name__ == "__main__":
    main() #git push origin --tags
