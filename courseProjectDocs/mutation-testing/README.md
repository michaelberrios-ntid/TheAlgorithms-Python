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
source_paths = [
  "web_programming/random_anime_character.py",
  "conversions/binary_to_decimal.py"
]

also_copy = [
    "web_programming/tests",
    "conversions/tests"
]

pytest_add_cli_args_test_selection = [
    "web_programming/tests/test_random_anime_character.py",
    "conversions/tests/test_binary_to_decimal.py"
]

pytest_command = "python -m pytest"
```
Can addtionally add `debug = true` to show the full test log

Add to `source_paths` and `pytest_add_cli_args_test_selection` if you want to mutate and test other files.

### 3. Run Mutation Testing

## Reset Mutants

Before re-running the mutation testing, you must reset the mutants to avoid getting results from cached mutants. To reset the mutants, run:
```bash
    rm -rf mutants/
```

## Create Mutants and run tests
```bash
    uv run mutmut run
```