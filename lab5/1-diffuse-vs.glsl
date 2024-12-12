uniform mat4 mProjView;
uniform mat4 mModel;
in vec3 position;

out vec3 normal;
void main() {
  gl_Position = mProjView * mModel * vec4(position, 1.0);
}