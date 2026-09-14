# Requirements and Test Oracles

## Functional Requirements
1. The system shall use the Merge Sort algorithm to order a given unordered collection and return the collection in ascending order.
2. The system shall use the Julia Sets algorithm to generate and display a graphical representation of the calculated Julia set.
3. The system shall use the Quick Sort algorithm to order a given unordered collection and return the collection in ascending order.
4. The system shall use the Prime Check algorithm to accept a non-negative integer and determine whether the number is a prime number.

## Non-Functional Requirements
1. The system shall provide documentation for implemented algorithms that explains their purpose or provides a link to a source that does.
2. The system shall use the Prime Check algorithm to determine whether a number is prime with a time complexity of O(sqrt(n))

## Test Oracles

| Requirement ID | Requirement Description | Test Oracle (Expected Behavior) |
|-----------------------|-----------------------------------|---------------------------------------------|
| FR-1                   | The system shall use the Merge Sort algorithm to order a given unordered collection and return the collection in ascending order. | When Merge Sort on a collection of values, the method should return the sames values sorted in ascending order. |
| FR-2                  | The system shall use the Julia Sets algorithm to generate and display a graphical representation of the calculated Julia set. | When the Julia Sets algorithm is executed, matshow() should display a graphical representation of the calculated Julia set. |
| NFR-1              | The system shall provide documentation for implemented algorithms that explains their purpose and expected behavior. |All implemented algorithms must have either a short text explaining their purpose or a link to a source that does.|
| FR-3 | The system shall use the Quick Sort algorithm to order a given unordered collection and return the collection in ascending order. | When using Quick Sort on a collection of values, the method should return the same values sorted in ascending order. |
| FR-4 | The system shall use the Prime Check algorithm to accept a non-negative integer and determine whether the number is a prime number. | Using the Prime Check algorithm should return True when a number has exactly two factors, 1 and itself, and False otherwise. |
| NFR-2 | The system shall use the Prime Check algorithm to determine whether a number is prime with a time complexity of O(sqrt(n)). | When testing a number n, the Prime Check algorithm should only search for factors up to √n rather than up to n, using increments of 6 to reduce the number of checks. |
