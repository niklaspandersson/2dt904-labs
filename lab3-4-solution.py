from OpenGL.GL import *
import math
from app import run, readFile
from matrix import Matrix
from glslprogram import Program
from meshes import setupTriangle

vsCode = readFile('./shaders/lab3-4.vert')
fsCode = readFile('./shaders/lab3-3.frag')


def init():
    global program
    global drawCount

    program = Program(vsCode, fsCode)
    program.use()

    drawCount = setupTriangle(program.programId)

    projection = Matrix.makePerspective()
    invCameraPos = Matrix.makeTranslation(0, 0, -255)
    mProjView = projection @ invCameraPos
    program.setUniformMat4('mProjView', mProjView)


def render(dt, time):
    glClear(GL_COLOR_BUFFER_BIT)

    mModel = Matrix.makeTranslation(
        -200.0, 80.0, 0.0)
    program.setUniformMat4('mModel', mModel)
    program.setUniformFloat('time', time)

    glDrawArraysInstanced(GL_TRIANGLES, 0, drawCount, 500*500)


run("2DT904 - Transformations", init, render)
