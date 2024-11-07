#7) გაიმეორეთ გავლილი მასალა


from turtle import *
#we want to draw a ladybug
speed(30)
width(5)
begin_fill()
circle(120)

color("red")
end_fill()
left(90)
color("black")
forward(240)
penup()
right(30)
forward(-80)
pendown()
begin_fill()
circle(20)
end_fill()

penup()
begin_fill()
left(30)
forward(-60)
pendown()
circle(20)
end_fill()

penup()
right(10)
begin_fill()
forward(-60)
left(90)
circle(20)
end_fill()


begin_fill()
penup()
right(180)
forward(100)
pendown()
circle(20)
end_fill()

penup()
begin_fill()
left(90)
forward(120)
left(90)
pendown()
circle(20)
end_fill()

penup()
begin_fill()
right(70)
forward(60)
left(90)
circle(20)
pendown()
end_fill()

penup()
begin_fill()
right(40)
forward(60)
right(130)
pendown()
circle(20)
end_fill()

begin_fill()
right(-30)
forward(60)
circle(5)
end_fill()

begin_fill()
penup()
forward(-60)

pendown()
begin_fill()
left(90)
forward(20)
forward(50)
left(90)
circle(5)
end_fill()






exitonclick()

