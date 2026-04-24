from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def display():
    glClear(GL_COLOR_BUFFER_BIT)

    # ---- Outer Rectangle (Window Boundary) ----
    glColor3f(1.0, 1.0, 1.0)  # White
    glBegin(GL_LINE_LOOP)
    glVertex2f(50, 50)
    glVertex2f(250, 50)
    glVertex2f(250, 250)
    glVertex2f(50, 250)
    glEnd()

    # ---- Inner Rectangle (Red Edges) ----
    glColor3f(1.0, 0.0, 0.0)  # Red
    glBegin(GL_LINE_LOOP)
    glVertex2f(100, 100)
    glVertex2f(200, 100)
    glVertex2f(200, 200)
    glVertex2f(100, 200)
    glEnd()

    glFlush()

def init():
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glMatrixMode(GL_PROJECTION)
    gluOrtho2D(0, 300, 0, 300)

def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(500, 500)
    glutCreateWindow(b"Rectangle Window - PyOpenGL")

    init()
    glutDisplayFunc(display)
    glutMainLoop()

if __name__ == "__main__":
    main()
