uniform mat4 mProjView;
uniform mat4 mModel;
in vec3 position;
in vec3 vertexNormal;

out vec3 normal;
void main() {
  gl_Position = mProjView * mModel * vec4(position, 1.0);

  vec4 worldNormal = mModel * vec4(vertexNormal, 0.0);
  normal = worldNormal.xyz;
}