#version 330

uniform mat4 mProj;
uniform mat4 mModelView;
in vec3 position;
in vec3 vertexNormal;

out vec3 normal;
out vec3 pos;
void main() {
  vec4 cameraSpacePosition = mModelView * vec4(position, 1.0);
  gl_Position = mProj * cameraSpacePosition;
  

  vec4 homoNormal = vec4(vertexNormal, 0.0);
  vec4 rotatedNormal = mModelView * homoNormal;

  pos = cameraSpacePosition.xyz;
  normal = rotatedNormal.xyz;
}