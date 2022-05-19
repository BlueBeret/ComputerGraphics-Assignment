import math
import time
from turtle import color
# import fungsi dan object dari tugas kemarin
from extension import pen, sc, getRandomColor, titik, garisDDA, w2v,v2w, xvmax, xvmin, yvmax, yvmin, xwmax, xwmin, ywmax, ywmin,turtle


def drawAffineTree():

    alpha = 0
    beta = -25
    gama = -35

    a0 = 0.5 * math.cos(alpha * math.pi / 180)
    b0 = -0.5 * math.sin(alpha * math.pi / 180)
    c0 = 0.65 * math.sin(alpha * math.pi / 180)
    d0 = 0.65 * math.cos(alpha * math.pi / 180)
    e0 = -0.02
    f0 = 1.5

    a2 = 0.6 * math.cos(gama * math.pi / 180)
    b2 = -0.6 * math.sin(gama * math.pi / 180)
    c2 = 0.6 * math.sin(gama * math.pi / 180)
    d2 = 0.6 * math.cos(gama * math.pi / 180)
    e2 = 0
    f2 = 2.3

    a1 = 0.65 * math.cos(-gama * math.pi / 180)
    b1 = -0.65 * math.sin(-gama * math.pi / 180)
    c1 = 0.6 * math.sin(-gama * math.pi / 180)
    d1 = 0.6 * math.cos(-gama * math.pi / 180)
    e1 = 0
    f1 = 2.0

    a3 = 0.65 * math.cos(beta * math.pi / 180)
    b3 = -0.65 * math.sin(beta * math.pi / 180)
    c3 = 0.6 * math.sin(beta * math.pi / 180)
    d3 = 0.6 * math.cos(beta * math.pi / 180)
    e3 = 0
    f3 = 1.6

    a4 = 0.65 * math.cos(-beta * math.pi / 180)
    b4 = -0.65 * math.sin(-beta * math.pi / 180)
    c4 = 0.6 * math.sin(-beta * math.pi / 180)
    d4 = 0.6 * math.cos(-beta * math.pi / 180)
    e4 = 0
    f4 = 1.3

    koorX = [xvmax / 2 + 7, xvmax / 2 - 7, xvmax / 2 - 5, xvmax / 2 + 5 ]
    koorY = [yvmax, yvmax, 430, 430 ]

    fillPoligon(koorX,koorY)

    n =10
    k =1


    
    sc.update()
    while k < n:
        start = time.time()
        for i in range(xvmin,xvmax):
            for j in range(yvmin,yvmax):
                if not (get_pixel_color(i,j) == 'white'):
                    (xw,yw) = v2w(i,j)

                    # gambar tengah
                    xb = a0 * xw + b0 * yw + e0
                    yb = c0 * xw + d0 * yw + f0
                    (xv,yv) = w2v(xb,yb)
                    titik(xv,yv)

                    # gambar daun kiri pertama
                    xb = a1 * xw + b1* yw + e1
                    yb = c1 * xw + d1 * yw + f1
                    (xv,yv) = w2v(xb,yb)
                    titik(xv,yv)

                    # gamabar daun kiri kedua
                    xb = a2 * xw + b2 * yw + e2;
                    yb = c2 * xw + d2 * yw + f2;
                    (xv,yv) = w2v(xb, yb);
                    titik(xv,yv);

                    # draw third leaf (right)
                    xb = a3 * xw + b3 * yw + e3;
                    yb = c3 * xw + d3 * yw + f3;
                    (xv,yv) = w2v(xb, yb);
                    titik(xv,yv);
                    
                    # draw fourth leaf (left)
                    xb = a4 * xw + b4 * yw + e4;
                    yb = c4 * xw + d4 * yw + f4;
                    (xv,yv) = w2v(xb, yb);
                    titik(xv,yv);
        
        print("Iterasi ke-",k,"dilakukan dalam",time.time()-start,"detik")
        print('here')
            
        k +=1
        



    
def fillPoligon(x,y):
    pen.up()
    pen.goto(x[0],y[0])
    pen.down()
    pen.fillcolor(getRandomColor())
    pen.begin_fill()
    for i in range(1,len(x)):
        pen.goto(x[i],y[i])
    pen.goto(x[0],y[0])
    pen.end_fill()
    pen.up()

def get_pixel_color(x, y):

    # canvas use different coordinates than turtle
    y=-y
    # get access to tkinter.Canvas
    canvas = turtle.getscreen().getcanvas()
    
    # find IDs of all objects in rectangle (x, y, x, y)
    ids = canvas.find_overlapping(x, y, x, y)

    # if found objects
    if ids: 
        # get ID of last object (top most)
        index = ids[-1]
        
        # get its color
        color = canvas.itemcget(index, "fill")
        
        # if it has color then return it
        if color:
            return color

    # if there was no object then return "white" - background color in turtle
    return "white" # default color 


if __name__ == "__main__":
    
    drawAffineTree()
    print('done')
    turtle.update()
    turtle.mainloop()
    input()

