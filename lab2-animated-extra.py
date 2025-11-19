from OpenGL.GL import *
import numpy as np
from glslprogram import fromSource
from app import run

# This in and all in, extra, no breaks example of what we can do now

vsCode = """
in vec3 position;
in vec3 vertexColor;
uniform vec3 offset;

out vec3 color;
void main()
{
  gl_Position = vec4(position + offset, 1.0);
  color = vertexColor;
}
"""

fsCode = """
out vec4 fragColor;
in vec3 color;
uniform vec3 colorOffset;
void main()
{
  fragColor = vec4(color + colorOffset, 1.0);
}
"""


def init():
    global program
    global count

    vao = glGenVertexArrays(1)
    glBindVertexArray(vao)

    program = fromSource(vsCode, fsCode)
    glUseProgram(program)

    # These triangles are smaller that in the original lab to make multiple triangles fit in the window
    positions = [
        0.0, 0.2, 0.0,
        0.2, -0.2, 0.0,
        -0.2, -0.2, 0.0
    ]
    # I've renamed this buffer for extra clarity and consistency
    positionBuffer = glGenBuffers(1)
    glBindBuffer(GL_ARRAY_BUFFER, positionBuffer)

    # Copies to the currently bound buffer, so this must happen while positionBuffer is bound
    glBufferData(GL_ARRAY_BUFFER, np.array(
        positions, dtype=np.float32), GL_STATIC_DRAW)
    posLoc = glGetAttribLocation(program, "position")

    # Uses the currently bound buffer, so this must happen while positionBuffer is bound
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


# Draw in a separate function that gets invoked repeatedly by the app function
# This function must accept two arguments:
# dt: the time-delta since the last call (in seconds)
# time: the current accumulated time (in seconds)


def render(dt, time):

    offsetLoc = glGetUniformLocation(program, 'offset')
    colorOffsetLoc = glGetUniformLocation(program, 'colorOffset')

    # When we animate, we need to clear the frame buffer between renders
    glClear(GL_COLOR_BUFFER_BIT)

    # Use an extra 3d vector uniform to also offset the colors values.
    # Uses cosine and time to get a periodic animation. Use different angular offsets and speed to vary red, green and blue in different pace
    glUniform3f(colorOffsetLoc, 0.5 + np.cos(1 + time*4)*0.5, 0.5 +
                np.cos(2 + time*3)*0.5, 0.5 + np.cos(5 + time*5)*0.5)

    speed = 2
    # Use a 3d vector for offset, Update the offset in a circular path based on time
    glUniform3f(offsetLoc, np.cos(time*speed)*0.4, np.sin(time*speed)*0.4, 0.0)

    # Draw one triangle
    glDrawArrays(GL_TRIANGLES, 0, count)

    # Use a different offset and draw the triangle again
    glUniform3f(offsetLoc, np.cos((2*np.pi/3.0)+time*speed) *
                0.4, np.sin((2*np.pi/3.0)+time*speed)*0.4, 0.0)
    glDrawArrays(GL_TRIANGLES, 0, count)

    # ...and again
    glUniform3f(offsetLoc, np.cos((4*np.pi/3.0)+time*speed) *
                0.4, np.sin((4*np.pi/3.0)+time*speed)*0.4, 0.0)
    glDrawArrays(GL_TRIANGLES, 0, count)

    # Observe that we don't update the colorOffset uniform between draw-calls, so the colors animate the same way on all triangles


# Provide the extra render-function to get callbacks every frame
# See the implementation of run fo details
run('2DT904 - Providing vertex data', init, render)
