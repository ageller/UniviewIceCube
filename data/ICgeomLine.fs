uniform float uv_fade;

in vec2 texcoord;
uniform vec4 lineColor;

out vec4 fragColor;

void main()
{
	fragColor = lineColor;
	fragColor.a *= uv_fade;
}
