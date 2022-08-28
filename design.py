import turtle
t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor('Black')
t.speed(10)
col=['red','red','red','red']
c=0
for i in range(1000):
    t.forward(i)
    t.right(100)
    t.color(col[c])
    if c==3:
        c=0
    else:
        c+=1