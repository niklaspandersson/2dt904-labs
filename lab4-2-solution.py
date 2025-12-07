from OpenGL.GL import *
from matrix import Matrix
from app import run, readFile
from glslprogram import Program
from meshes import setupSquare
import math

vsCode = readFile('./shaders/lab4-2-solution.vert')
fsCode = readFile('./shaders/lab4-2-solution.frag')


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

    mModel = Matrix.makeRotationY(math.sin(time) * 0.2)
    program.setUniformMat4('mModel', mModel)


run("2DT904 - Rasterization", init, update)
