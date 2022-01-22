from turtle import color
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
def drawCube(startPoint,size,ax,color):
    """
    Draws a cube.
    """
    # Create the vertices
    vertices = createVertices(startPoint,size)
    # Create the faces
    faces = createFaces(vertices)
    # Draw the faces
    for face in faces:
        for edge in range(len(face)):
            ax.plot([face[edge][0], face[(edge + 1) % len(face)][0]],
                    [face[edge][1], face[(edge + 1) % len(face)][1]],
                    [face[edge][2], face[(edge + 1) % len(face)][2]], c=color)
    return ax
def createVertices(startPoint,size):
    """
    Creates the vertices for a rectangular prism.
    """
    # Create the vertices
    vertices = []
    vertices.append(startPoint)
    vertices.append([startPoint[0]+size[0],startPoint[1],startPoint[2]])
    vertices.append([startPoint[0]+size[0],startPoint[1]+size[1],startPoint[2]])
    vertices.append([startPoint[0],startPoint[1]+size[1],startPoint[2]])
    vertices.append([startPoint[0],startPoint[1],startPoint[2]+size[2]])
    vertices.append([startPoint[0]+size[0],startPoint[1],startPoint[2]+size[2]])
    vertices.append([startPoint[0]+size[0],startPoint[1]+size[1],startPoint[2]+size[2]])
    vertices.append([startPoint[0],startPoint[1]+size[1],startPoint[2]+size[2]])
    return vertices
def createFaces(vertices):
    """
    Creates the faces for a rectangular prism.
    """
    # Create the faces
    faces = []
    faces.append([vertices[0],vertices[1],vertices[2],vertices[3]])
    faces.append([vertices[0],vertices[4],vertices[5],vertices[1]])
    faces.append([vertices[0],vertices[3],vertices[7],vertices[4]])
    faces.append([vertices[1],vertices[5],vertices[6],vertices[2]])
    faces.append([vertices[2],vertices[6],vertices[7],vertices[3]])
    faces.append([vertices[4],vertices[7],vertices[6],vertices[5]])
    return faces


