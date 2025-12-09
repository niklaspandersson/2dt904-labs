from OpenGL.GL import *
from meshes import load
from app import run, readFile
from glslprogram import Program
from matrix import Matrix
from math import pi

vsCode = readFile('./shaders/lab5-2-solution.vert')
fsCode = readFile('./shaders/lab5-2-solution.frag')


def init():
    global program
    global displayCount

    program = Program(vsCode, fsCode)
    program.use()

    displayCount = load(program.programId, "./models/monkey")

    program.setUniformMat4('mProj', Matrix.makePerspective())

    glEnable(GL_CULL_FACE)
    glEnable(GL_DEPTH_TEST)


def update(dt, time):
    speed = time * 0.7
    mView = Matrix.makeTranslation(0, 0, -4)

    mModelView = mView @ Matrix.makeRotationY(
        pi+speed) @ Matrix.makeRotationX(pi/8)

    program.setUniformMat4(
        'mModelView', mModelView)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glDrawElements(GL_TRIANGLES, displayCount, GL_UNSIGNED_SHORT, None)


run("2DT904 - Illumination", init, update)
