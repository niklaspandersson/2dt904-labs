from OpenGL.GL import *
from meshes import setupSquare
from app import run, readFile
import numpy as np
from glslprogram import Program
from matrix import Matrix
import pygame

vsCode = readFile('./1-vs.glsl')
fsCode = readFile('./1-fs-solution.glsl')


def init():
    global program
    global displayCount

    program = Program(vsCode, fsCode)
    program.use()

    # Load image data
    image = pygame.image.load("./images/xmaspot.png")
    image_data = pygame.image.tostring(image, "RGBA", True)
    width = image.get_width()
    height = image.get_height()

    # Supply and describe the image to opengl
    textureId = glGenTextures(1)
    textureIndex = 0
    glActiveTexture(GL_TEXTURE0 + textureIndex)
    glBindTexture(GL_TEXTURE_2D, textureId)
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, width, height,
                 0, GL_RGBA, GL_UNSIGNED_BYTE, image_data)
    glGenerateMipmap(GL_TEXTURE_2D)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_MIRRORED_REPEAT)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_MIRRORED_REPEAT)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER,
                    GL_LINEAR_MIPMAP_LINEAR)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)

    displayCount = setupSquare(program.programId)

    # Provide vextex UV-coordinates
    uvData = [0.0, 0.0,  # B L
              50.0, 50.0,  # T R
              0.0, 50.0,  # T L

              50.0, 0.0,  # B R
              50.0, 50.0,  # T R
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

    # set sampler uniform
    program.setUniformInt('tex', textureIndex)
    program.setUniformMat4('mProjView', mProjView)

    glEnable(GL_CULL_FACE)
    glEnable(GL_DEPTH_TEST)


def update(dt, time):
    speed = time * 0.3
    program.setUniformMat4('mModel', Matrix.makeRotationZ(speed))
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glDrawArrays(GL_TRIANGLES, 0, displayCount)


run("2DT904 - Texturing", init=init, update=update)
