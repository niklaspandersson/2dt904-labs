from OpenGL.GL import *
from meshes import setupSquare
from app import run, readFile
import numpy as np
from glslprogram import Program
from matrix import Matrix
import pygame

vsCode = readFile('./shaders/lab6-1.vert')
fsCode = readFile('./shaders/lab6-1.frag')


def init():
    global program
    global vertexCount

    program = Program(vsCode, fsCode)
    program.use()

    # TODO: Load image data

    # TODO: Supply and describe the image to opengl

    vertexCount = setupSquare(program.programId)

    # TODO: Provide vextex UV-coordinates

    projection = Matrix.makePerspective()
    invCameraPos = Matrix.makeTranslation(0, 0, -4)
    mProjView = projection @ invCameraPos

    # TODO: set sampler uniform
    program.setUniformMat4('mProjView', mProjView)

    glEnable(GL_CULL_FACE)
    glEnable(GL_DEPTH_TEST)


def update(dt, time):
    speed = time * 0.3
    program.setUniformMat4('mModel', Matrix.makeRotationZ(speed))
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glDrawArrays(GL_TRIANGLES, 0, vertexCount)


run("2DT904 - Texturing", init=init, update=update)
