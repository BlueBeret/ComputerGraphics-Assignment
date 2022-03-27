# SOFIRUL DANATRIYA (20/455453/PA/19668)
# requirement: `pip install PythonTurtle`


# import lib math untuk fungsi trigonometri
import math
from turtle import color

# import fungsi dan object dari tugas kemarin
from extension import pen, sc, getRandomColor, titik, garisDDA

# window yang saya gunakan adalah (-9,-9,9,9)

def segitiga(x1,y1,x2,y2,x3,y3, warna=None):
    if warna == None:
        warna = getRandomColor()
    garisDDA(x1,y1,x2,y2, warna)
    garisDDA(x2,y2,x3,y3, warna)
    garisDDA(x3,y3,x1,y1, warna)

def rotasiDegree(x,y,theta):
    # mengubah sudut dari degree ke radian
    theta = math.radians(theta)
    x1 = x*math.cos(theta) - y*math.sin(theta)
    y1 = x*math.sin(theta) + y*math.cos(theta)
    return x1,y1

def skala(x,y,sx,sy):
    return x*sx, y*sy

def rotasiSegitiga(x1,y1,x2,y2,x3,y3, theta):
    # untuk rotasi suatu segitiga
    # titik titiknya di rotasi dulu
    

    x1,y1 = rotasiDegree(x1,y1,theta)
    x2,y2 = rotasiDegree(x2,y2,theta)
    x3,y3 = rotasiDegree(x3,y3,theta)
    return (x1,y1,x2,y2,x3,y3)

def skalaSegitiga(x1,y1,x2,y2,x3,y3, sx,sy):
    # untuk scaling segitiga
    x1,y1 = skala(x1,y1,sx,sy)
    x2,y2 = skala(x2,y2,sx,sy)
    x3,y3 = skala(x3,y3,sx,sy)
    return (x1,y1,x2,y2,x3,y3)


if __name__ == "__main__":
    # garis x=0 dan garis y=0
    garisDDA(0,-9,0,9, (255,0,0), ketebalan=2)
    garisDDA(-9,0,9,0, (255,0,0), ketebalan=2)

    # koordinat segitiga pqr
    (px,py,qx,qy,rx,ry) = (1,1,1,4,4,1)

    # sebelum scaling dan rotasi
    segitiga(px,py,qx,qy,rx,ry)
    print("\n")
    while 1:
        (px,py,qx,qy,rx,ry) = (1,1,1,4,4,1)
        theta = float( input("masukkan sudut rotasi dalam derajat: "))
        sx = float(input("masukkan nilai scaling x: "))
        sy = float(input("masukkan nilai scaling y: "))

        # rotasi segitiga
        (px,py,qx,qy,rx,ry) = rotasiSegitiga(px,py,qx,qy,rx,ry, theta)
        # scaling segitiga menjadi 1,5 kali lebih besar
        (px,py,qx,qy,rx,ry) = skalaSegitiga(px,py,qx,qy,rx,ry, sx,sy)

        segitiga(px,py,qx,qy,rx,ry)
        input(f"△PQR setelah rotasi {theta}° & scaling {sx,sy})\n{'='*20}\nTekan ctrl+c untuk keluar,\natau enter untuk melanjutkan\n{'='*20}\n")