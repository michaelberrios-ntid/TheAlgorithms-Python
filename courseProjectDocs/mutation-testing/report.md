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
```
⠼ Generating mutants
    done in 290ms (1 files mutated, 0 ignored, 0 unmodified)
⠸ Running stats     
    done
⠴ Running clean tests
    done
⠦ Running forced fail test
    done
Running mutation testing
⠏ 82/82  🎉 51 🫥 0  ⏰ 0  🤔 0  🙁 31  🔇 0  🧙 0
13.28 mutations/second
```
| Total Mutants | Killed | Survived |
|---------------|--------|----------|
|82 | 51| 31       |

## Analysis and Response
Of the surviving mutants, 3 were mutants of the save_image() function while the remaining 28 were of random_anime_character()

### save_image()
Of the 3 mutants, 2 survived do to tests not checking if None parameters were passed into `httpx.get()`
The other mutant was due to a change in which timeout length was given. This mutant was ignored, as the timeout could realistically be many values aside from None.

### random_anime_character()
Multiple surviving mutants were located within the `Beautiful_Soup()` call. Similar to the mutants in `save_image()`, the parameters of `httpx.get()` were not verified.
Furthermore, the string parameter was not verified either.


To kill these mutants, the existing `test_save_image()` and `test_random_anime_character()` test methods were modified with additional functionality.

## Results
```
⠏ Listing all tests 
⠋ Running clean tests
    done
⠙ Running forced fail test
    done
Running mutation testing
⠸ 82/82  🎉 63 🫥 0  ⏰ 0  🤔 0  🙁 19  🔇 0  🧙 0
3.80 mutations/second
```
| Total Mutants | Killed | Survived |
|---------------|--------|----------|
|82 | 63     | 19       |