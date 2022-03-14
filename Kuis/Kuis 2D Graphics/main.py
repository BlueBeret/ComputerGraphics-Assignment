from math import sin, cos, pi
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
sc.setworldcoordinates(-1000,-1000,1000,1000)
# membuat object baru 
pen = turtle.Turtle()
pen.speed(0) 
# menyembunyikan kursor/pointer
pen.hideturtle()
pen.penup()


# fungsi untuk menggambar titik
def titik(x,y,warna):
    pen.goto(x,y)
    pen.dot(1, warna)


# fungsi untuk menggambar sinus
def buatSinus(color=(255,0,0), rotasi=0, n = 10000, sc=sc):
    for i in range(n):
        i = 720*i/n

        # x dan y asli
        x = i
        y = sin(i/180*pi)
        if rotasi==0 or rotasi == 180:
            # titik ditransformasikan sesuai koordinat pada layar 
            # yaitu xmin = -1000 ymin = -1000 xmax = 1000 ymax = 1000

            # x dan y rotasi
            x_rotasi = x * cos(rotasi * pi/180) - y * sin(rotasi * pi/180)
            y_rotasi = x * sin(rotasi * pi/180) + y * cos(rotasi * pi/180)

            xv = (x_rotasi/720)*1000
            yv = (y_rotasi)*200
            
            titik(xv,yv , color)
        else:
            # x dan y rotasi
            x_rotasi = x * cos(rotasi * pi/180) - y * sin(rotasi * pi/180)
            y_rotasi = x * sin(rotasi * pi/180) + y * cos(rotasi * pi/180)

            # titik ditransformasikan sesuai koordinat pada layar 
            # yaitu xmin = -1000 ymin = -1000 xmax = 1000 ymax = 1000
            xv = (x_rotasi)*200
            yv = (y_rotasi/720)*1000

            titik(xv, yv, color)






if __name__ == "__main__":
    # buat grafik sinus awal berwarna merah
    buatSinus()
    buatSinus(color=(0,255,0), rotasi=90)
    buatSinus(color=(0,0,255), rotasi=180)
    buatSinus(color=(255,255,0), rotasi=270)
    sc.mainloop()
