from OpenGL.GL import *
from matrix import Matrix
from app import run, readFile
from glslprogram import Program
from meshes import setupCube
from math import pi

vsCode = readFile('./shaders/lab4-1.vert')
fsCode = readFile('./shaders/lab4-1.frag')


def init():
    global drawCount
    global program

    program = Program(vsCode, fsCode)
    program.use()

    drawCount = setupCube(program.programId, 2)

    projection = Matrix.makePerspective()
    invCameraPos = Matrix.makeTranslation(0, 0, -5)
    mProjView = projection @ invCameraPos

    program.setUniformMat4('mModel', Matrix.makeIdentity())
    program.setUniformMat4('mProjView', mProjView)

    # Enable depth testing and face culling
    glEnable(GL_CULL_FACE)
    glEnable(GL_DEPTH_TEST)


def update(dt, time):
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    # Draw cube near
    mModel = Matrix.makeRotationZ(
        time*pi / 2.5) @ Matrix.makeRotationX(time*pi / 5.5) @ Matrix.makeRotationY(pi / 3.5)
    program.setUniformMat4('mModel', mModel)
    glDrawArrays(GL_TRIANGLES, 0, drawCount)

    # Draw cube far
    # This will be occluded by the near cube, and should not be visible thanks to depth testing
    mModel = Matrix.makeTranslation(0, 0, -20) @ Matrix.makeRotationZ(
        time*pi / 5.5) @ Matrix.makeRotationX(time*pi / 5.5) @ Matrix.makeRotationY(pi / 5.5)
    program.setUniformMat4('mModel', mModel)
    glDrawArrays(GL_TRIANGLES, 0, drawCount)


run("2DT904 - Hidden surface removal", init, update)
