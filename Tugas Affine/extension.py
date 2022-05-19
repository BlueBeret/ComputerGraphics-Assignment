import random
# import library turtle, bisa diintall dengan command "pip install PythonTurtle"
import turtle 

# INISIALISASI Program

# Mengubah mode warna menjadi RGB 
turtle.colormode(255)
# membuat object layar baru dengan ukuran 1000x1000 piksel
turtle.delay(0)
turtle.ht()
turtle.tracer(0,0)
sc = turtle.Screen()
sc.setup(500,625)
sc.screensize(500,625)
scWidth = sc.window_width()
scHeight = sc.window_height()
# mengganti koordinat seperti layar
sc.setworldcoordinates(llx=0, lly=0, urx=500, ury=625) 
# membuat object baru 
pen = turtle.Turtle()
# menyembunyikan kursor/pointer
pen.penup()

xvmin = 0
xvmax = 500
yvmin = 0
yvmax = 625

xwmin = -3
xwmax = 3
ywmin = 0
ywmax = 7.5

# fungsi untuk membuat warna random
def getRandomColor():
    return (random.randint(0,255), random.randint(0,255), random.randint(0,255))

# fungsi untuk menggambar titik
def titik(x,y,warna=(255,0,0), ketebalan=1):
    # menyesuaikan dengan ukuran layar
    pen.goto(x,y)
    pen.down()
    pen.pensize(1)
    pen.forward(0)
    pen.up()


# fungsi untuk menggambar garis dengan algoritma DDA
def garisDDA(x1,y1,x2,y2,warna=(255,0,0),ketebalan=1):

    dx = x2 - x1
    dy = y2 - y1

    # banyak iterasi = dx jika dx>dy dan dy jika dx<dy
    if (abs(dx) > abs(dy)):
        panjang = abs(dx)
    else:
        panjang = abs(dy)

    # jika abs(dx) > abs(dy) maka perubahan kooridinat x adalah 1
    # sebaliknya, maka perubahan x adalah 1/m
    dx = dx /panjang

    # jika abs(dx) > abs(dy) maka perubahan kooridinat y adalah m
    # sebaliknya, maka perubahan y adalah 1
    dy = dy /panjang
    
    x,y = x1,y1
    i = 1
    while(i <= panjang):
        pen.goto(x,y)
        pen.dot(ketebalan, warna)
        x += dx
        y += dy
        i += 1
        
    sc.update()

def w2v(xw, yw):
    xv = xvmin + (int)((xw - xwmin) * (xvmax - xvmin) / (xwmax - xwmin))
    yv = yvmax - (int) ((yw - ywmin) * (yvmax - yvmin) / (ywmax - ywmin))

    return (xv, yv)

def v2w(xv, yv):
    xw = xwmin + (xv - xvmin) * (xwmax - xwmin) / (xvmax - xvmin)
    yw = ywmin + (yvmax - yv) * (ywmax - ywmin) / (yvmax - yvmin)

    return (xw, yw)


