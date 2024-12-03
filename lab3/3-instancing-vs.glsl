uniform float time;
uniform mat4 mModel;
uniform mat4 mProjView;
in vec3 position;

out vec3 color;

float rand(vec2 co)
{
    return fract(sin(dot(co.xy ,vec2(12.9898,78.233))) * 43758.5453);
}

void main()
{
  vec2 instance_pos = vec2(gl_InstanceID / 4, gl_InstanceID % 4);
  vec3 offset = vec3(instance_pos, 0) * 2;
  float variataion = rand(instance_pos)*2;

  gl_Position = mProjView * mModel * vec4(position + offset + vec3(variataion, 0, 0), 1.0);
  color = vec3(variataion,fract(time), .8);
}