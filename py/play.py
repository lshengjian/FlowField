import pygame
from pygame import Vector2
from myfun import slop,linear_gradient
from random import randrange


FPS=30

w,h=800,600
hw,hh=w//2,h//2
N=20
step=0.05
def p2c(x,y):
    return (hw*(1+x),hh*(1-y))

def c2p(x,y):
    return ((x-hw)/hw,(hh-y)/hh)


CS=linear_gradient("#0000FF","#FF0000",100)


class Ball:
    p:Vector2
    screen:pygame.surface=None

    def __init__(self,s,x0,y0):
        self.p=Vector2(x0,y0)
        self.screen=s

    def move(self):
        x,y=self.p
        if x>1:
            x=-1
        s=slop(self.p)
        x1,y1=x+step,y+step*s
        self.p=Vector2(x1,y1)

    def draw(self):
        x,y=self.p
        x,y=p2c(x,y)
        pygame.draw.circle(self.screen, "red", [x, y], 6)


class Point:
    p:Vector2
    screen:pygame.surface=None

    def __init__(self,s,a,b):
        self.p=Vector2(a,b)
        self.screen=s

    def draw(self):
        x,y=self.p
        s=slop(self.p)
        x1,y1=x+step,y+step*s
        x,y=p2c(x,y)
        x1,y1=p2c(x1,y1)
       
        #pygame.draw.circle(self.screen, "blue", [x, y], 2)
        c=CS[0]#randrange(0,len(CS))

        pygame.draw.aaline(self.screen,c, [x,y], [x1, y1], True)

    
def main():
    #global cnt
    # Initialize pygame
    pygame.init()
    

    # Set the height and width of the screen
    size = [w, h]
    screen = pygame.display.set_mode(size)
    ps=[]
    ball =Ball(screen,-1,0.5)

    for i in range(1,N):
        for j in range(1,N):
            ps.append(Point(screen,2*(i-N//2)/N,2*(j-N//2)/N))

    pygame.display.set_caption("Example code for the draw module")

    # Loop until the user clicks the close button.
    done = False
    clock = pygame.time.Clock()

    while not done:
        # This limits the while loop to a max of 60 times per second.
        # Leave this out and we will use all CPU we can.
        clock.tick(FPS)
        #cnt+=0.016

        for event in pygame.event.get():  # User did something
            if event.type == pygame.QUIT:  # If user clicked close
                done = True  # Flag that we are done so we exit this loop
            elif event.type == pygame.MOUSEBUTTONDOWN: 
                pos=pygame.mouse.get_pos()
                x,y=pos
                x,y=c2p(x,y)
                ball =Ball(screen,x,y)
        # Clear the screen and set the screen background
        screen.fill("white")
        for p in ps:
            p.draw()
        ball.move()
        ball.draw()
        

        pygame.display.flip()

if __name__ == "__main__":
    main()
    pygame.quit()