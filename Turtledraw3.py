def first_angle(n): # firat_external_angle
    teta=90*(n+2)/n
    return(teta)

n=2
space=10
from turtle import *
shape("turtle")
while n<360:
    n +=1
    left(first_angle(n))

    for i in range(n):
        fd(40+(n-3)*4/n*space)
        left(360/n)
    left(-first_angle(n))
    up()
    setpos(space*(n-2),0)
    down()
    
done()