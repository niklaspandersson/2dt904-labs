from OpenGL.GL import *
from meshes import load
from app import run, readFile
from glslprogram import Program
from matrix import Matrix
from math import pi

vsCode = readFile('./2-specular-vs-solution.glsl')
fsCode = readFile('./2-specular-fs-solution.glsl')


def init():
    global program
    global displayCount

    program = Program(vsCode, fsCode)
    program.use()

    displayCount = load(program.programId, "./monkey")

    projection = Matrix.makePerspective()

    program.setUniformMat4('mProj', projection)

    glEnable(GL_CULL_FACE)
    glEnable(GL_DEPTH_TEST)


def update(dt, time):
    invCameraPos = Matrix.makeTranslation(0, 0, -4)
    speed = time * 0.7
    mViewModel = invCameraPos @ Matrix.makeRotationY(pi+speed)
    program.setUniformMat4(
        'mViewModel', mViewModel)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glDrawElements(GL_TRIANGLES, displayCount, GL_UNSIGNED_SHORT, None)


run("2DT904 - Illumination", init=init, update=update)
