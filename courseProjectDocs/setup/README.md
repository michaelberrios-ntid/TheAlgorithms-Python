# How to Run Tests

### 1. Install uv

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### 2. Load uv into the Current Shell

```bash
source ~/.bashrc
```

### 3. Verify uv

```bash
uv --version
```

The output should display the installed version of `uv`. For example:

```text
uv 0.12.23 (x86_64-unknown-linux-gnu)
```

### 4. Go into the TheAlgorithms-Python Repository

```bash
cd TheAlgorithms-Python
```

### 5. Install Python and Project Testing Dependencies

The repository specifies the required Python version in the `.python-version` file. `uv` will automatically install the required Python version, create the virtual environment, and install the project and testing dependencies.

```bash
uv sync --group test
```

During setup, `uv` should indicate that it is using a free-threaded version of Python 3.14 and creating the `.venv` virtual environment. For example:

```text
Using CPython 3.14.8+freethreaded
Creating virtual environment at: .venv
```

The exact Python patch version may be different.

### 6. Verify the Environment

Verify that the repository specifies Python `3.14t`:

```bash
cat .python-version
```

Expected output:

```text
3.14t
```

Verify the Python version being used by the project:

```bash
uv run python --version
```

Expected output:

```text
Python 3.14.x
```

The patch version may vary. For example, the tested environment used `Python 3.14.8`.

Verify that the Python interpreter is the free-threaded (`3.14t`) build:

```bash
uv run python -c "import sysconfig; print(sysconfig.get_config_var('Py_GIL_DISABLED'))"
```

Expected output:

```text
1
```

A value of `1` confirms that the free-threaded Python build is being used.

Verify that `pytest` was installed with the testing dependencies:

```bash
uv run python -m pytest --version
```

Expected output:

```text
pytest 9.x.x
```

For example, the tested environment used:

```text
pytest 9.1.1
```

### 7. Set the CI Environment Variable

Set the `CI` environment variable so that tests requiring a CI environment, such as the Instagram-related test, behave appropriately.

```bash
export CI=true
```

Verify that the environment variable was set:

```bash
echo $CI
```

Expected output:

```text
true
```

> **Note:** `export CI=true` applies only to the current shell session. If the terminal is closed, run the command again before running the tests.

### 8. Run the Tests

```bash
uv run --with=pytest-run-parallel pytest \
  --iterations=8 \
  --parallel-threads=auto \
  --ignore-gil-enabled \
  --ignore=courseProjectDocs \
  --ignore=courseProjectCode \
  --ignore=computer_vision/cnn_classification.py \
  --ignore=computer_vision/flip_augmentation.py \
  --ignore=computer_vision/harris_corner.py \
  --ignore=computer_vision/mosaic_augmentation.py \
  --ignore=data_compression/peak_signal_to_noise_ratio.py \
  --ignore=digital_image_processing/ \
  --ignore=docs/conf.py \
  --ignore=dynamic_programming/k_means_clustering_tensorflow.py \
  --ignore=machine_learning/lstm/lstm_prediction.py \
  --ignore=neural_network/input_data.py \
  --ignore=project_euler/ \
  --ignore=quantum/q_fourier_transform.py \
  --ignore=scripts/validate_solutions.py \
  --ignore=web_programming/current_stock_price.py \
  --ignore=web_programming/fetch_anime_and_play.py \
  --ignore=scripts/validate_filenames.py \
  --cov-report=term-missing:skip-covered \
  --cov=. .
```

A successful test run should complete without test failures.

### 9. Clean Up After Testing

After testing is complete, the testing environment and installed tools can be removed if they are no longer needed.

#### Remove the Project Virtual Environment

From inside the `TheAlgorithms-Python` repository, remove the `.venv` directory:

```bash
rm -rf .venv
```

This removes the project's installed dependencies, including `pytest`, `pytest-cov`, and other packages installed by `uv sync`.

Verify that the virtual environment was removed:

```bash
ls -a | grep .venv
```

If `.venv` was successfully removed, this command should return no output.

#### Remove the uv-Managed Python Installation

Check which Python versions are managed by `uv`:

```bash
uv python list
```

Look for the installed free-threaded Python 3.14 version. It may appear similar to:

```text
cpython-3.14.x+freethreaded-linux-x86_64-gnu
```

Remove the free-threaded Python 3.14 installation:

```bash
uv python uninstall 3.14t
```

Verify that it was removed:

```bash
uv python list
```

The Python 3.14 free-threaded entry should now show:

```text
<download available>
```

> **Note:** Do not remove Ubuntu's system Python installation, such as `/usr/bin/python3`.

#### Remove the CI Environment Variable

The `CI` variable can be removed from the current shell with:

```bash
unset CI
```

Verify that it was removed:

```bash
echo $CI
```

Expected output:
The command should return a blank line.

The `CI` variable is temporary, so closing the terminal also removes it.

#### Remove uv

If `uv` was installed only for this testing process and is no longer needed, remove the installed `uv` and `uvx` executables:

```bash
rm -f ~/.local/bin/uv ~/.local/bin/uvx
```

Verify that `uv` is no longer available:

```bash
uv --version
```

Expected output should indicate that the command cannot be found, for example:

```text
uv: command not found
```

> **Note:** If `uv` was already installed before following these instructions or is used for other Python projects, do not remove it.

#### Repository

The `TheAlgorithms-Python` repository itself is not removed by the steps above.

If the repository was cloned only for this testing process and is no longer needed, move to its parent directory and remove it:

```bash
cd ..
rm -rf TheAlgorithms-Python
```

Only run this command if there are no files or changes in the repository that need to be kept.