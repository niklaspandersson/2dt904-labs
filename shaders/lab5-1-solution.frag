#version 330

out vec4 fragColor;

const vec3 color = vec3(1.0, 0.0, 0.0);
const vec3 lightDir = vec3(1.0, 0.0, 2.0);

const vec3 ambient = vec3(0.2, 0.2, 0.2);

in vec3 normal;
void main() {
  vec3 N = normalize(normal);
  vec3 L = normalize(lightDir);

  float intensity = max(0.0, dot(N, L));

  vec3 finalColor = vec3(0);
  finalColor += ambient*color;
  finalColor += color*intensity;

  fragColor = vec4(finalColor, 1.0);
}