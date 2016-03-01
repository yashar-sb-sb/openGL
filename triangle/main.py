import pygame
import random
import math

from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *


def mult(X,Y):
  return [[sum(a*b for a,b in zip(X_row,Y_col)) for Y_col in zip(*Y)] for X_row in X]

verticies = [
    [0, 0, 1],
    [0, 0.1, 1],
    [0.15, 0, 1]
    ]

ver = [
    [0, 0, 0],
    [0, 0.1, 0],
    [0.15, 0, 0]
    ]


edges = [
    [0, 1],
    [1, 2],
    [2, 0],
    ]


def Draw():
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glColor3fv((1,0,0))
            glVertex3fv(verticies[vertex])
    
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
            glVertex3fv(trans(ver[vertex]))
    
    glEnd()

def t1(x):
  return [x[0]/2,x[1],x[2]]

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
        
        for i in range(3):
          ver[i] = t1(verticies[i])

        for i in range(3):
          k = [[ver[i][0]],[ver[i][1]],[ver[i][2]]]
          k = mult([
            [math.cos(45/180*math.pi),math.sin(45/180*math.pi),0],
            [-math.sin(45/180*math.pi),math.cos(45/180*math.pi),0],
            [0,0,1]],k)
          ver[i][0] = k[0][0]
          ver[i][1] = k[1][0]
          ver[i][2] = k[2][0]
          

        for i in range(3):
          k = [[ver[i][0]],[ver[i][1]],[ver[i][2]]]
          k = mult([
            [math.cos(45/180*math.pi),math.sin(45/180*math.pi),0],
            [-math.sin(45/180*math.pi),math.cos(45/180*math.pi),0],
            [0,0,1]],k)
          ver[i][0] = k[0][0]
          ver[i][1] = k[1][0]
          ver[i][2] = k[2][0]
        
        
        Draw1()
        pygame.display.flip()
        clock.tick(30)


main()
