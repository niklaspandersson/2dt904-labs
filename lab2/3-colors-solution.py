from OpenGL.GL import *
import numpy as np
from glslprogram import fromSource
from app import run

vsCode = """
uniform float offset;
in vec3 position;
in vec3 vertexColor;

out vec3 color;
void main()
{
  gl_Position = vec4(position.x + offset, position.y, position.z, 1.0);
  color = vertexColor;
}
"""

fsCode = """
in vec3 color;
out vec4 fragColor;
void main()
{
  fragColor = vec4(color, 1.0);
}
"""


def render():
    program = fromSource(vsCode, fsCode)
    posAttrLocation = glGetAttribLocation(program, "position")
    colorAttrLocation = glGetAttribLocation(program, "vertexColor")

    vao = glGenVertexArrays(1)
    glBindVertexArray(vao)

    positions = [0.0, 0.8, 0.0,
                 0.8, -0.8, 0.0,
                 -0.8, -0.8, 0.0]

    colors = [1.0, 0.0, 0.0,
              0.0, 1.0, 0.0,
              0.0, 0.0, 1.0]

    posAttrData = glGenBuffers(1)
    glBindBuffer(GL_ARRAY_BUFFER, posAttrData)
    glBufferData(GL_ARRAY_BUFFER, np.array(
        positions, dtype=np.float32), GL_STATIC_DRAW)
    glVertexAttribPointer(posAttrLocation, 3, GL_FLOAT, False, 0, None)
    glEnableVertexAttribArray(posAttrLocation)

    colorAttrData = glGenBuffers(1)
    glBindBuffer(GL_ARRAY_BUFFER, colorAttrData)
    glBufferData(GL_ARRAY_BUFFER, np.array(
        colors, dtype=np.float32), GL_STATIC_DRAW)
    glVertexAttribPointer(colorAttrLocation, 3, GL_FLOAT, False, 0, None)
    glEnableVertexAttribArray(colorAttrLocation)

    count = len(positions) // 3

    glUseProgram(program)
    offsetLocation = glGetUniformLocation(program, 'offset')
    glUniform1f(offsetLocation, 1.0)

    glDrawArrays(GL_TRIANGLES, 0, count)


run("2DT904 - providing data", render)
