###This code will not work in repl.it as there is no access to the colorgram package here.###
##We talk about this in the video tutorials##
# import colorgram

# rgb_colors = []

# colors = colorgram.extract('image.jpg', 30)
# for color in colors:

#     r= color.rgb.r
#     g= color.rgb.g
#     b= color.rgb.b
#     new_color=(r,g,b)
#     rgb_colors.append(new_color)
import turtle as t

import random
jimmy=t.Turtle()
screen=t.Screen()
print(f"Screen Width: {screen.window_width()}")
print(f"Screen heihgt: {screen.window_height()}")
start_x=screen.window_height
color_list=[ (202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]
t.colormode(255)
jimmy.penup()
print(jimmy.pos())
x=-320
y=-280
jimmy.goto(x,y)
jimmy.pendown()

def drawCircle():
    jimmy.pendown()
    jimmy.dot(20,random.choice(color_list))
    jimmy.penup()
    jimmy.forward(70)
for i in range(0,11):
    for i in range(0,11):
        drawCircle()
    y+=50
    jimmy.goto(x,y)
jimmy.ht()
screen.exitonclick()