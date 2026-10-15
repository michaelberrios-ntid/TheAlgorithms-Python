import pytest
import random

from graphs.graph_adjacency_matrix import GraphAdjacencyMatrix, TestGraphMatrix

# Tests incorrect value handling
def test_matrix_creation_exception():
    with pytest.raises(ValueError, match=r"must have length 2"):
        matrix = GraphAdjacencyMatrix(vertices=[], edges = [[1,2,3]])
    with pytest.raises(ValueError, match=r"must have length 2"):
        matrix = GraphAdjacencyMatrix(vertices = [], edges = [[1]])

# Test incorrect value catching in adding edge
def test_edge_addition_exception():
    with pytest.raises(ValueError, match=r"Either"):
        matrix = GraphAdjacencyMatrix(vertices = [],edges = [])
        matrix.add_edge(1, 2)
    #Directed
    with pytest.raises(ValueError, match=r"edge already exists between"):
        matrix = GraphAdjacencyMatrix(vertices = [1,2],edges = [[1,2],[1,2]])
    # Undirected
    with pytest.raises(ValueError, match=r"edge already exists between"):
        matrix = GraphAdjacencyMatrix(vertices = [1,2], edges = [[1,2],[2,1]], directed = False)

# Test incorrect value catching when removing edge
def test_edge_removal_exception():
    with pytest.raises(ValueError, match=r"Either"):
        matrix = GraphAdjacencyMatrix(vertices = [1],edges = [])
        matrix.remove_edge(1, 2)
    with pytest.raises(ValueError, match=r"edge does NOT exist between"):
        matrix = GraphAdjacencyMatrix(vertices = [1,2],edges = [])
        matrix.remove_edge(1, 2)

# Test incorrect value catching when adding vertex
def test_vertex_addition_exception():
    test_vertices = random.sample(range(1, 100), 10)
    matrix = GraphAdjacencyMatrix(vertices = test_vertices,edges = [])
    with pytest.raises(ValueError, match=r"already exists in this graph"):
        for v in test_vertices:
            matrix.add_vertex(v)

# Test incorrect value catching when removing vertex
def test_vertex_removal_exception():
    test_vertices = random.sample(range(1, 100), 10)
    matrix = GraphAdjacencyMatrix(vertices=[], edges=[])
    with pytest.raises(ValueError, match=r"does not exist in this graph"):
        for v in test_vertices:
            matrix.remove_vertex(v)
