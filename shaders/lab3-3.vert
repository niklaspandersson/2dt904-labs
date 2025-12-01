#version 330

uniform mat4 mModel;
uniform mat4 mProjView;
uniform float time;
in vec3 position;
out vec3 color;

float rand(vec2 co)
{
    return fract(sin(dot(co.xy ,vec2(12.9898,78.233))) * 43758.5453);
}

void main()
{
  int gridSize = 4;
  float size = 2.5;
  vec3 offset = vec3((gl_InstanceID % gridSize)*size, (gl_InstanceID / gridSize)*size, 0.0) - vec3(gridSize / 2, gridSize / 2, 0.0);

  gl_Position = mProjView * mModel * vec4(position + offset, 1.0);

  float red = rand(vec2(gl_InstanceID+17))+0.3;
  float green = rand(vec2(gl_InstanceID+11))+0.3;
  float blue = rand(vec2(gl_InstanceID+23))+0.3;
  color = vec3(red, green, blue);
}