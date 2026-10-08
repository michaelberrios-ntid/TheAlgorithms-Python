# New Test Cases

author: Daniel Arcega

## Rationale
Based on the previous coverage report, files with lower coverage were investigated to find potential unit test locations.

## Graph Adjacency Matrix Test
 Tests located in graphs/tests/test_graph_adjacency_matrix.py
 
I noticed that the handling of exceptions was not tested for correctness, so I added some for certain methods:
* Constructor
* add_edge
* remove_edge

These tests utilize pytest in order to check if the exceptions have been handled properly

## Binary Search
I noticed that the binary_search_with_duplicates() method contained its own definitions of lower_bound() and upper_bound().

I added inline doctests to cover their logic. Namely, do they return the correct index when the first is valid, when there are no valid ideces, etc.