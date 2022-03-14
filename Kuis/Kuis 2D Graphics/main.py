from curses.ascii import STX
from math import sin, cos, pi
import random
from tkinter import XView
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
sc.bgcolor('black')
sc.screensize(1000,1000)
sc.setworldcoordinates(0,-1,720,1)
# membuat object baru 
pen = turtle.Turtle()
pen.speed(0) 
# menyembunyikan kursor/pointer
pen.hideturtle()
pen.penup()




# fungsi untuk membuat warna random
def getRandomColor():
    return (random.randint(0,255), random.randint(0,255), random.randint(0,255))

# fungsi untuk menggambar titik
def titik(x,y,warna):
    pen.goto(x,y)
    pen.dot(1, warna)


# fungsi untuk menggambar sinus
def buatSinus(color=(255,0,0), rotasi=0, n = 10000, sc=sc):
    if rotasi == 0 or rotasi == 180:
        sc.setworldcoordinates(0,-1,720,1)
    elif rotasi == 90 or rotasi == 270:
        sc.setworldcoordinates(-1,0,1,720)

    
    for i in range(n):
        i = 720*i/n

        # x dan y asli
        x = i
        y = sin(i/180*pi)
        if rotasi==0:
            titik(x, y, color)
        else:
            # x dan y rotasi
            x_rotasi = x * cos(rotasi * pi/180) - y * sin(rotasi * pi/180)
            y_rotasi = x * sin(rotasi * pi/180) + y * cos(rotasi * pi/180)
            titik(x_rotasi, y_rotasi, color)






if __name__ == "__main__":
    # buat grafik sinus awal berwarna merah
    buatSinus()
    input()
    buatSinus(color=(0,255,0), rotasi=90)
    input()
