# System Testing

## Sorting System Test
**author:** Daniel Arcega

**notebook:** `sorting-comparison.ipynb`

### Ideology
`TheAlgorithms/Python` is not designed to be imported and integrated
into another project. Instead, its purpose is to act as a standalone, educational collection of various algorithms and equations.
Therefore, my system test mimics how an investigative user would utilize the repository.

### Test Scope and Coverage
The `sorting-comparison` notebook tests the validity of implemented sorting algorithms, the ability to utilize different algorithms consecutively, 
and the ability to use this repository as a learning tool. It mimics how a user might use different algorithms to learn.

### Test Case Summary
|Title| Pre-conditions| Test Steps                                           | Expected Results                                                 |
------|---------------|------------------------------------------------------|------------------------------------------------------------------|
|Sorting Algorithm Comparison| User has access to TheAlgorithms/Python repository | Import relevant packages, write test code, run tests | All algorithms successfully run, data is collected and presented |

### Execution and results
Algorithm modules were imported with a 100% success rate. All methods were run without issue. Time data was processed and tabulated.

Of the 17 sorting methods, 16 methods correctly sorted all arrays. `comb_sort` was the lone outlier, resulting in a **94%** rate of success.

### How to run `sorting_comparison`
1. Ensure jupyter is installed on your repository
```
uv add --dev jupyter
```
2. Open `sorting_comparison.ipynb`
3. Run jupyter server
```angular2html
uv run --with jupyter jupyter lab
```

4. Attach the notebook to the kernel (various methods avaiable)
5. Run all cells