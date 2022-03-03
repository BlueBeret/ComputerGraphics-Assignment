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
sc.screensize(1000,1000) 
# mengganti koordinat seperti layar
sc.setworldcoordinates(llx=0, lly=1000, urx=1000, ury=0) 
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


# fungsi untuk menggambar garis dengan algoritma DDA
def garisDDA(x1,y1,x2,y2,warna):
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
        titik(x,y,warna)
        x += dx
        y += dy
        i += 1
        if (i%5 == 0):
            sc.update() # grafik diupdate setiap 5 titik untuk memberi kesan menggambar secara pelan pelan

if __name__ == "__main__":
    n = int(input("Berapa banyak garis yang ingin dibuat?"))
    print("Garis ke-",0,": ", "x1","y1","x2","y2","RGB")
    for i in range(n):
        x1 = random.randint(0,1000)
        y1 = random.randint(0,1000)
        x2 = random.randint(0,1000)
        y2 = random.randint(0,1000)
        warna = getRandomColor()
        print("Garis ke-",i+1,": ", x1,y1,x2,y2,warna)
        garisDDA(x1,y1,x2,y2,warna)

    input("selesai")