from OpenGL.GL import *
from meshes import load
from app import run, readFile
from glslprogram import Program
from matrix import Matrix
from math import pi, cos, sin

vsCode = readFile('./shaders/lab5-3-solution.vert')
fsCode = readFile('./shaders/lab5-3-solution.frag')


def init():
    global program
    global displayCount
    global mView

    program = Program(vsCode, fsCode)
    program.use()

    displayCount = load(program.programId, "./models/monkey")

    program.setUniformMat4('mProj', Matrix.makePerspective())
    program.setUniformFloat('gloss', 150.0)

    glEnable(GL_CULL_FACE)
    glEnable(GL_DEPTH_TEST)


def update(dt, time):
    mView = Matrix.makeTranslation(0, 0, -4)

    # Rotate light position in the Z=5 plane with a radius of 4 units ("in a circle in front of the model")
    angle = -time*4
    lightDistanceFromOrigin = 4
    lightPosWorld = [lightDistanceFromOrigin *
                     cos(angle), lightDistanceFromOrigin * sin(angle), 5, 1]

    # calculate light position in camera space and pass to shader
    lightPosCamera = mView @ lightPosWorld
    program.setUniformVec4('lightPos', lightPosCamera)

    mModelView = mView @ Matrix.makeRotationY(
        -pi*3.0/4) @ Matrix.makeRotationX(time*pi/8)
    program.setUniformMat4('mModelView', mModelView)

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glDrawElements(GL_TRIANGLES, displayCount, GL_UNSIGNED_SHORT, None)


run("2DT904 - Illumination", init, update)
