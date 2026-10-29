from OpenGL.GL import *
from meshes import setupSquare
from app import run, readFile
import numpy as np
from glslprogram import Program
from matrix import Matrix
import pygame

vsCode = readFile('./shaders/lab6-1.vert')
fsCode = readFile('./shaders/lab6-1-solution.frag')


def init():
    global program
    global vertexCount

    program = Program(vsCode, fsCode)
    program.use()

    # 1. Load image data
    image = pygame.image.load("./images/xmaspot.png")
    image_data = pygame.image.tostring(image, "RGBA", True)
    width = image.get_width()
    height = image.get_height()

    # 2. Supply and describe the image to opengl
    textureId = glGenTextures(1)
    glActiveTexture(GL_TEXTURE0)
    glBindTexture(GL_TEXTURE_2D, textureId)
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, width, height,
                 0, GL_RGBA, GL_UNSIGNED_BYTE, image_data)

    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER,
                    GL_NEAREST)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)

    # glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    # glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)

    vertexCount = setupSquare(program.programId)

    # TODO: part 2 - Provide second set of vertex UV-coordinates

    projection = Matrix.makePerspective()
    invCameraPos = Matrix.makeTranslation(0, 0, -4)
    mProjView = projection @ invCameraPos

    # 3. set sampler uniform
    program.setUniformMat4('mProjView', mProjView)
    program.setUniformInt('tex', 0)

    glEnable(GL_CULL_FACE)
    glEnable(GL_DEPTH_TEST)


def update(dt, time):
    speed = time * 0.3
    program.setUniformMat4('mModel', Matrix.makeRotationZ(speed))
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glDrawArrays(GL_TRIANGLES, 0, vertexCount)


run("2DT904 - Texturing", init=init, update=update)
