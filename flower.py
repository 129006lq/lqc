#!/usr/bin/python
# -*- coding: UTF-8 -*-

import turtle
import time

# 同时设置pencolor=color1, fillcolor=color2
turtle.color("red", "yellow")
turtle.bgpic(r'C:\Users\Administrator\Desktop\壁纸\lqc.gif')

turtle.begin_fill()
for _ in range(50):

    turtle.forward(200)
    turtle.right(170)
turtle.end_fill()

turtle.mainloop()


