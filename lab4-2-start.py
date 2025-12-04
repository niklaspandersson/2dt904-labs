from OpenGL.GL import *
from matrix import Matrix
from app import run, readFile
from glslprogram import Program
from meshes import setupSquare

vsCode = readFile('./shaders/lab4-2.vert')
fsCode = readFile('./shaders/lab4-2.frag')


def init():
    global drawCount
    global program

    program = Program(vsCode, fsCode)
    program.use()

    drawCount = setupSquare(program.programId, 2)

    projection = Matrix.makePerspective()
    invCameraPos = Matrix.makeTranslation(0, 0, -2)
    mProjView = projection @ invCameraPos

    program.setUniformMat4('mModel', Matrix.makeIdentity())
    program.setUniformMat4('mProjView', mProjView)


def update(dt, time):
    glClear(GL_COLOR_BUFFER_BIT)
    glDrawArrays(GL_TRIANGLES, 0, drawCount)


run("2DT904 - Rasterization", init, update)
