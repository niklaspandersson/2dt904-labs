#version 330

uniform mat4 mProjView;
uniform mat4 mModel;
in vec3 position;
in vec2 vertexUV;
in vec2 vertexUV2;

out vec2 uv;
out vec2 uv2;
void main() {
  gl_Position = mProjView * mModel * vec4(position, 1.0);
  uv = vertexUV;
  uv2 = vertexUV2;
}