import pygame

from flowfield.utils import linear_gradient
from flowfield.Ball import Ball
from flowfield.Grid import Grid
from flowfield.demos import F2 as F

FPS=60
step=0.02
N=40
W,H=800,800
SIZE=H//N

X_MIN,X_MAX=-2,2
Y_MIN,Y_MAX=-4,4
kw=W/(X_MAX-X_MIN)
kh=H/(Y_MAX-Y_MIN)

def toMath(x,y):
    return (X_MIN+x/kw,Y_MIN+(H-y)/kh)

def toScreen(x,y):
    return (kw*(x-X_MIN),H-kh*(y-Y_MIN))

CS=linear_gradient("#0000FF","#FF0000",100)

    
def main():
    pygame.init()
    size = [W, H]
    screen = pygame.display.set_mode(size)
    ball =Ball(X_MIN,Y_MAX/2,X_MIN,X_MAX)
    grid =Grid(F,(X_MIN,X_MAX),(Y_MIN,Y_MAX),N)

    pygame.display.set_caption("Example code for the draw module")
    done = False
    clock = pygame.time.Clock()

    while not done:
        clock.tick(FPS)

        for event in pygame.event.get():  # User did something
            if event.type == pygame.QUIT:  # If user clicked close
                done = True  # Flag that we are done so we exit this loop
            elif event.type == pygame.MOUSEBUTTONDOWN: 
                pos=pygame.mouse.get_pos()
                x,y=pos
                x,y=toMath(x,y)
                ball.reset(x,y)
        # Clear the screen and set the screen background
        screen.fill("white")
        draw_grid(screen, grid)
        ball.move(F,step)
        
        draw_ball(screen, ball)
        

        pygame.display.flip()

def draw_line(screen,x,y,k):
    x1,y1=x+step,y+step*k
    x,y=toScreen(x,y)
    x1,y1=toScreen(x1,y1)
    c=CS[0]#randrange(0,len(CS))
    pygame.draw.aaline(screen,c, [x,y], [x1, y1], True)

def draw_grid(screen, grid):
    for i in range(1,N):
        for j in range(1,N):
            x,y=toMath(j*SIZE,i*SIZE)
            draw_line(screen,x,y,grid.slop(i,j))

def draw_ball(screen, ball):
    x,y=toScreen(ball.pos.real,ball.pos.imag)
    pygame.draw.circle(screen, "red", [x, y], 6)

if __name__ == "__main__":
    main()
    pygame.quit()