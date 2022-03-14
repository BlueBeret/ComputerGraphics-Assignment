import turtle

pen = turtle.Turtle()

def titik(x,y):
    pen.penup()
    pen.goto(x,y)
    pen.pendown()
    pen.dot()

def garisLurus(x1,y1, x2,y2):
    dy = abs(y2-y1)
    dx = abs(x2-x1)
    m = dy/dx
    print(m)
    if m <= 1:
        for i in range(dx):
            titik(x1+i,y1+i*m)
    else:
        for i in range(dy):
            titik(x1+i/m,y1+i)


garisLurus(100,100, 1000, 500)
input()
