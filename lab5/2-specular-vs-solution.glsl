uniform mat4 mProj;
uniform mat4 mViewModel;
in vec3 position;
in vec3 vertexNormal;

out vec3 normal;
out vec3 pos;
void main() {
  // does calculations in camera space instead
  vec4 cameraSpacePos = mViewModel * vec4(position, 1.0);
  gl_Position = mProj * cameraSpacePos;

  vec4 worldNormal = mViewModel * vec4(vertexNormal, 0.0);
  normal = worldNormal.xyz;
  pos = cameraSpacePos.xyz;
}