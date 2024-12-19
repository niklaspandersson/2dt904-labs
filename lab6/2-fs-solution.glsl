in vec2 uv;
out vec4 fragColor;

uniform sampler2D tex0;
uniform sampler2D tex1;

void main() {
  vec4 color0 = texture(tex0, uv);
  vec4 color1 = texture(tex1, uv);

  // use the u-coordinate as blending factor
  float f = uv.x;

  // More examples of other ways to select between the textures

  // create a hard edge in the middle of the square
  // float f = step(0.5, uv.x);

  // create a hard edge based on the distance to the center of the square (where uv = (0.5, 0.5))
  // float f = step(1.0, distance(vec2(.5, .5), uv) * 2);

  // create a soft edge based on the distance to the center of the square (where uv = (0.5, 0.5))
  // float f = smoothstep(.9, 1.0, distance(vec2(.5, .5), uv) * 2);

  // blend the two textures using f as parameter
  vec4 final_color = mix(color0, color1, f);

  fragColor = final_color;
}