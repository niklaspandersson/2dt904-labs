in vec3 normal;
out vec4 fragColor;

const vec3 lightDir = vec3(0.0, 0.0, 1.0);
const vec3 color = vec3(1.0, 0.0, 0.0);

void main() {

  //diffuse lighting
  float diffuseAngle = dot(lightDir, normal);
  float intensity = max(diffuseAngle, 0);

  vec3 final_color = intensity * color;
  fragColor = vec4(final_color, 1.0);
}