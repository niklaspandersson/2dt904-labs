# Lab 5 - Lighting
In this lab you will:
1. Implement the phong illumination model in glsl

## 1. DIFFUSE LIGHTING - Code along
1. Run `1-diffuse.py` to see why lighting is often required when we do 3d graphics
2. Examine `setupCube` to see that it provides both normals and colors that we can user
3. The vertex shader need to pass the normals along to the fragment shader
4. The fragment shader needs to calculate the angle between the surface normal and light direction to determine the intensity of the reflected light. Care must be taken to make sure that these directions are in the same coordinate space.
5. Use the surface color along with the calculated intensity to determine the final color of the pixel
6. Change from constant surface color to use the available vertex color data

## 2. SPECULAR LIGHTING - Code along
1. Run `2-specular.py` to "see" our new model
2. Copy the code for diffuse lighting from the `1-diffuse` shader program.
3. What extra data do we need for the specular reflection?
4. Again, we need to make sure to have all our positions / directions in the same coordinate system
5. Calculate the reflected diretion of the light
6. Calculate the specular term from the phong model
7. Use the specular intensity along with the light color to compute the specular contribution to the final pixel color
8. Add all components together

## 3. EXPERIMENT - Try yourself
1. Experiment with the glossiness and light color
2. Try to change from directional light to point light. What has to be changed?
3. Extract constants from the shaders to uniforms
4. Try to animate the position of the light, have it circle around the world origin (where the object is located)