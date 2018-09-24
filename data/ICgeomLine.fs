uniform float uv_fade;

in vec2 texcoord;
in vec3 color;

out vec4 fragColor;

void main()
{
	fragColor = vec4(color, 1.);
	fragColor.a *= uv_fade;
}
