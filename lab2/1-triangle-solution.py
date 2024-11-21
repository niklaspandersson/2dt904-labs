from OpenGL.GL import *
import numpy as np
from glslprogram import fromSource
from app import run

vsCode = """
in vec3 position;
void main()
{
  gl_Position = vec4(position, 1.0);
}
"""

fsCode = """
out vec4 fragColor;
void main()
{
  fragColor = vec4(1.0, 1.0, 0.0, 1.0);
}
"""


def render():
    program = fromSource(vsCode, fsCode)
    posAttrLocation = glGetAttribLocation(program, "position")

    vao = glGenVertexArrays(1)
    glBindVertexArray(vao)

    positions = [0.0, 0.8, 0.0,
                 0.8, -0.8, 0.0,
                 -0.8, -0.8, 0.0]

    vertexData = glGenBuffers(1)
    glBindBuffer(GL_ARRAY_BUFFER, vertexData)
    glBufferData(GL_ARRAY_BUFFER, np.array(
        positions, dtype=np.float32), GL_STATIC_DRAW)
    glVertexAttribPointer(posAttrLocation, 3, GL_FLOAT, False, 0, None)
    glEnableVertexAttribArray(posAttrLocation)

    count = len(positions) // 3

    glUseProgram(program)
    glDrawArrays(GL_TRIANGLES, 0, count)


def render_noop():
    pass


run("2DT904 - providing data", render)
