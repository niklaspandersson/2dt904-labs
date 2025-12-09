#version 330

out vec4 fragColor;

const vec3 surfaceColor = vec3(1.0, 0.0, 0.0);

// Directional light. The light hits all fragment from the same direction. Simulates a light source "infinitely" far away
const vec3 lightDir = vec3(1.0, 0.0, 2.0);
const vec3 lightColor = vec3(1.0, 1.0, 1.0);

const vec3 ambientIntensity = vec3(0.2);

in vec3 pos;
in vec3 normal;

void main() {
  vec3 N = normalize(normal);
  vec3 L = normalize(lightDir);
  vec3 V = normalize(-pos);
  vec3 R = reflect(-L, N);
  
  vec3 finalColor = vec3(0);

  /* ambient */
  finalColor += surfaceColor*ambientIntensity;

  /* diffuse */
  // use the dot product to get the cos of the angle between the surface normal and light direction. Use max with 0 to ensure that we don't get negative intensities for surfaces facing away from the light.
  float diffuseIntensity = max(0.0, dot(N, L));
  finalColor += surfaceColor*diffuseIntensity;

  /* specular */
  // only calculate specular reflections if the surface actually recieves light
  if(diffuseIntensity > 0.0) {
    float angle = max(dot(R, V), 0.0);
    float specularIntensity = pow(angle, 10.0);
    
    finalColor += lightColor * specularIntensity;
  }

  fragColor = vec4(finalColor, 1.0);
}