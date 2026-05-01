from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math

angle = 0
fan_angle = 0


def init():
    glClearColor(0.60, 0.85, 1.0, 1.0)
    glEnable(GL_DEPTH_TEST)


def quad(a,b,c,d):
    glBegin(GL_QUADS)
    glVertex3fv(a); glVertex3fv(b); glVertex3fv(c); glVertex3fv(d)
    glEnd()


def box(x,y,z,w,h,d,color):
    glColor3fv(color)

    
    quad((x,y,z),(x+w,y,z),(x+w,y+h,z),(x,y+h,z))
    quad((x,y,z+d),(x+w,y,z+d),(x+w,y+h,z+d),(x,y+h,z+d))

    
    quad((x,y,z),(x,y,z+d),(x,y+h,z+d),(x,y+h,z))
    quad((x+w,y,z),(x+w,y,z+d),(x+w,y+h,z+d),(x+w,y+h,z))

    
    quad((x,y+h,z),(x+w,y+h,z),(x+w,y+h,z+d),(x,y+h,z+d))
    quad((x,y,z),(x+w,y,z),(x+w,y,z+d),(x,y,z+d))


def floor():
    box(-10,0,-10,20,0.2,20,(0.95,0.85,0.5))


def walls():
    color = (0.65, 0.45, 0.25)

    
    box(-10,0,-10,20,6,0.2,color)

    
    box(-10,0,9.8,20,6,0.2,color)

    
    box(-10,0,-10,0.2,6,20,color)

    
    box(9.8,0,-10,0.2,6,20,color)


def blackboard():
    box(-3,2,9.75,6,3,0.05,(0.1,0.5,0.2))


def window():
    box(4,2,9.75,4,2,0.05,(0.4,0.8,1.0))


def desk(x,z):
    
    box(x,1,z,2.2,0.2,1.2,(0.85,0.45,0.15))
    
    box(x+0.1,0,z+0.1,0.1,1,0.1,(0.3,0.2,0.1))
    box(x+2,0,z+0.1,0.1,1,0.1,(0.3,0.2,0.1))
    box(x+0.1,0,z+1,0.1,1,0.1,(0.3,0.2,0.1))
    box(x+2,0,z+1,0.1,1,0.1,(0.3,0.2,0.1))


def chair(x,z):
    box(x+0.3,0.5,z+0.3,1.2,0.1,1,(0.4,0.2,0.1))


def fan():
    global fan_angle
    glPushMatrix()
    glTranslatef(0,5.5,0)
    glRotatef(fan_angle,0,1,0)

    for i in range(4):
        glRotatef(90,0,1,0)
        box(0,0,0,0.1,0.1,2,(0.25,0.25,0.25))

    glPopMatrix()


def scene():
    floor()
    walls()
    blackboard()
    window()
    fan()

    for i in range(3):
        for j in range(2):
            x = -6 + i*4
            z = -6 + j*5
            desk(x,z)
            chair(x,z)


def display():
    global angle

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()

    # smooth camera orbit
    cam_x = 12 * math.cos(math.radians(angle))
    cam_z = 10 * math.sin(math.radians(angle))

    gluLookAt(cam_x,5,cam_z, 0,2,0, 0,1,0)

    scene()

    glutSwapBuffers()


def update(v):
    global angle, fan_angle

    angle += 0.3      
    fan_angle += 6    

    glutPostRedisplay()
    glutTimerFunc(16, update, 0)


def reshape(w,h):
    glViewport(0,0,w,h)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(60, w/h, 1, 100)
    glMatrixMode(GL_MODELVIEW)


def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(900,600)
    glutCreateWindow(b"Final 3D Classroom")

    init()

    glutDisplayFunc(display)
    glutReshapeFunc(reshape)
    glutTimerFunc(0, update, 0)

    glutMainLoop()

main()