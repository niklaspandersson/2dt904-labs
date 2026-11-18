import pygame
import numpy as np
from OpenGL.GL import *


def initializeShader(shaderCode, shaderType):
    shaderCode = '#version 330\n' + shaderCode

    ref = glCreateShader(shaderType)
    glShaderSource(ref, shaderCode)
    glCompileShader(ref)

    success = glGetShaderiv(ref, GL_COMPILE_STATUS)
    if not success:
        message = glGetShaderInfoLog(ref)
        glDeleteShader(ref)

        message = '\n' + message.decode('utf-8')
        raise Exception(message)
    return ref


def initializeProgram(vsCode, fsCode):
    vsRef = initializeShader(vsCode, GL_VERTEX_SHADER)
    fsRef = initializeShader(fsCode, GL_FRAGMENT_SHADER)

    ref = glCreateProgram()
    glAttachShader(ref, vsRef)
    glAttachShader(ref, fsRef)

    glLinkProgram(ref)

    success = glGetProgramiv(ref, GL_LINK_STATUS)
    if not success:
        message = glGetProgramInfoLog(ref)
        glDeleteProgram(ref)

        message = '\n' + message.decode('utf-8')
        raise Exception(message)

    return ref


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
  fragColor = vec4(1.0, 1.0, 0.0, 1.0);
}
"""


def main():
    # init pygame modules
    pygame.init()

    # use a core ogl profile for cross-platform compatibility
    pygame.display.gl_set_attribute(
        pygame.GL_CONTEXT_PROFILE_MASK, pygame.GL_CONTEXT_PROFILE_CORE)

    # create and display the window
    pygame.display.set_mode(
        [512, 512], pygame.DOUBLEBUF | pygame.OPENGL, vsync=1)
    pygame.display.set_caption("2DT904 - Describing objects")

    program = initializeProgram(vsCode, fsCode)
    glUseProgram(program)

    vao = glGenVertexArrays(1)
    glBindVertexArray(vao)

    positions = [
        0.0, 0.8, 0.0,
        -0.8, -0.8, 0.0,
        0.8, -0.8, 0.0
    ]

    # povide position data to openGL
    positionBuffer = glGenBuffers(1)
    glBindBuffer(GL_ARRAY_BUFFER, positionBuffer)

    # Copies to the currently bound buffer, so this must happen while positionBuffer is bound
    glBufferData(GL_ARRAY_BUFFER, np.array(positions, dtype=np.float32), GL_STATIC_DRAW)

     # Uses the currently bound buffer, so this must happen while positionBuffer is bound
    positionLocation = glGetAttribLocation(program, "position")
    glVertexAttribPointer(positionLocation, 3, GL_FLOAT, False, 0, None)
    glEnableVertexAttribArray(positionLocation)


    offsetLocation = glGetUniformLocation(program, "offset")
    glUniform1f(offsetLocation, 0.3)

    running = True
    while running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        glDrawArrays(GL_TRIANGLES, 0, 3)
        pygame.display.flip()

    pygame.quit()


main()
