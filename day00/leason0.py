from turtle import *

#house
speed(30)

#step 1 spuare


color('orange')
width(7)
forward(150)
backward(300)
right(90)
forward(300)
left(90)
forward(300)
left(90)
forward(300)
backward(300)
left(90)



#door
forward(120)
color('red')
begin_fill()
right(90)
forward(130)
left(90)
forward(75)
left(90)
forward(130)
end_fill()




#roof
penup()
goto(150,0)
pendown()
color('purple')
begin_fill()
right(147.5)
forward(280)
left(115)
forward(280)
end_fill()




#window
width(3)
penup()
goto(75,-75)
pendown()
color('brown')
begin_fill()
left(32.5)
forward(30)
left(90)
forward(30)
left(90)
forward(30)
left(90)
forward(60)
left(90)
forward(30)
left(90)
forward(30)
left(90)
forward(60)
left(90)
forward(30)
left(90)
forward(30)
left(90)
forward(60)
left(90)
forward(30)
left(90)
forward(30)
color('yellow')
end_fill()
penup()
goto(-75,-75)
pendown()
color('brown')
begin_fill()
forward(30)
left(90)
forward(30)
left(90)
forward(30)
left(90)
forward(60)
left(90)
forward(30)
left(90)
forward(30)
left(90)
forward(60)
left(90)
forward(30)
left(90)
forward(30)
left(90)
forward(60)
left(90)
forward(30)
left(90)
forward(30)
color('yellow')
end_fill()



exitonclick()