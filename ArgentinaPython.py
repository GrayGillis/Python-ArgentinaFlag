from turtle import *
import turtle

speed(0)
setup(800, 500)

penup()
goto(-400, 250)
pendown()

# top third
color("skyblue")
begin_fill()
forward(800)
right(90)
forward(167)
right(90)
forward(800)
end_fill()

# sun in middle third
penup()
goto(-10,5)
pendown()

color('red','yellow')

for i in range(100):
    begin_fill()
    forward(80 - i)
    left(170)
    forward(80 - i)
    end_fill()

right(80)

# bottom third

penup()
goto(-400, -83)
pendown()
left(90)

color("skyblue")
begin_fill()
forward(167)
left(90)
forward(800)
left(90)
forward(167)
end_fill()

turtle.done()
