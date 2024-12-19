from OpenGL.GL import *
import numpy as np
from ctypes import c_void_p


def setupTriangle(programId):
    posAttrLocation = glGetAttribLocation(programId, "position")

    vao = glGenVertexArrays(1)
    glBindVertexArray(vao)

    positions = [0.0, 1.0, 0.0,
                 1.0, -1.0, 0.0,
                 -1.0, -1.0, 0.0]

    vertexData = glGenBuffers(1)
    glBindBuffer(GL_ARRAY_BUFFER, vertexData)
    glBufferData(GL_ARRAY_BUFFER, np.array(
        positions, dtype=np.float32), GL_STATIC_DRAW)
    glVertexAttribPointer(posAttrLocation, 3, GL_FLOAT, False, 0, None)
    glEnableVertexAttribArray(posAttrLocation)

    return len(positions) // 3


def setupSquare(programId, sideLength=2):
    halfLen = sideLength / 2.0

    posAttrLocation = glGetAttribLocation(programId, "position")

    vao = glGenVertexArrays(1)
    glBindVertexArray(vao)

    # pos(vec3), uv(vec2)
    vertexData = [-halfLen, -halfLen, 0.0,  # L B
                  halfLen, halfLen, 0.0,  # R T
                  -halfLen, halfLen, 0.0,  # L T
                  halfLen, -halfLen, 0.0,  # R B
                  halfLen, halfLen, 0.0,  # R T
                  -halfLen, -halfLen, 0.0]  # L B
    NumComponents = 3

    vertexBuffer = glGenBuffers(1)
    glBindBuffer(GL_ARRAY_BUFFER, vertexBuffer)
    glBufferData(GL_ARRAY_BUFFER, np.array(
        vertexData, dtype=np.float32), GL_STATIC_DRAW)

    FloatSize = np.dtype(np.float32).itemsize
    glVertexAttribPointer(posAttrLocation, 3, GL_FLOAT,
                          False, NumComponents * FloatSize, c_void_p(0))
    glEnableVertexAttribArray(posAttrLocation)

    return len(vertexData) // NumComponents


def setupCube(programId, sideLength=2):
    halfLen = sideLength / 2.0

    P0 = np.array([-halfLen, -halfLen, -halfLen])
    P1 = np.array([halfLen, -halfLen, -halfLen])
    P2 = np.array([-halfLen, halfLen, -halfLen])
    P3 = np.array([halfLen, halfLen, -halfLen])
    P4 = np.array([-halfLen, -halfLen, halfLen])
    P5 = np.array([halfLen, -halfLen, halfLen])
    P6 = np.array([-halfLen, halfLen, halfLen])
    P7 = np.array([halfLen, halfLen, halfLen])

    C1, C2 = [1, 0.5, 0.5], [0.5, 0, 0]
    C3, C4 = [0.5, 1, 0.5], [0, 0.5, 0]
    C5, C6 = [0.5, 0.5, 1], [0, 0, 0.5]

    positionData = np.array([P5, P1, P3,
                             P5, P3, P7,

                             P0, P4, P6,
                             P0, P6, P2,

                             P6, P7, P3,
                             P6, P3, P2,

                             P0, P1, P5,
                             P0, P5, P4,

                             P4, P5, P7,
                             P4, P7, P6,

                             P1, P0, P2,
                             P1, P2, P3]).ravel().astype(np.float32)
    colorData = np.array([C1]*6 + [C2]*6 + [C3]*6 + [C4]
                         * 6 + [C5]*6 + [C6]*6).ravel().astype(np.float32)

    N1 = [1, 0, 0]
    N2 = [-1, 0, 0]
    N3 = [0, 1, 0]
    N4 = [0, -1, 0]
    N5 = [0, 0, 1]
    N6 = [0, 0, -1]

    normalData = np.array([N1]*6 + [N2]*6 + [N3]*6 + [N4]
                          * 6 + [N5]*6 + [N6]*6).ravel().astype(np.float32)

    posAttrLocation = glGetAttribLocation(programId, "position")
    colorAttrLocation = glGetAttribLocation(programId, "vertexColor")
    normalAttrLocation = glGetAttribLocation(programId, "vertexNormal")

    vao = glGenVertexArrays(1)
    glBindVertexArray(vao)

    positionBufferId = glGenBuffers(1)
    glBindBuffer(GL_ARRAY_BUFFER, positionBufferId)
    glBufferData(GL_ARRAY_BUFFER, positionData, GL_STATIC_DRAW)

    glVertexAttribPointer(posAttrLocation, 3, GL_FLOAT, False, 0, None)
    glEnableVertexAttribArray(posAttrLocation)

    if (colorAttrLocation != -1):
        colorBufferId = glGenBuffers(1)
        glBindBuffer(GL_ARRAY_BUFFER, colorBufferId)
        glBufferData(GL_ARRAY_BUFFER, colorData, GL_STATIC_DRAW)
        glVertexAttribPointer(colorAttrLocation, 3, GL_FLOAT, False, 0, None)
        glEnableVertexAttribArray(colorAttrLocation)

    if (normalAttrLocation != -1):
        normalBufferId = glGenBuffers(1)
        glBindBuffer(GL_ARRAY_BUFFER, normalBufferId)
        glBufferData(GL_ARRAY_BUFFER, normalData, GL_STATIC_DRAW)
        glVertexAttribPointer(normalAttrLocation, 3, GL_FLOAT, False, 0, None)
        glEnableVertexAttribArray(normalAttrLocation)

    return len(positionData) // 3


def load(programId, path):

    posAttrLocation = glGetAttribLocation(programId, "position")
    normalAttrLocation = glGetAttribLocation(programId, "vertexNormal")

    vao = glGenVertexArrays(1)
    glBindVertexArray(vao)

    vertexdata = np.loadtxt(
        path + "-vertices.txt").ravel().astype(np.float32)
    indices = np.loadtxt(path + "-indices.txt").ravel().astype(np.uint16)
    print(vertexdata.size)
    print(indices.size)

    indexBuffer = glGenBuffers(1)
    glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, indexBuffer)
    glBufferData(GL_ELEMENT_ARRAY_BUFFER, indices, GL_STATIC_DRAW)

    vertexBuffer = glGenBuffers(1)
    glBindBuffer(GL_ARRAY_BUFFER, vertexBuffer)
    glBufferData(GL_ARRAY_BUFFER, vertexdata, GL_STATIC_DRAW)
    glVertexAttribPointer(posAttrLocation, 3, GL_FLOAT,
                          False, 8 * 4, c_void_p(0))
    glVertexAttribPointer(normalAttrLocation, 3, GL_FLOAT,
                          False, 8 * 4, c_void_p(3*4))
    glEnableVertexAttribArray(posAttrLocation)
    glEnableVertexAttribArray(normalAttrLocation)

    return len(indices)
