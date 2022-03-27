import random
# import library turtle, bisa diintall dengan command "pip install PythonTurtle"
import turtle 

# INISIALISASI Program

# Mengubah mode warna menjadi RGB 
turtle.colormode(255)
# menghapus semua delay default
turtle.delay(0)
turtle.ht()
turtle.tracer(0,0)
# membuat object layar baru dengan ukuran 1000x1000 piksel
sc = turtle.Screen()
sc.setup(990,990)
sc.screensize(990,990)
scWidth = sc.window_width()
scHeight = sc.window_height()
# mengganti koordinat seperti layar
sc.setworldcoordinates(llx=-495, lly=-495, urx=495, ury=495) 
# membuat object baru 
pen = turtle.Turtle()
pen.speed(0) 
# menyembunyikan kursor/pointer
pen.hideturtle()
pen.penup()

WXMIN = -9
WXMAX = 9
WYMIN = -9
WYMAX = 9

# fungsi untuk membuat warna random
def getRandomColor():
    return (random.randint(0,255), random.randint(0,255), random.randint(0,255))

# fungsi untuk menggambar titik
def titik(x,y,warna, ketebalan=1):
    # menyesuaikan dengan ukuran layar
    x *= 55
    y *= 55
    pen.goto(x,y)
    pen.dot(ketebalan, warna)


# fungsi untuk menggambar garis dengan algoritma DDA
def garisDDA(x1,y1,x2,y2,warna,ketebalan=1):
    #menyesuaikan dengan ukuran layar
    x1 *= 55
    y1 *= 55
    x2 *= 55
    y2 *= 55

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
        
    sc.update() # grafik diupdate setiap 5 titik untuk memberi kesan menggambar secara pelan pelan
