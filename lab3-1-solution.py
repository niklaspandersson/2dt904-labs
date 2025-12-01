from OpenGL.GL import *
from app import run, readFile
from matrix import Matrix
from glslprogram import Program
from meshes import setupTriangle

vsCode = readFile('./shaders/lab3-1.vert')
fsCode = readFile('./shaders/lab3.frag')


def init():
    program = Program(vsCode, fsCode)
    program.use()

    drawCount = setupTriangle(program.programId)

    mModel = Matrix.makeTranslation(0.5, 0.0, 0.) @ Matrix.makeRotationX(1.5)
    program.setUniformMat4('mModel', mModel)

    projection = Matrix.makePerspective()
    invCameraPos = Matrix.makeTranslation(0, 0, -5)
    mProjView = projection @ invCameraPos

    program.setUniformMat4('mProjView', mProjView)
    glDrawArrays(GL_TRIANGLES, 0, drawCount)


run("2DT904 - Transformations", init)
