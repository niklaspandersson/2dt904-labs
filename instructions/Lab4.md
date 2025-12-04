# Lab 4 - Hidden surfaces and fragment shading

In this lab you will:

1. See the effect of hidden surface removal
2. Explore various ways in which we can use maths to draw in the fragment shader

## 0. PREPARE - Try yourself

Before the lab starts, please try to find time to:

1. Make sure that you have a version of the lab repo containing the boilerplate for lab 4.
1. Get familiar with the boilerplate:
   - the `setupCube` function in `meshes.py`
1. Make sure that you understand and can run the `lab4-1-start.py` and `lab4-2-start.py` files

## 1. HIDDEN SURFACE REMOVAL - Code along

1. Run `lab4-1-start.py` to see the problem
   - Press `space` to pause the animation to try to figure out how it can look the way it does
2. The initial OpenGL state has no strategies for hidden surface removal enabled. Which means that it is only the order in which the primitives are drawn that determine what is drawn "on top". When we have a convex shape like this cube, enabling back-face culling will fix the problem, since no front-facing side will ever obscure another front-facing side.
   - Enable `back-face culling` by invoking `glEnable(GL_CULL_FACE)`. This will cull back-facing triangles by default.
   - When we do that, only front-facing triangles will be rasterized and rendered, which will solve our issues.
3. Back-face culling is usually not sufficient for correctness though. Lets draw another cube behind the one we already have, to see the problem.

   - Copy the section "Draw cube near" to create a "Draw cube far" and put that at the end of `update`
   - Add a translation of -20 in z to the mModel matrix as the last transformation beeing applies. Also change the rotation speed of the far cube by updating the factors in the `MakeRotation` arguments
   - Again it wrongly appears in front. We now have front-facing surfaces that obsure other front-facing surfaces, and we're back to relaying on the order in which the primitives are beeing drawn. To solve this once and for all, we also need a `z-buffer`
   - If you want to convince yourself that the current behaviour is order dependent, try moving the drawing of the far cube before the near cube. But be sure to move it back afterward again so that we can see the effect of depth testing later.

4. Tell OpenGL to use a `z-buffer` by enabling `depth testing`
   - `glEnable(GL_DEPTH_TEST)`
   - We also need to clear the z-buffer each frame, just like the color buffer. Update the argument to `glClear` to include the `GL_DEPTH_BUFFER_BIT`.

## 2. FRAGMENT SHADER - Code along

1. Start over with `lab4-2-start.py`.
2. Examine the `setupSquare` function in `meshes.py`. Each vertex has an extra 2d-coordinate attribute. Take some minutes and try to figure out how they are layed out, and what the purpose of those coordinates are. Remember that they are vertex attributes, and will thus be interpolated for each pixel in the square.
3. Before we can use the so called `uv` coordinates, we need to pass them through the pipeline. Start in the vertex-shader.
4. In the fragment-shader, declare the corresponding input and use it as the red- and green components of the color for now.
5. Now we have a coordinate system that is fixed on the surface. No matter how we animate or orient the surface, the uv-coordinates will be locked in place on the surface. Let's add some animation to the plane to show this.

   1. Add a mModel matrix in the update function and animate a rotation around one of the axis using `math.sine` and `time` as a parameter. For instance:

      `mModel = Matrix.makeRotationY(math.sin(time) * math.pi / 4)`

   2. Make sure to pass the `mModel` matrix to the shader program using the uniform.

6. With the uv-coordinates we can now procedurally define how the surface should look. glsl provides a plethoria of interesting functions that we can use. Some examples:

   1. `mix()` is for interpolating two values
   2. With `step()` you get either 0 or 1 depending on a threshold
   3. `smoothStep()` is similar to step, but instead of a hard threshold you have a range in which you get a smooth interpolation between 0 or 1.
   4. `step` and `smoothStep` are great for generating weight to use in `mix`
   5. We can use `fract()` and `floor` to subdivide the coordinate system.
   6. Finally `distance` gets the distance between two points, which is useful for creating circles among other things.

## 3. FRAGMENT SHADER - Try yourself

`The book of shaders` is a great resource for this kind of algorithmic (or procedural) drawing

- [https://thebookofshaders.com/] (specifically the section "Algorithmic drawing")

1. Try to draw a swedish flag
   - Change to a danish flag by changing the colors
   - Try animating between them using `mix` and some periodic function like sine or cosine
2. Try to animate the uv coordinates in the vertex shader (before they reach the fragment shader)
