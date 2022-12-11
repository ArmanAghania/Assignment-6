import turtle



colors = ["purple", "blue", "green", "yellow", "orange", "red"]

turtle.bgcolor('black')
turtle.speed(0)

for i in range(360):
    turtle.pencolor(colors[i%6])
    turtle.width(i/100 + 1)
    turtle.forward(i)
    turtle.left(59)

turtle.done()




