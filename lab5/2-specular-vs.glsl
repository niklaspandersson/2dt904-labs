uniform mat4 mProjView;
uniform mat4 mModel;
in vec3 position;

void main() {
  gl_Position = mProjView * mModel * vec4(position, 1.0);
}