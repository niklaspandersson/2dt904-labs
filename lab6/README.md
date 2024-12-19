# Lab 5 - Texturing
In this lab you will:
1. Learn how to load images 
2. Learn how to provide image data to opengl
3. Use images (aka textures) in your shaders

## 1. TEXTURING BASICS - Code along
1. Open `1-simple-texture.py`
2. Load an image using pygame
3. Provide image data and description to opengl
4. Add a UV-coordinate vertex attribute
5. Sample the texture from the fragment shader

## 4. USING MULTIPLE TEXTURES - Code along
1. Save `1-simple-texture.py` as `2-multi-textures.py`
1. Save `1-fs.glsl` as `2-fs.glsl`
2. Extract code for loading an image into opengl to a function
3. Load a second image
4. Use both images in the shader

## 2. UV-coordinates - Try yourself
1. Go back to working in `1-simple-texture.py`
2. Change the uv-coordinates to only map the santa hat to the square

## 3. FILTERING AND WRAPPING - Try yourself
1. Keep working in `1-simple-texture.py`
2. Update the coordinates to 
```python
    uvData = [0.0, 0.0,  # B L
              2.0, 2.0,  # T R
              0.0, 2.0,  # T L

              2.0, 0.0,  # B R
              2.0, 2.0,  # T R
              0.0, 0.0]  # B L
```
3. Set the texture wrap parameters to try out different wrapping methods
4. Set the uvs to reapeat the texture 50 times over the square. Run the code to see the effect
5. Create and use mipmaps to mitigate the flickering
    1. Generate mipmaps after the call to glTexImage2D by invoking
    ```python
    glGenerateMipmap(GL_TEXTURE_2D)
    ```
    2. Set the `GL_TEXTURE_MIN_FILTER` parameter to `GL_LINEAR_MIPMAP_LINEAR`
