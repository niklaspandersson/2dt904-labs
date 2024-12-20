from OpenGL.GL import *
from matrix import Matrix
from app import run, readFile
from glslprogram import Program
from meshes import setupTriangle
from math import pi

vsCode = readFile('./lab3/1-transformations-vs.glsl')
fsCode = readFile('./lab3/varying-color-fs.glsl')


def init():
    global program
    global drawCount

    program = Program(vsCode, fsCode)
    program.use()

    drawCount = setupTriangle(program.programId)

    mModel = Matrix.makeTranslation(.5 , .5, 0.) @ Matrix.makeScale(.5) @ Matrix.makeRotationZ(pi / 2.432)  
    program.setUniformMat4('mModel', mModel)

    projection = Matrix.makePerspective()
    invCameraPos = Matrix.makeTranslation(0,0,-10)
    mProjView = projection @ invCameraPos

    program.setUniformMat4('mProjView', mProjView)


def update(dt, time):
    glDrawArrays(GL_TRIANGLES, 0, drawCount)


run("2DT904 - Transformations", init=init, update=update, screenSize=[512,512])
