# How to run tests:

### 1. Install uv


### 2. Load uv into the current shell

### 3. Verify uv
uv --version

### 4. Go into TheAlgorithms-Python repository
cd TheAlgorithms-Python

### 5. Install the Python version specified by the repository
uv python install 3.14

### 6. Install the project dependencies + testing dependencies
uv sync --python 3.14 --group test

### 7. Verify the environment
uv run python --version
uv run python -m pytest --version

### 8. Run this command
uv run --with=pytest-run-parallel pytest   --iterations=8   --parallel-threads=auto   --ignore-gil-enabled   --ignore=courseProjectDocs --ignore=courseProjectCode   --ignore=computer_vision/cnn_classification.py   --ignore=computer_vision/flip_augmentation.py   --ignore=computer_vision/harris_corner.py   --ignore=computer_vision/mosaic_augmentation.py   --ignore=data_compression/peak_signal_to_noise_ratio.py   --ignore=digital_image_processing/   --ignore=docs/conf.py   --ignore=dynamic_programming/k_means_clustering_tensorflow.py   --ignore=machine_learning/lstm/lstm_prediction.py   --ignore=neural_network/input_data.py   --ignore=project_euler/   --ignore=quantum/q_fourier_transform.py   --ignore=scripts/validate_solutions.py   --ignore=web_programming/current_stock_price.py   --ignore=web_programming/fetch_anime_and_play.py  --ignore=scripts/validate_filenames.py --cov-report=term-missing:skip-covered   --cov=. .
