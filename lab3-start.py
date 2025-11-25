from OpenGL.GL import *
from app import run, readFile
from glslprogram import Program
from meshes import setupTriangle

vsCode = readFile('./shaders/lab3-1.vert')
fsCode = readFile('./shaders/lab3.frag')


def init():
    program = Program(vsCode, fsCode)
    program.use()

    drawCount = setupTriangle(program.programId)
    glDrawArrays(GL_TRIANGLES, 0, drawCount)


run("2DT904 - Transformations", init)
