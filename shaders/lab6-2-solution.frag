#version 330

in vec2 uv;
in vec2 uv2;
out vec4 fragColor;

uniform sampler2D tex;
uniform sampler2D tex2;

void main() {
  vec4 color1 =  texture(tex, uv);
  vec4 color2 =  texture(tex2, uv2);

  // float f = uv.x;

  // More examples of other ways to select between the textures

  // create a hard edge in the middle of the square
  float f = step(0.5, uv.x);

  // create a hard edge based on the distance to the center of the square (where uv = (0.5, 0.5))
  // float f = step(1.0, distance(vec2(.5, .5), uv) * 2);

  // create a soft edge based on the distance to the center of the square (where uv = (0.5, 0.5))
  // float f = smoothstep(.9, 1.0, distance(vec2(.5, .5), uv) * 2);

  // blend the two textures using f as parameter

  fragColor = mix(color1, color2, f);
}