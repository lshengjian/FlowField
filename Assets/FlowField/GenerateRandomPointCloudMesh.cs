using UnityEngine;
using Random = Unity.Mathematics.Random;
[RequireComponent(typeof(MeshFilter), typeof(MeshRenderer))]
public class GenerateRandomPointCloudMesh : MonoBehaviour
{
    //public float K = 0.2f;
    Mesh _mesh;
    [SerializeField] int _numSideVerties = 20;
    void Awake()
    {
        _mesh = new Mesh();
        int total = _numSideVerties * _numSideVerties;
        int half = _numSideVerties / 2;
        //var rnd = new Random( (uint) System.DateTime.Now.GetHashCode() );
        // Vector3[] vertices = new Vector3[_numSideVerties];
        // for( int i=0 ; i<_numSideVerties ; i++ )
        // 	vertices[i] = rnd.NextFloat3( -Vector3.one , Vector3.one );
        Vector3[] vertices = new Vector3[total];
        int cnt = 0;
        for (int i = 0; i < _numSideVerties; i++)
            for (int j = 0; j < _numSideVerties; j++)
                vertices[cnt++] = new Vector3((i * 1.0f - half) / half, (j * 1.0f - half) / half, 0);


        _mesh.vertices = vertices;

        int[] indices = new int[_mesh.vertices.Length];
        for (int i = 0; i < indices.Length; i++)
            indices[i] = i;

        var mf = GetComponent<MeshFilter>();
        _mesh.SetVertices(vertices);
        _mesh.SetIndices(indices, MeshTopology.Points, 0);
        mf.sharedMesh = _mesh;
    }
    void OnDestroy()
    {
        if (_mesh != null) Destroy(_mesh);
    }
}