import pygame
import random

from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *


def mult(x,y):
  return [[sum(a*b for a,b in zip(X_row,Y_col)) for Y_col in zip(*Y)] for X_row in X]

verticies = (
    (0, 0.2, 0),
    (-0.2, -0.1, 0),
    (0.1, 0.15, 0),
    (-0.2, 0.1, 0),
    (0.1, 0, 0),
    )

edges = (
    (0, 1),
    (1, 2),
    (2, 3),
    (3, 4),
    (4, 0),
    )

def get(x):
  return (x[0]+0.3,x[1]+0.3,x[2]+0.3)

def Draw():
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glColor3fv((0,1,0))
            glVertex3fv(get(verticies[vertex]))
    
    glEnd()

def trans(x):
  return (-x[0],x[1],x[2])

def trans1(x):
  return (x[0],-x[1],x[2])

def Draw1():
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glColor3fv((0,0,1))
            glVertex3fv(trans(get(verticies[vertex])))
    
    glEnd()

def Draw2():
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glColor3fv((1,0,0))
            glVertex3fv(trans1(get(verticies[vertex])))
    
    glEnd()


def main():
    pygame.init()
    display = (600, 600)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
    clock = pygame.time.Clock()
    
    framesCount = 0
    
    a, b, c, d = random.randint(-2,2),random.randint(-2,2),random.randint(-2,2),random.randint(-2,2)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        Draw()
        Draw1()
        Draw2()
        pygame.display.flip()
        clock.tick(30)


main()
