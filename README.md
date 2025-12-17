# Labs for 2dt904 (computer graphics), fall -25

This repository contains all the instructions and boilerplate code for the labs. The instructions for all labs will be published in the `instructions`-folder.

Please have a look at the instructions for lab1 on how to setup the python environment.

I recomend that you follow along with the book throughout the course and build the framework that they describe. That will give you a great starting point for the assignments, and for the parts of labs when you are supposed to experiment on you own. That said, the framework from the book will not be neccessary to complete the labs.

I will publish the instructions and boilerplate code for each lab in this respository. Feel free to do your labs in this repo or in a separate one. If you work directly in this one, be prepared to have to rebase whenever I've published something new or made any changes.

## Labs

### Lab 1

- Setting up the environment
- Displaying a window with pygame
- Minimal rendering with OpenGL

### Lab 2

- Provide vertex data describing an object to the graphics pipeline using `vertex attributes`
- Provide data that is shared for an entire object to the pipeline using `uniforms`

### Lab 3

- Provide various transformation matrices to the vertex shader.
- Perform time-based animations
- Draw multiple instances of a single object

### Lab 4

- Use of back-face culling and depth testing for hidden surface removal.
- Using uv coordinates to create a coordinate system in the plane of a surface.
- Using uv coordinates to procedurally "draw" on the surface of objects in the fragment shader.

### Lab 5

- Implementing the phong illumination model i GLSL
- Diffuse lighting
- Specular lighting

### Lab 6

- Loading images
- basic texturing and multitexturing
- filtering, wrapping and mipmaps

## Python dev. tips

There is a pip-package that automatically restart the application when file-changes are detected. It's called `py-mon`, and you can read about it here: https://pypi.org/project/py-mon/

1. With your python environment active, install it using `pip install py-mon` (or `python3 -m pip install py-mon` depending on your environment).
2. When developing, run your application from the terminal using `pymon [filename]` instead of using python directly.
3. Enjoy not having to manually run the application after each code update.
