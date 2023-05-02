from IMGUI import *
from utilities import *
left_slider=0.0
GRID_SIZE=32
TILE_SIZE=vec2(32,32)

_left_area = rect(0, 0, 100, 20)
       
def gui_hit( position):
    return region_hit(_left_area, position) 
def draw(imgui,s):
    global left_slider
    imgui.begin(s)
    left_slider = imgui.slider(1, left_slider, rect(10, 10, 80, 20),80)
    imgui.end()

def handle(imgui,event):
    if (event.type == MOUSEBUTTONUP or event.type == MOUSEBUTTONDOWN or event.type == MOUSEMOTION) and gui_hit(vec2(event.pos)):
        imgui.on_event(event)
    elif event.type == KEYDOWN or event.type == KEYUP:
        imgui.on_event(event)
    else:
        return False
    return True
if __name__ == "__main__":
    screen=initialize_pygame(vec2(800, 600), False)
    imgui = IMGUI(pygame.font.SysFont("Consolas", 16))
    done = False
    clock = pygame.time.Clock()


    while not done:
        # This limits the while loop to a max of 60 times per second.
        # Leave this out and we will use all CPU we can.
        clock.tick(60)

        for event in pygame.event.get():  # User did something
            if event.type == pygame.QUIT:  # If user clicked close
                done = True  # Flag that we are done so we exit this loop
            else:
                handle(imgui,event)
        #screen.fill("white")
        draw(imgui,screen)

