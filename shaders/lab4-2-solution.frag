#version 330
in vec2 uv;
uniform float t;

out vec4 fragColor;
void main() {
  const vec3 color1 = vec3(0.12, 0.31, 0.87);
  const vec3 color2 = vec3(0.92, 0.91, 0.14);

  // GRADIENT
  // float weight = uv.x;
  // vec3 col = mix(color1, color2, weight);

  // CROSS
  float weight_left = step(0.35, uv.x);
  float weight_right = 1-step(0.45, uv.x);
  float weight_col = weight_left*weight_right;

  float weight_top = step(0.45, uv.y);
  float weight_bottom = 1-step(0.55, uv.y);
  float weight_row = weight_top*weight_bottom;

  float weight = min(1.0, weight_col + weight_row);
  vec3 col = mix(color1, color2, weight);

  // CHECKERBOARD
  // float checkCount = 5.0;
  // vec2 pos = floor(uv * checkCount);
  // float weight = mod(pos.x + pos.y, 2.0);
  // vec3 col = mix(color1, color2, weight);

  // SUBDIVIDE
  // float subDivs = 10.0;
  // vec2 uv_small = fract(uv * subDivs);
  // vec3 col = vec3(uv_small, 0.0);

  // CIRCLES
  // float dist = distance(uv*2, vec2(1.0));
  // float weight = step(0.8, dist);
  // vec3 col = vec3(weight);

  fragColor = vec4(col, 1.0);
}