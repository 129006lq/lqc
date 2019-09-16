#!/usr/bin/python
# -*- coding: UTF-8 -*-

import turtle
import time
turtle.pensize(5)
turtle.color('yellow','red')

turtle.speed(3)
turtle.bgcolor()
turtle.bgpic(r'C:\Users\Administrator\Desktop\壁纸\lqc.gif')

turtle.begin_fill()
for _ in range(5):
    turtle.forward(200)
    turtle.left(144)
turtle.end_fill()

time.sleep(5)

turtle.begin_fill()
for _ in range(5):
    turtle.backward(200)
    turtle.right(144)
turtle.end_fill()

turtle.penup()
turtle.goto(-100,-200)
turtle.pencolor('green')
turtle.write("满园春色关不住",font=('Arial',30,'normal'))



turtle.mainloop()


