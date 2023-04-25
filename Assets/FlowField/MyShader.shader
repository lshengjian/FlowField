Shader "example/point cloud mesh to direction" {
Properties
{
	_Size ("Width", float) = 0.2
}

SubShader
{
	LOD 200
	Tags { "Queue" = "Transparent" "RenderType" = "Transparent" }
	Blend SrcAlpha OneMinusSrcAlpha
	Pass
	{
		CGPROGRAM
		#pragma vertex vert
		#pragma fragment frag
		#pragma geometry geom
		#include "UnityCG.cginc"

		struct vertexIn {
			float4 pos : POSITION;
			float4 color : COLOR;
		};
		struct vertexOut {
			float4 pos : SV_POSITION;
			float4 color : COLOR0;
		};
		struct geomOut {
			float4 pos : POSITION;
			float4 color : COLOR0;
		};

		float _Size;


		vertexOut vert ( vertexIn i )
		{
			vertexOut o;
			o.pos = UnityObjectToClipPos(i.pos);
			o.color = i.color;
			return o;
		}
		[maxvertexcount(6)]
		void geom ( point vertexOut IN[1] , inout LineStream<geomOut> lineStream )
		{
			vertexOut vertex = IN[0];
			const float2 points[6] = { float2(0,0) , float2(1,0),
			float2(1,0),float2(0.8,-0.12),
			float2(1,0),float2(0.8,0.12) };
			float2 pmul = float2( _Size*(_ScreenParams.y / _ScreenParams.x) , _Size ) * 0.5;
			
			geomOut newVertex;
			//newVertex.color = vertex.color;
			for( int i=0 ; i<6 ; i++ )
			{
				newVertex.pos = vertex.pos + float4( points[i]*pmul , 0 , 0 );
				//float3 pos=vertex.pos.xyz;
				newVertex.color=float4(1,0,0,1);//float4(abs(pos),1);
				lineStream.Append( newVertex );
			}
		}
/*
		[maxvertexcount(4)]
		void geom ( point vertexOut IN[1] , inout TriangleStream<geomOut> triStream )
		{
			vertexOut vertex = IN[0];
			const float2 points[4] = { float2(1,-1) , float2(1,1) , float2(-1,-1) , float2(-1,1) };
			float2 pmul = float2( _Size*(_ScreenParams.y / _ScreenParams.x) , _Size ) * 0.5;
			
			geomOut newVertex;
			newVertex.color = vertex.color;
			for( int i=0 ; i<4 ; i++ )
			{
				newVertex.pos = vertex.pos + float4( points[i]*pmul , 0 , 0 );
				triStream.Append( newVertex );
			}
		}
*/
		float4 frag ( geomOut i ) : COLOR
		{
			return i.color;
		}
		
		ENDCG
	}
}
	FallBack Off
}