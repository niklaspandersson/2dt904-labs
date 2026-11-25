from OpenGL.GL import *
import numpy as np
from ctypes import c_void_p


def setupTriangle(programId):
    posAttrLocation = glGetAttribLocation(programId, "position")
    colorAttrLocation = glGetAttribLocation(programId, "vertexColor")

    vao = glGenVertexArrays(1)
    glBindVertexArray(vao)

    positionData = [0.0, 1.0, 0.0,
                 1.0, -1.0, 0.0,
                 -1.0, -1.0, 0.0]

    vertexData = glGenBuffers(1)
    glBindBuffer(GL_ARRAY_BUFFER, vertexData)
    glBufferData(GL_ARRAY_BUFFER, np.array(
        positionData, dtype=np.float32), GL_STATIC_DRAW)
    glVertexAttribPointer(posAttrLocation, 3, GL_FLOAT, False, 0, None)
    glEnableVertexAttribArray(posAttrLocation)


    colorData = [1.0, 0.0, 0.0,
                 0.0, 1.0, 0.0,
                 0.0, 0.0, 1.0]
    if (colorAttrLocation != -1):
        colorBufferId = glGenBuffers(1)
        glBindBuffer(GL_ARRAY_BUFFER, colorBufferId)
        glBufferData(GL_ARRAY_BUFFER, np.array(
        colorData, dtype=np.float32), GL_STATIC_DRAW)
        glVertexAttribPointer(colorAttrLocation, 3, GL_FLOAT, False, 0, None)
        glEnableVertexAttribArray(colorAttrLocation)

    return len(positionData) // 3
