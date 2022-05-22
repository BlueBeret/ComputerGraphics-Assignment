import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *



verticies = (
(0,0,0), #1
(2,0,0), #2
(2,0,2), #3
(0,0,2), #4
(0.5,4,0.5),# 5
(1.5,4,0.5),# 6
(1.5,4,1.5),# 7
(0.5,4,1.5),# 8
(0.5,5,0.5),# 9
(1.5,5,0.5),# 10
(1.5,5,1.5),# 11
(0.5,5,1.5),# 12
(0.5,6,0.5),# 13
(1.5,6,0.5),# 14
(1.5,6,1.5),# 15
(0.5,6,1.5)# 16
    )

surfaces = (
(4,1,2,6,5),
(4,1,4,8,5),
(4,2,3,7,6),
(4,5,6,7,8),
(4,3,4,8,7),
(4,1,2,3,4),
(4,9,10,14,13),
(4,9,12,16,13),
(4,10,11,15,14),
(4,13,14,15,16),
(4,11,12,16,15),
(4,9,10,11,12)
)



edges = []
for j in range(len(surfaces)):
    surface = surfaces[j]
    titik = [surface[x] for x in range(1, surface[0]+1)]
    for i in range(len(titik)):
        edges.append((titik[i], titik[(i+1)%len(titik)]))
print(edges)

colors = (
    (1,0,0),
    (0,1,0),
    (0,0,1),
    (0,1,0),
    (1,1,1),
    (0,1,1),
    (1,0,0),
    (0,1,0),
    (0,0,1),
    (1,0,0),
    (1,1,1),
    (0,1,1),
    )

def dots():
    glBegin(GL_POINTS)
    for vertex in verticies:
        glVertex3fv(vertex)
    glEnd()

def Cube():
    # glBegin(GL_QUADS)
    # for surface in surfaces:
    #     x = 0
    #     for vertex in surface:
    #         x+=1
    #         glColor3fv(colors[x])
    #         glVertex3fv(verticies[vertex])
    # glEnd()

    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            index = vertex-1
            glVertex3fv(verticies[index])
    glEnd()


def main():
    pygame.init()
    display = (800,600)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

    gluPerspective(100, (display[0]/display[1]), 0.1, 50.0)

    glTranslatef(0.0,-2, -5)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    glTranslatef(-0.5,0,0)
                if event.key == pygame.K_d:
                    glTranslatef(0.5,0,0)
                if event.key == pygame.K_w:
                    glTranslatef(0,0,0.5)
                if event.key == pygame.K_s:
                    glTranslatef(0,0,-0.5)
                if event.key == pygame.K_UP:
                    glTranslatef(0,-0.5,0)
                if event.key == pygame.K_DOWN:
                    glTranslatef(0,0.5,0)
                if event.key == pygame.K_e:
                    glRotatef(30,0,1,0)

        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        dots()
        Cube()
        pygame.display.flip()
        pygame.time.wait(10)


main()