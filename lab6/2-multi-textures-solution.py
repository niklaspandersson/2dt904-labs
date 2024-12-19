from OpenGL.GL import *
from meshes import setupSquare
from app import run, readFile
import numpy as np
from glslprogram import Program
from matrix import Matrix
import pygame

vsCode = readFile('./1-vs.glsl')
fsCode = readFile('./2-fs-solution.glsl')


def loadTexture(slot, path):
    image = pygame.image.load(path)
    image_data = pygame.image.tostring(image, "RGBA", True)
    width = image.get_width()
    height = image.get_height()

    textureId = glGenTextures(1)

    glActiveTexture(GL_TEXTURE0 + slot)
    glBindTexture(GL_TEXTURE_2D, textureId)
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, width, height,
                 0, GL_RGBA, GL_UNSIGNED_BYTE, image_data)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)


def init():
    global program
    global displayCount

    program = Program(vsCode, fsCode)
    program.use()

    loadTexture(0, "./images/xmaspot.png")
    loadTexture(1, "./images/halloweenpot.png")

    displayCount = setupSquare(program.programId)

    # TODO: Provide vextex UV-coordinates
    uvData = [0.0, 0.0,  # B L
              1.0, 1.0,  # T R
              0.0, 1.0,  # T L

              1.0, 0.0,  # B R
              1.0, 1.0,  # T R
              0.0, 0.0]  # B L

    uvBuffer = glGenBuffers(1)
    glBindBuffer(GL_ARRAY_BUFFER, uvBuffer)
    glBufferData(GL_ARRAY_BUFFER, np.array(
        uvData, dtype=np.float32), GL_STATIC_DRAW)
    uvAttrLocation = glGetAttribLocation(program.programId, "vertexUV")
    glVertexAttribPointer(uvAttrLocation, 2, GL_FLOAT,
                          False, 2 * np.dtype(np.float32).itemsize, None)
    glEnableVertexAttribArray(uvAttrLocation)

    projection = Matrix.makePerspective()
    invCameraPos = Matrix.makeTranslation(0, 0, -4)
    mProjView = projection @ invCameraPos

    # TODO: set sampler uniform
    program.setUniformInt('tex0', 0)
    program.setUniformInt('tex1', 1)
    program.setUniformMat4('mProjView', mProjView)

    glEnable(GL_CULL_FACE)
    glEnable(GL_DEPTH_TEST)


def update(dt, time):
    speed = time * 0.3
    program.setUniformMat4('mModel', Matrix.makeRotationZ(speed))
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glDrawArrays(GL_TRIANGLES, 0, displayCount)


run("2DT904 - Texturing", init=init, update=update)
