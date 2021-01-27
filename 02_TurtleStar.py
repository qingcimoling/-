#02_TurtleStar.py
from turtle import *
colormode(1.0)  
color((1,0.96,0.93),"pink")  
begin_fill()
while True:
    forward(200)
    left(170)
    if abs(pos()) < 1:
        break
end_fill()
done()
