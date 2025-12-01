#version 330

uniform mat4 mModel;
uniform mat4 mProjView;
uniform float time;
in vec3 position;

void main()
{
  gl_Position = mProjView * mModel * vec4(position, 1.0);
}