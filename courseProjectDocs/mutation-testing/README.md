# Mutation Testing

author: Daniel Arcega

## Steps to run mutation testing
### 1. Ensure mutmut is installed on your version of the repository.
```bash 
   uv add --dev mutmut
   uv sync
```

### 2. Configure project.toml
Add these lines to project.toml
```bash
[tool.mutmut]
source_paths = [ "web_programming/random_anime_character.py" ]
pytest_add_cli_args_test_selection= [ "tests/test_random_anime_character_mutant.py" ]
pytest_command = "python -m pytest"
```
Add to `source_paths` and `pytest_add_cli_args_test_selection` if you want to mutate and test other files.

### Create Mutants and run tests
```bash
    uv run mutmut run
```