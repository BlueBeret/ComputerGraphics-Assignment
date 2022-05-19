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
    sc = turtle.Screen()
    sc.setup(1000,1000)
    sc.screensize(1000,1000) 
    # mengganti koordinat seperti layar
    sc.setworldcoordinates(llx=0, lly=0, urx=1000, ury=1000) 
    # membuat object baru 
    pen = turtle.Turtle()
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
    for i in range(int(panjang)):
        x = x1 * ((1-u) **3) + 3*x2*u*((1-u)**2) + 3*x3*(u**2)*(1-u) + x4*(u**3)
        y = y1 * ((1-u) **3) + 3*y2*u*((1-u)**2) + 3*y3*(u**2)*(1-u) + y4*(u**3)
        u += 1/panjang
        #print(x,y)
        titik(round(x),round(y),warna)
       
        


def windowkeviewport(x_w,y_w):
    x_wmin = -5
    x_wmax = 5
    y_wmin = -5
    y_wmax = 5

    x_vmin = 0
    x_vmax = 1000
    y_vmin = 0
    y_vmax = 1000

    sx = (x_vmax - x_vmin) / (x_wmax - x_wmin)
    sy = (y_vmax - y_vmin) / (y_wmax - y_wmin)
 
    # calculating the point on viewport
    x_v = x_vmin + ((x_w - x_wmin) * sx)
    y_v = y_vmin + ((y_w - y_wmin) * sy)

    return (x_v,y_v)


def circle(x,y, radius):
    global pen
    global sc
    pen.goto(x,y-radius)
    pen.pendown()
    pen.circle(radius)
    pen.penup()

    
if __name__ == "__main__":
    init()
    x_center = 0
    y_center = 0
    radius = 100
    (xv,yv) = windowkeviewport(x_center,y_center)
    pen.fillcolor(getRandomColor())
    circle(xv,yv,radius)
    # koordinat berzier pertama
    x1 = 1
    y1 = 0
    x2 = 2
    y2 = 1
    x3 = 4
    y3 = 4
    x4 = 5
    y4 = 0
    (x1v,y1v) = windowkeviewport(x1,y1)
    (x2v,y2v) = windowkeviewport(x2,y2)
    (x3v,y3v) = windowkeviewport(x3,y3)
    (x4v,y4v) = windowkeviewport(x4,y4)
    kurvaBezier(x1v,y1v,x2v,y2v,x3v,y3v,x4v,y4v, (255,0,0))

    # koordinat berzier kedua
    x1_2 = x1
    y1_2 = -y1
    x2_2 = x2
    y2_2 = -y2
    x3_2 = x3
    y3_2 = -y3
    x4_2 = x4
    y4_2 = -y4
    (x1_2v,y1_2v) = windowkeviewport(x1_2,y1_2)
    (x2_2v,y2_2v) = windowkeviewport(x2_2,y2_2)
    (x3_2v,y3_2v) = windowkeviewport(x3_2,y3_2)
    (x4_2v,y4_2v) = windowkeviewport(x4_2,y4_2)
    kurvaBezier(x1_2v,y1_2v,x2_2v,y2_2v,x3_2v,y3_2v,x4_2v,y4_2v, (255,0,0))

    # koordinat berzier ketiga
    x1_3 = -x1
    y1_3 = y1
    x2_3 = -x2
    y2_3 = y2
    x3_3 = -x3
    y3_3 = y3
    x4_3 = -x4
    y4_3 = y4
    (x1_3v,y1_3v) = windowkeviewport(x1_3,y1_3)
    (x2_3v,y2_3v) = windowkeviewport(x2_3,y2_3)
    (x3_3v,y3_3v) = windowkeviewport(x3_3,y3_3)
    (x4_3v,y4_3v) = windowkeviewport(x4_3,y4_3)
    kurvaBezier(x1_3v,y1_3v,x2_3v,y2_3v,x3_3v,y3_3v,x4_3v,y4_3v, (255,0,0))

    # koordinat berzier ke empat
    x1_4 = x1_3
    y1_4 = -y1_3
    x2_4 = x2_3
    y2_4 = -y2_3
    x3_4 = x3_3
    y3_4 = -y3_3
    x4_4 = x4_3
    y4_4 = -y4_3
    (x1_4v,y1_4v) = windowkeviewport(x1_4,y1_4)
    (x2_4v,y2_4v) = windowkeviewport(x2_4,y2_4)
    (x3_4v,y3_4v) = windowkeviewport(x3_4,y3_4)
    (x4_4v,y4_4v) = windowkeviewport(x4_4,y4_4)
    kurvaBezier(x1_4v,y1_4v,x2_4v,y2_4v,x3_4v,y3_4v,x4_4v,y4_4v, (255,0,0))

    # koordinat berzier ke 5
    x1_5 = y1
    y1_5 = x1
    x2_5 = y2
    y2_5 = x2
    x3_5 = y3
    y3_5 = x3
    x4_5 = y4
    y4_5 = x4
    (x1_5v,y1_5v) = windowkeviewport(x1_5,y1_5)
    (x2_5v,y2_5v) = windowkeviewport(x2_5,y2_5)
    (x3_5v,y3_5v) = windowkeviewport(x3_5,y3_5)
    (x4_5v,y4_5v) = windowkeviewport(x4_5,y4_5)
    kurvaBezier(x1_5v,y1_5v,x2_5v,y2_5v,x3_5v,y3_5v,x4_5v,y4_5v, (255,0,0))

    # koordinat berzier ke 6
    x1_6 = -y1
    y1_6 = x1
    x2_6 = -y2
    y2_6 = x2
    x3_6 = -y3
    y3_6 = x3
    x4_6 = -y4
    y4_6 = x4
    (x1_6v,y1_6v) = windowkeviewport(x1_6,y1_6)
    (x2_6v,y2_6v) = windowkeviewport(x2_6,y2_6)
    (x3_6v,y3_6v) = windowkeviewport(x3_6,y3_6)
    (x4_6v,y4_6v) = windowkeviewport(x4_6,y4_6)
    kurvaBezier(x1_6v,y1_6v,x2_6v,y2_6v,x3_6v,y3_6v,x4_6v,y4_6v, (255,0,0))

    # koordinat berzier ke 7
    x1_7 = x1_6
    y1_7 = -y1_6
    x2_7 = x2_6
    y2_7 = -y2_6
    x3_7 = x3_6
    y3_7 = -y3_6
    x4_7 = x4_6
    y4_7 = -y4_6
    (x1_7v,y1_7v) = windowkeviewport(x1_7,y1_7)
    (x2_7v,y2_7v) = windowkeviewport(x2_7,y2_7)
    (x3_7v,y3_7v) = windowkeviewport(x3_7,y3_7)
    (x4_7v,y4_7v) = windowkeviewport(x4_7,y4_7)
    kurvaBezier(x1_7v,y1_7v,x2_7v,y2_7v,x3_7v,y3_7v,x4_7v,y4_7v, (255,0,0))

    # koordinat berzier kek 8
    x1_8 = -x1_7
    y1_8 = y1_7
    x2_8 = -x2_7
    y2_8 = y2_7
    x3_8 = -x3_7
    y3_8 = y3_7
    x4_8 = -x4_7
    y4_8 = y4_7
    (x1_8v,y1_8v) = windowkeviewport(x1_8,y1_8)
    (x2_8v,y2_8v) = windowkeviewport(x2_8,y2_8)
    (x3_8v,y3_8v) = windowkeviewport(x3_8,y3_8)
    (x4_8v,y4_8v) = windowkeviewport(x4_8,y4_8)
    kurvaBezier(x1_8v,y1_8v,x2_8v,y2_8v,x3_8v,y3_8v,x4_8v,y4_8v, (255,0,0))





        
        

        

    sc.update()

    input("Press Enter to exit...")