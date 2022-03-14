import random, time
# import library turtle, bisa diintall dengan command "pip install PythonTurtle"
import turtle 

global pen
# INISIALISASI Program
def init():
    global pen
    global sc
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
def titik(x,y,warna, size=1):
    global pen
    pen.goto(x,y)
    pen.dot(size, warna)

def kurvaBezier(x1,y1,x2,y2,x3,y3,x4,y4, warna):
    # menghitung panjang kurva
    panjang = max(abs(x1-x2), abs(y1-y2)) + max(abs(x2-x3), abs(y2-y3))+max (abs(x3-x4), abs(y3-y4))

    u = 0
    for i in range(panjang):
        x = x1 * ((1-u) **3) + 3*x2*u*((1-u)**2) + 3*x3*(u**2)*(1-u) + x4*(u**3)
        y = y1 * ((1-u) **3) + 3*y2*u*((1-u)**2) + 3*y3*(u**2)*(1-u) + y4*(u**3)
        u += 1/panjang
        #print(x,y)
        titik(round(x),round(y),warna)
        # grafik diupdate setiap 5 titik untuk memberi kesan menggambar secara pelan pelan
        if (i%5 == 0):
            sc.update() 
        time.sleep(0.01)


if __name__ == "__main__":
    while 1:
        # titik dibuat random
        init()
        x1 = random.randint(0,1000)
        x2 = random.randint(0,1000)
        x3 = random.randint(0,1000)
        x4 = random.randint(0,1000)
        y1 = random.randint(0,1000)
        y2 = random.randint(0,1000)
        y3 = random.randint(0,1000)
        y4 = random.randint(0,1000)

        print("-------------------")
        print(f"P1 = ({x1},{y1})")
        print(f"P2 = ({x2},{y2})")
        print(f"P3 = ({x3},{y3})")
        print(f"P4 = ({x4},{y4})")
        print("-------------------")

        # titik p terminal warna merah. dan titik p2 warna biru dan p3 warna hijau
        titik(x1,y1,(255,0,0),5)
        titik(x2,y2,(0,0,255),5)
        titik(x3,y3,(50,255,50),5)
        titik(x4,y4,(255,0,0),5)
        sc.update()

        warna = getRandomColor()
        kurvaBezier(x1,y1,x2,y2,x3,y3,x4,y4, warna)

        x = input("buat lagi? (y/n)")
        if x.lower() == "n":
            break
        sc.clear()

        
        

        

    sc.update()

    input("Press Enter to exit...")