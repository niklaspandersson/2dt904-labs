# Lab 5 - Texturing

In this lab you will:

1. Learn how to load images
2. Learn how to provide image data to opengl
3. Use images (aka textures) in your shaders

## 0. PREPARE - Try yourself

Before the lab starts, please try to find time to:

1. Make sure that you have a version of the lab repo containing the boilerplate for lab 6.
   - Check that you now have an `images`-folder with two png-images in it.
   - Also, note that the glslprogam.py contains a new method for setting integer uniforms: `setUniformInt`

## 1. TEXTURING BASICS - Code along

1. **Open `lab6-1-start.py`**
2. **Load an image using pygame**
   1. Pygame have a simple api for working with images. With that, we can load an image, get its width and height, and also get a datastructure tailored for openGL containing all the pixels in the image
   ```python
   image = pygame.image.load("./images/xmaspot.png")
   image_data = pygame.image.tostring(image, "RGBA", True)
   width = image.get_width()
   height = image.get_height()
   ```
3. **Provide image data and description to opengl**. Just like when we provide vertex data to opengl, providing a texture requires quite a few steps:
   1. We need to create a texture "object" and bind it.
      ```python
      textureId = glGenTextures(1)
      glActiveTexture(GL_TEXTURE0)
      glBindTexture(GL_TEXTURE_2D, textureId)
      ```
   2. We need to upload the actual data
      ```python
      glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, width, height, 0, GL_RGBA, GL_UNSIGNED_BYTE, image_data)
      ```
   3. Finally we tell opengl what kind of filtering we want for the texture
      ```python
      glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
      glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
      ```
4. **Sample the texture from the fragment shader**. To do that, we need to:
   1. provide a uniform telling the shader which _texture unit_ to sample from.
      ```python
      program.setUniformInt('tex', 0)
      ```
   2. declare a corresponding _sampler_ uniform in the fragment shader
      ```glsl
      uniform sampler2D tex;
      ```
   3. use the built-in `texture()` function to sample from the bound texture
      ```glsl
      fragColor = texture(tex, uv);
      ```

## 2. USING MULTIPLE TEXTURES - Code along

1. **Load a second image**
2. **Use both images in the shader**
   1. We can interpolate the colors of both texture
   1. We can choose one texture at a time
   1. We can combine the textures in any other way. If you've ever used an image editing software you probably know abound "blend modes", we can implement any of those using simple arithmetics.
3. **Using a second set of uv-coordinates** Since we never unbind the vertex array object describing our square, we can "easily" create and describe a new buffer with additional vertex attributes, straight in our init-function.

   1. Define the data for the second pair of uv-coordinates

      ```python
      uvData = [0.0, 0.0,  # B L
               1.0, 1.0,  # T R
               0.0, 1.0,  # T L

               1.0, 0.0,  # B R
               1.0, 1.0,  # T R
               0.0, 0.0]  # B L
      ```

   2. Create and bind a buffer object for the new attribute
      ```python
      uvBuffer = glGenBuffers(1)
      glBindBuffer(GL_ARRAY_BUFFER, uvBuffer)
      ```
   3. Upload the data to opengl
      ```python
      glBufferData(GL_ARRAY_BUFFER, np.array(
      uvData, dtype=np.float32), GL_STATIC_DRAW)
      ```
   4. Describe the data and bind it to a vertex attribute input to the shader
      ```python
      uvAttrLocation = glGetAttribLocation(program.programId, "vertexUV2")
      glVertexAttribPointer(uvAttrLocation, 2, GL_FLOAT,
                        False, 2 * np.dtype(np.float32).itemsize, None)
      glEnableVertexAttribArray(uvAttrLocation)
      ```

## 3. UV-coordinates - Try yourself

1. Try changing the uv-coordinates to only map the santa hat to the square

## 4. FILTERING AND WRAPPING - Try yourself

1. Update the second set of coordinates to

   ```python
       uvData = [0.0, 0.0,  # B L
               2.0, 2.0,  # T R
               0.0, 2.0,  # T L

               2.0, 0.0,  # B R
               2.0, 2.0,  # T R
               0.0, 0.0]  # B L
   ```

2. Update the fragment shader to use a simple sample from one of the textures as fragColor, using `uv2` for uv-coordinates.

3. Set the texture wrap parameters to try out different wrapping methods. Add the following after the call to `glTexImage2D`

   ```python
   # OpenGL sometimes refers to the UV-coordinates as S and T respectively
   glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
   glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
   ```

   1. Try exchanging `GL_REPEAT` for other options. `GL_MIRRORED_REPEAT` and `GL_CLAMP_TO_EDGE`
   2. Try using different values for `GL_TEXTURE_WRAP_S` and `GL_TEXTURE_WRAP_T`.

4. Set the uvs to repeat the texture 50 times over the square. Run the code to see the effect
5. Create and use mipmaps to mitigate the flickering
   1. Generate mipmaps after the call to `glTexImage2D` by invoking
   ```python
   glGenerateMipmap(GL_TEXTURE_2D)
   ```
   2. Set the `GL_TEXTURE_MIN_FILTER` parameter to `GL_LINEAR_MIPMAP_LINEAR`. Run the code to see the effect
