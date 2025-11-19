from OpenGL.GL import *
import numpy as np
from glslprogram import fromSource
from app import run

vsCode = """
in vec3 position;
in vec3 vertexColor;
uniform float offset;

out vec3 color;
void main()
{
  gl_Position = vec4(position.x + offset, position.y, position.z, 1.0);
  color = vertexColor;
}
"""

fsCode = """
out vec4 fragColor;
in vec3 color;
void main()
{
  fragColor = vec4(color, 1.0);
}
"""


def init():
    vao = glGenVertexArrays(1)
    glBindVertexArray(vao)

    program = fromSource(vsCode, fsCode)
    glUseProgram(program)

    positions = [
        0.0, 0.8, 0.0,
        0.8, -0.8, 0.0,
        -0.8, -0.8, 0.0
    ]
    vertexData = glGenBuffers(1)
    glBindBuffer(GL_ARRAY_BUFFER, vertexData)

    # Copies to the currently bound buffer, so this must happen while vertexData is bound
    glBufferData(GL_ARRAY_BUFFER, np.array(
        positions, dtype=np.float32), GL_STATIC_DRAW)
    posLoc = glGetAttribLocation(program, "position")

    # Uses the currently bound buffer, so this must happen while vertexData is bound
    glVertexAttribPointer(posLoc, 3, GL_FLOAT, False, 0, None)
    glEnableVertexAttribArray(posLoc)

    colors = [
        1.0, 0.0, 0.0,
        0.0, 1.0, 0.0,
        0.0, 0.0, 1.0
    ]
    colorBuffer = glGenBuffers(1)
    glBindBuffer(GL_ARRAY_BUFFER, colorBuffer)

    # Copies to the currently bound buffer, so this must happen while colorBuffer is bound
    glBufferData(GL_ARRAY_BUFFER, np.array(
        colors, dtype=np.float32), GL_STATIC_DRAW)
    colorLoc = glGetAttribLocation(program, "vertexColor")

    # Uses the currently bound buffer, so this must happen while colorBuffer is bound
    glVertexAttribPointer(colorLoc, 3, GL_FLOAT, False, 0, None)
    glEnableVertexAttribArray(colorLoc)

    count = len(positions) // 3

    offsetLoc = glGetUniformLocation(program, 'offset')
    glUniform1f(offsetLoc, 0.5)

    glDrawArrays(GL_TRIANGLES, 0, count)


run('2DT904 - Providing vertex data', init)
