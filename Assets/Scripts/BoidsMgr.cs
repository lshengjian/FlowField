using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using System.Linq;
using System;
using Random = UnityEngine.Random;

public struct BoidData
{
    public Vector3 position;
    public Quaternion rotation;

    public Vector3 flockCenter;
    public Quaternion flockRot;
    public Vector3 separationHeading;

    public Matrix4x4 TRSMatrix;

    public static int Size
    {
        get
        {
            return sizeof(float) * (3 * 3 + 4 * 6);
        }
    }
}


public class BoidsMgr : MonoBehaviour
{
    const float lerpRation = 0.15f;
    [Header("Boid Attributes")]
    public int totalNum = 20;
    public float boidSpeed = 1;
    public float senseRadius = 10;

    public Mesh boidMesh;
    public Material boidMat;
    [Range(0.0f, 1.0f)]

    public float seperationWeight; //分离
    public float cohesionWeight; //内聚
    public float marchingWeight;//自身惯性

    public Vector3 unitScale = new Vector3(0.3f, 0.2f, 0.9f);



    [Header("Room Attributes")]
    public int roomSize = 40;

    [Header("Shader&Buffer")]
    public ComputeShader compute;
    ComputeBuffer m_boidBuffer;
    ComputeBuffer m_argsBuffer;
    private uint[] m_args = new uint[5] { 0, 0, 0, 0, 0 };
    private int m_kernelIndex;

    BoidData[] m_boids;

    private Vector3 m_roomOffset;

    private void Start()
    {
        m_boids = new BoidData[totalNum];
        m_roomOffset = new Vector3(-roomSize / 2, 0, -roomSize / 2);
        MakeBoids();
        InitializeComputeBuffer();
    }
    private void InitializeComputeBuffer()
    {
        if (boidMesh != null)
        {
            m_args[0] = (uint)boidMesh.GetIndexCount(0);
            m_args[1] = (uint)totalNum;
            m_args[2] = (uint)boidMesh.GetIndexStart(0);
            m_args[3] = (uint)boidMesh.GetBaseVertex(0);
        }
        m_argsBuffer = new ComputeBuffer(1, m_args.Length * sizeof(uint), ComputeBufferType.IndirectArguments);
        m_argsBuffer.SetData(m_args);

        m_boidBuffer = new ComputeBuffer(totalNum, BoidData.Size);

        boidMat.SetBuffer("boidsBuffer", m_boidBuffer);
        boidMat.SetVector("scale", unitScale);

        m_kernelIndex = compute.FindKernel("CSMain");
        compute.SetBuffer(m_kernelIndex, "boidBuffer", m_boidBuffer);
        compute.SetFloat("senseRad", senseRadius);
        compute.SetInt("totalNum", totalNum);
    }

    private void MakeBoids()
    {
        for (int i = 0; i < totalNum; i++)
        {
            BoidData boid = new BoidData();
            boid.position = GenRandomPos() + m_roomOffset;
            boid.rotation = GenRandomRot();
            m_boids[i] = boid;
            boid.TRSMatrix = Matrix4x4.TRS(boid.position, boid.rotation, unitScale);
        }
    }

    private void LateUpdate()
    {
        if (m_boids == null)
            return;
        m_boidBuffer.SetData(m_boids);
        compute.Dispatch(m_kernelIndex, totalNum / 64, 1, 1);
        m_boidBuffer.GetData(m_boids);

        // put result back to every boid
        for (int i = 0; i < totalNum; i++)
        {
            UpdateUnit(i);
        }

        Bounds bounds = new Bounds(Vector3.zero, Vector3.one * roomSize);
        Graphics.DrawMeshInstancedIndirect(boidMesh, 0, boidMat, bounds, m_argsBuffer);
       // Graphics.DrawMeshInstancedProcedural(boidMesh, 0, boidMat, bounds, totalNum);

    }


    public void UpdateUnit(int idx)
    {
        BoidData data = m_boids[idx];

        Vector3 acceleration = Vector3.zero;
        Vector3 cohesion = data.flockCenter - data.position;
        Vector3 forward = data.rotation * Vector3.forward;
        acceleration = data.separationHeading.normalized * seperationWeight
                       + cohesion.normalized * cohesionWeight
                       + forward * marchingWeight;
        Vector3 velocity = acceleration * Time.deltaTime * boidSpeed;
        Vector3.ClampMagnitude(velocity, boidSpeed);
        data.rotation = Quaternion.Lerp(data.rotation, data.flockRot, lerpRation);
        data.position += velocity;


        if (Mathf.Abs(data.position.x) >= roomSize / 2 ||
            Mathf.Abs(data.position.y) >= roomSize ||
            Mathf.Abs(data.position.z) >= roomSize / 2 ||
            data.position.y <= 0)
        {
            Vector3 tempPos = data.position - m_roomOffset;
            Func<Vector3, Vector3> normPosFunc = GetNormFunc((float a) => { return Mathf.Repeat(a, roomSize); });
            tempPos = normPosFunc(tempPos);
            data.position = tempPos + m_roomOffset;
        }

        data.TRSMatrix = Matrix4x4.TRS(data.position, data.rotation, unitScale);

        m_boids[idx] = data;

    }

    private void OnDisable()
    {
        m_boidBuffer.Release();
        m_argsBuffer.Release();
    }

    Func<Vector3, Vector3> GetNormFunc(Func<float, float> metaFunc)
    {
        return (Vector3 rawPos) =>
        {
            return new Vector3(metaFunc(rawPos.x), metaFunc(rawPos.y), metaFunc(rawPos.z));
        };
    }


    Vector3 GenRandomPos()
    {
        return new Vector3(Random.Range(0, roomSize), Random.Range(0, roomSize), Random.Range(0, roomSize));
    }

    Quaternion GenRandomRot()
    {
        return Quaternion.Euler(new Vector3(Random.Range(-180, 180), Random.Range(-180, 180), Random.Range(-180, 180)));
    }
    void PrintData()
    {
        int t = 0;
        foreach (BoidData boid in m_boids)
        {
            t++;
            Debug.Log(t);
            Debug.Log("cohesion:" + boid.flockCenter.ToString());
            Debug.Log("alignment:" + boid.rotation.ToString());
            Debug.Log("position:" + boid.position.ToString());
            Debug.Log("separation:" + boid.separationHeading.ToString());
        }
    }
}
