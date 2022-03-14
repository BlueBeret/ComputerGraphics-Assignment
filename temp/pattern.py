from tkinter import *

root = Tk()
canvas = Canvas(root, 
    width=1000, 
    height=1000,
    background="#FFFFFF")
canvas.pack(expand=YES, fill=BOTH)



def dot(x,y,size=1, color="#FF0000", outline=""):
    if size==1:
        canvas.create_line(x,y,x+1,y, fill=color, width=size)
        return
    canvas.create_oval(x-size/2,y-size/2,x+size/2,y+size/2,fill=color,width=0, outline=outline)

def onClick(event):
    global BERZIER_COORD
    if len(BERZIER_COORD) < 8:
        BERZIER_COORD.append(event.x)
        BERZIER_COORD.append(event.y)
    if len(BERZIER_COORD) == 8:
        kurvaBezier(BERZIER_COORD[0], BERZIER_COORD[1], BERZIER_COORD[2],
        BERZIER_COORD[3], BERZIER_COORD[4], BERZIER_COORD[5], BERZIER_COORD[6], BERZIER_COORD[7])
        BERZIER_COORD = []
        

def kurvaBezier(x1,y1,x2,y2,x3,y3,x4,y4, warna="#FF0000"):
    panjang = max(abs(x1-x2), abs(y1-y2)) + max(abs(x2-x3), abs(y2-y3))+max (abs(x3-x4), abs(y3-y4))

    u = 0
    for i in range(panjang):
        x = x1 * ((1-u) **3) + 3*x2*u*((1-u)**2) + 3*x3*(u**2)*(1-u) + x4*(u**3)
        y = y1 * ((1-u) **3) + 3*y2*u*((1-u)**2) + 3*y3*(u**2)*(1-u) + y4*(u**3)
        u += 1/panjang
        dot(round(x),round(y),color=warna)


BERZIER_COORD = []

canvas.bind("<Button-1>", onClick)

root.mainloop()