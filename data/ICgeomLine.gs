layout(triangles) in;
layout(line_strip, max_vertices = 4) out;

uniform mat4 uv_modelViewProjectionMatrix;

void main()
{

	
	vec4 pos = vec4(gl_in[0].gl_Position.x, gl_in[0].gl_Position.y, gl_in[0].gl_Position.z, 1.);
	gl_Position = uv_modelViewProjectionMatrix * pos;
	EmitVertex();
	gl_Position = uv_modelViewProjectionMatrix * vec4(pos.xy, pos.z-2450, 1.);
	EmitVertex();
	EndPrimitive();

}
