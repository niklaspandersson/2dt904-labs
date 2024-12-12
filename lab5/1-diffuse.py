from OpenGL.GL import *
from meshes import setupCube
from app import run, readFile
from glslprogram import Program
from matrix import Matrix

vsCode = readFile('./1-diffuse-vs.glsl')
fsCode = readFile('./1-diffuse-fs.glsl')


def init():
    global program
    global displayCount

    program = Program(vsCode, fsCode)
    program.use()

    displayCount = setupCube(program.programId)

    projection = Matrix.makePerspective()
    invCameraPos = Matrix.makeTranslation(0, 0, -4)
    mProjView = projection @ invCameraPos

    program.setUniformMat4('mProjView', mProjView)

    glEnable(GL_CULL_FACE)
    glEnable(GL_DEPTH_TEST)


def update(dt, time):
    speed = time * 0.2
    program.setUniformMat4('mModel', Matrix.makeRotationY(
        speed) @ Matrix.makeRotationZ(1.5*speed))
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glDrawArrays(GL_TRIANGLES, 0, displayCount)


run("2DT904 - Illumination", init=init, update=update)
