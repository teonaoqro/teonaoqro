from turtle import *

#we want to paint a house

#step 1: draw a square
speed(30)
width(7)
color("blue")
begin_fill()
forward(200)
left(90) 

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
end_fill()
#end of square

#drawing a door

forward(70)
color("red")
begin_fill()
left(90)
forward(120)    #height of the door
right(90)
forward(60)
right(90)
forward(120)
end_fill()

penup()
goto(200,200)
pendown()

color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

#drawing a window
penup()
goto(180,180)
color("yellow")
begin_fill()
pendown()
right(60)

forward(40)
left(90)
forward(40)
left(90)
forward(40)
left(90)
forward(40)
end_fill()


penup()

goto(20,20)
begin_fill()
forward(120)
pendown()
forward(40)
right(90)
forward(40)
right(90)
forward(40)
right(90)
forward(40)
end_fill()


penup()
color("green")
goto(400,400)
pendown()
forward(620)
left(90)
forward(620)
left(90)
forward(620)
left(90)
forward(620)













exitonclick()
