#version 330

uniform mat4 mModel;
uniform mat4 mProjView;
uniform float time;
in vec3 position;
out vec3 color;

float rand(vec2 co)
{
    return fract(sin(dot(co.xy ,vec2(12.9898,78.233))) * 43758.5453);
}

mat3 rotY(float angle) {
  float s = sin(angle);
  float c = cos(angle);

  return mat3(
    c, 0.0, s,
    0.0, 1.0, 0.0,
    -s, 0.0, c
  );
}
mat3 rotX(float angle) {
  float s = sin(angle);
  float c = cos(angle);

  return mat3(
    c, -s, 0.0,
    s, c, 0.0,
    0.0, 0.0, .01
  );
}

void main()
{
  int gridSize = 500;
  float size = 2.5;
  // Calculate big grid offset and smaller random offset
  vec3 offsetBig = vec3((gl_InstanceID % gridSize), 0, (gl_InstanceID / gridSize));
  vec3 offsetSmall = vec3(rand(offsetBig.xz), 0, rand(offsetBig.xz*2));
  vec3 offset = offsetBig * size + offsetSmall*50;

  // Move downwards over time, mod to create a looping effect (once below -200, jump back to 0)
  float speed = 10.0 + rand(offsetBig.xz)*50.0;
  offset.y = mod(-(time + rand(offsetBig.xz)*10) * speed, -200.0);

  // rotate based on time and some random factors
  float angleY = rand(offsetBig.xz*3)*3.14 + time * (1.0 + rand(offsetBig.xz)*20);
  float angleX = rand(offsetBig.xz*3)*3.14 + time * (2.0 + rand(offsetBig.xz)*5);
  vec3 rotated = rotY(angleY)*rotX(angleX) * position;

  //Apply transformations
  gl_Position = mProjView * mModel * vec4(rotated + offset, 1.0);

  // randomize colors based on instance ID
  float red = rand(vec2(gl_InstanceID+17))+0.3;
  float green = rand(vec2(gl_InstanceID+11))+0.3;
  float blue = rand(vec2(gl_InstanceID+23))+0.3;
  color = vec3(red, green, blue);
}