import pytest

from graphs.graph_adjacency_matrix import GraphAdjacencyMatrix

# Tests incorrect value handling
def test_matrix_creation():
    with pytest.raises(ValueError):
        matrix = GraphAdjacencyMatrix(edges = [[1,2,3]])
    with pytest.raises(ValueError):
        matrix = GraphAdjacencyMatrix(edges = [[1]])

# Test incorrect value catching in adding edge
def test_edge_addition():
    with pytest.raises(ValueError):
        matrix = GraphAdjacencyMatrix()
        matrix.add_edge(1, 2)
    #Directed
    with pytest.raises(ValueError, match=r"edge already exists between"):
        matrix = GraphAdjacencyMatrix(vertices = [1,2],edges = [[1,2],[1,2]])
    # Undirected
    with pytest.raises(ValueError, match=r"edge already exists between"):
        matrix = GraphAdjacencyMatrix(vertices = [1,2], edges = [[1,2],[2,1]])

#Test incorrect value catching when removing edge
def test_edge_removal():
    with pytest.raises(ValueError, match=r"Either"):
        matrix = GraphAdjacencyMatrix(vertices = [1])
        matrix.remove_edge(1, 2)
    with pytest.raises(ValueError, match=r"edge does NOT exist between"):
        matrix = GraphAdjacencyMatrix(vertices = [1,2])
        matrix.remove_edge(1, 2)