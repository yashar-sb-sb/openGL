import pygame
import random

from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

verticies = (
    (1, -1, -1),
    (1, 1, -1),
    (-1, 1, -1),
    (-1, -1, -1),
    (1, -1, 1),
    (1, 1, 1),
    (-1, -1, 1),
    (-1, 1, 1),
    )

edges = (
    (0, 1),
    (0, 3),
    (0, 4),
    (2, 1),
    (2, 3),
    (2, 7),
    (6, 3),
    (6, 4),
    (6, 7),
    (5, 1),
    (5, 4),
    (5, 7),
    )

def Cube():
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(verticies[vertex])
    
    glEnd()


def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
    clock = pygame.time.Clock()
    
    gluPerspective(45, display[0]/display[1], 0.1, 50.0)
    
    glTranslatef(0.0,0.0, -5)

    glRotatef(0, 0, 0, 0)
    
    framesCount = 0
    
    a, b, c, d = random.randint(-2,2),random.randint(-2,2),random.randint(-2,2),random.randint(-2,2)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        framesCount += 1
        if(framesCount % (30) == 0):
            a, b, c, d = random.randint(-2,2),random.randint(-2,2),random.randint(-2,2),random.randint(-2,2)
        glRotatef(a,b,c,d)
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        Cube()
        pygame.display.flip()
        clock.tick(30)


main()
