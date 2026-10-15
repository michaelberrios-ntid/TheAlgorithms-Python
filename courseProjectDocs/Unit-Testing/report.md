# New Test Cases

author: Daniel Arcega

## Rationale
Based on the previous coverage report, files with lower coverage were investigated to find potential unit test locations.

## Graph Adjacency Matrix Test
 Tests located in graphs/tests/test_graph_adjacency_matrix.py
 
 Before, graph_adjacency_matrix.py already had a test method, TestGraphMatrix. However, it and its test methods were designed to be run specifically, and are not compatible with pytest.

 I have created pytest compatible tests that test some of the same behaviors
 Namely:
 * Initialization exception handling
 * Edge addition/removal exception handling
 * Vertex addition/removal exception handling

In the future, it may be useful to add more pytest compatible coverage.

## Binary Search
I noticed that the binary_search_with_duplicates() method contained its own definitions of lower_bound() and upper_bound().

I added inline doctests to cover their logic. Namely, do they return the correct index when the first is valid, when there are no valid ideces, etc.