# New Test Cases for graph_adjacency_matrix.py and binary_search.py

author: Daniel Arcega

## Rationale
Based on the previous coverage report, files with lower coverage were investigated to find potential unit test locations.

## Test Results
Of the 5 tests run, 5 tests pass.

## Graph Adjacency Matrix Test
 Tests located in graphs/tests/test_graph_adjacency_matrix.py
 
 Before, graph_adjacency_matrix.py already had a test method, TestGraphMatrix. However, it and its test methods were designed to be run specifically, and are not compatible with pytest.

 I have created pytest compatible tests that test some of the same behaviors
 Namely:
 * Initialization exception handling
 * Edge addition/removal exception handling
 * Vertex addition/removal exception handling

In the future, it may be useful to add more pytest compatible coverage.

# Coverage Update
| Version | Statements | Missing Stmts | Branches | Partial Branches | Coverage |
| ------- | ------- | ------- | ------- | ------- | ------- |
| Old | 260 | 13 | 102 | 6 | 95% |
| New | 260 | 7 | 102 | 3 | 97% |

The additional tests led to a 2% improvement in coverage.

## Binary Search
I noticed that the binary_search_with_duplicates() method contained its own definitions of lower_bound() and upper_bound().

I added inline doctests to cover their logic. The tests were based on boundary value analysis, covering the max/min values as well as their predecessors.

Due to the way the coverage statistics are gathered, the only change in the coverage is reducing the number of missing lines.
| Version | Statements | Missing Stmts | Branches | Partial Branches | Coverage |
| ------- | ------- | ------- | ------- | ------- | ------- |
| Old and New | 118 | 25 | 60 | 8 | 78% |

