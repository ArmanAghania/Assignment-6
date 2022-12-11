import turtle

myturtle = turtle.Turtle()
turtle.bgcolor('black')
myturtle.pencolor('red')
myturtle.speed(0)
myturtle.penup()
myturtle.goto(0,200)
myturtle.pendown()

fwdist = 0
dirright = 0

while(True):
    myturtle.forward(fwdist)
    myturtle.right(dirright)
    fwdist += 3
    dirright += 1
    if dirright == 2000:
        break
    myturtle.hideturtle
turtle.done()