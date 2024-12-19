in vec3 normal;
in vec3 pos;
out vec4 fragColor;

const vec3 lightDir = vec3(0.0, 0.0, 1.0);
const vec3 color = vec3(1.0, 0.0, 0.0);
const vec3 lightColor = vec3(1.0, 1.0, 0.0);

void main() {
  vec3 N = normalize(normal);
  vec3 L = normalize(lightDir);
  vec3 V = normalize(-pos);

  //diffuse lighting
  float diffuseAngle = dot(L, N);
  float diff_intensity = max(diffuseAngle, 0);

  // specular lighting
  float specular = 0.0;
  if(diff_intensity > 0.0) {
    vec3 R = reflect(-L, N);
    float angle = dot(R, V);
    float spec_intensity = max(angle, 0);
    specular = pow(spec_intensity, 32.0);
  }

  vec3 final_color = diff_intensity * color;
  final_color += lightColor * specular;

  fragColor = vec4(final_color, 1.0);
}