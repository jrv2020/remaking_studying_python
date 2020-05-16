
from turtle import *
color('red', 'yellow')
begin_fill()
while True:
    forward(200)
    left(170)
    if abs(pos()) < 1:
        break
end_fill()
done()

"""
x = int(input('quantas repetições quer?'))
y = int(input('quantas repetições quer?'))
from turtle import *
color('red', 'yellow')
for x in range(y):
    print(x)
    color('green', 'yellow')
    begin_fill()
    while True:
        forward(200+x)
        left(170)
        if abs(pos()) < 1:
            break
        end_fill()

    color('red', 'green')
    begin_fill()
    while True:
        forward(x+5)
        left(x+5)
        if abs(pos()) < 10:
           break
    end_fill()
    done()
"""