from tkinter import *
import time
import math

xvmin = 0
xvmax = 100
yvmin = 0
yvmax = 200

xwmin = -3
xwmax = 3
ywmin = 0
ywmax = 7.5

root = Tk()
canvas = Canvas(root, 
    width=100, 
    height=200,
    background="#FFFFFF")
canvas.pack(expand=YES, fill=BOTH)

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

    input()
    print('drawing tree')
    while k < n:
        
        for i in range(xvmin,xvmax):
            start = time.time()
            for j in range(yvmin,yvmax):
                if not (get_pixel_color(canvas,i,j) == 'WHITE'):
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
            print("Iterasi ke-",i,"dilakukan dalam",time.time()-start,"detik")
        
        print("Iterasi ke-",k,"dilakukan dalam",time.time()-start,"detik")
        print('here')
            
        k +=1

def titik(x,y, color="#FF0000"):
    canvas.create_line(x,y,x+1,y, fill=color, width=4)

def fillPoligon(x,y):
    coord = []
    for i in range(len(x)):
        coord.append(x[i])
        coord.append(y[i])
    canvas.create_polygon(coord,fill='red')

def w2v(xw, yw):
    xv = xvmin + (int)((xw - xwmin) * (xvmax - xvmin) / (xwmax - xwmin))
    yv = yvmax - (int) ((yw - ywmin) * (yvmax - yvmin) / (ywmax - ywmin))

    return (xv, yv)

def v2w(xv, yv):
    xw = xwmin + (xv - xvmin) * (xwmax - xwmin) / (xvmax - xvmin)
    yw = ywmin + (yvmax - yv) * (ywmax - ywmin) / (yvmax - yvmin)

    return (xw, yw)

def get_pixel_color(canvas, x, y):
        ids = canvas.find_overlapping(x, y, x, y)

        if len(ids) > 0:
            index = ids[-1]
            color = canvas.itemcget(index, "fill")
            color = color.upper()
            if color != '':
                return color

        return "WHITE"

if __name__ == '__main__':
    drawAffineTree()
    titik(50,50)
    root.mainloop()
