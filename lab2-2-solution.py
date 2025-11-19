from OpenGL.GL import *
import numpy as np
from glslprogram import fromSource
from app import run

vsCode = """
in vec3 position;
uniform float offset;
void main()
{
  gl_Position = vec4(position.x + offset, position.y, position.z, 1.0);
}
"""

fsCode = """
out vec4 fragColor;
void main()
{
  fragColor = vec4(1.0, 0.0, 1.0, 1.0);
}
"""


def init():

    # create a vertex array object to hold
    vao = glGenVertexArrays(1)
    glBindVertexArray(vao)

    # The actual vertex position data
    # three vertices with three components each: x, y and z
    positions = [
        0.0, 0.8, 0.0,
        0.8, -0.8, 0.0,
        -0.8, -0.8, 0.0
    ]

    # Create and bind an opengl buffer for the position data
    vertexData = glGenBuffers(1)
    glBindBuffer(GL_ARRAY_BUFFER, vertexData)

    # Fill the currently bound buffer with the data, using np to make the data compatible with opengl. So this must happen while the buffer vertexData is bound
    glBufferData(GL_ARRAY_BUFFER, np.array(
        positions, dtype=np.float32), GL_STATIC_DRAW)

    # Compile, link and activate a glsl program defined by the provided vertex- and fragment-shader source code
    program = fromSource(vsCode, fsCode)
    glUseProgram(program)

    # Queries the glsl-program for the location where it will look for data for the "in vec3 position" variable
    posLoc = glGetAttribLocation(program, "position")

    # Ties the currently bound buffer object to the location for the "position" variable. So this must happen while the buffer vertexData is bound. Also describes how the data is layed out in the buffer.
    glVertexAttribPointer(posLoc, 3, GL_FLOAT, False, 0, None)

    # Tells opengl to actually use the data tied to the specific location
    glEnableVertexAttribArray(posLoc)

    # Queries the glsl-program for the location where it will look for data for the "uniform float offset" variable
    offsetLoc = glGetUniformLocation(program, 'offset')

    # Provide data to that location
    glUniform1f(offsetLoc, 0.5)

    count = 3
    # Run pipeline using the data and glsl-program that we've provided above
    # Tell it to render triangles, and that we want it to process count (3) vertices
    # This call inplies explicit encoding. So, if we want to render multiple triangles, we have to provide data for 3 extra vertices for each extra triangle
    glDrawArrays(GL_TRIANGLES, 0, count)


run('2DT904 - Providing vertex data', init)
