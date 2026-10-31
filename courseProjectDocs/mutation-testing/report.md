# Mutation Test Report

author: Daniel Arcega

## Mutation Tool: mutmut
Since TheAlgorithms-Python did not utilize mutation testing before, we had the ability to choose which framework to use. 
We chose mutmut due to it being simple to run and its capabilities. You can configure which files to mutate, and mutmut will
automatically gather those files as well as any test files that cover them.

### Config
```bash
    [tool.mutmut]
    source_paths = [ <paths to gather files to mutate from> ]
    pytest_add_cli_args_test_selection= [ <paths to tests> ]
    pytest_command = "python -m pytest"
```

## Intial Mutation Report
| Total Mutants | Killed | Missed |
|---------------|--------|--------|
|82 | 51| 31|

## Analysis and Response