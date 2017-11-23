# circle bounce

# create a window and draw it
# create a circle and draw it
# initialize a dx and dy
# for i in 10000 move the circle dx,dy
# if x > screen right edge change dx to -1
# if x < 0 change dx to 1
# if y > bottom of screen change dy to -1
# if y < 0 change dy to 1
# slow update speed

from graphics import *

def main():

    win = GraphWin("Circle Bounce",300,300)
    win.setBackground('white')

    r = 10

    circle = Circle(Point(150,150),r)
    circle.draw(win)

    dx = 2
    dy = 1

    for i in range(10000):
        
        x = circle.getCenter().getX()
        y = circle.getCenter().getY()
        
        if x > 300 - r or x < 0 + r:
            dx *= -1
        if y > 300 - r or y < 0 + r:
            dy *= -1
            
        circle.move(dx,dy)
        update(120)

main()

    
