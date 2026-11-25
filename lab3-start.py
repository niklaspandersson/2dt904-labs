import pygame
from OpenGL.GL import *
from glslprogram import Program
from matrix import Matrix
from meshes import setupTriangle

def readFile(name: str):
    with open(name, encoding='utf-8') as f:
        return f.read()
    
vsCode = readFile('./shaders/lab3.vert')
fsCode = readFile('./shaders/lab3.frag')

def main():
    # init pygame modules
    pygame.init()

    # use a core ogl profile for cross-platform compatibility
    pygame.display.gl_set_attribute(
        pygame.GL_CONTEXT_PROFILE_MASK, pygame.GL_CONTEXT_PROFILE_CORE)

    # create and display the window
    pygame.display.set_mode(
        [512, 512], pygame.DOUBLEBUF | pygame.OPENGL, vsync=1)
    pygame.display.set_caption("2DT904 - Transformations")

    program = Program(vsCode, fsCode)
    program.use()
    drawCount = setupTriangle(program.programId)

    mModel = Matrix.makeTranslation(0.5, 0.0, 0.) @ Matrix.makeScale(0.5)
    program.setUniformMat4('mModel', mModel)

    running = True
    while running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        glDrawArrays(GL_TRIANGLES, 0, drawCount)
        pygame.display.flip()

    pygame.quit()

main()
