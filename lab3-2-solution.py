from OpenGL.GL import *
import math
from app import run, readFile
from matrix import Matrix
from glslprogram import Program
from meshes import setupTriangle

vsCode = readFile('./shaders/lab3-2.vert')
fsCode = readFile('./shaders/lab3.frag')


def init():
    global program
    global drawCount

    program = Program(vsCode, fsCode)
    program.use()

    drawCount = setupTriangle(program.programId)

    projection = Matrix.makePerspective()
    invCameraPos = Matrix.makeTranslation(0, 0, -5)
    mProjView = projection @ invCameraPos
    program.setUniformMat4('mProjView', mProjView)


def render(dt, time):
    glClear(GL_COLOR_BUFFER_BIT)

    mModel = Matrix.makeTranslation(
        math.sin(time*2), 0.0, 0.) @ Matrix.makeRotationX(time)
    program.setUniformMat4('mModel', mModel)
    program.setUniformFloat('time', time)

    glDrawArrays(GL_TRIANGLES, 0, drawCount)


run("2DT904 - Transformations", init, render)
