# Video Player in Python

This is a simple application which plays Video and Audio using PyQt5 in python.

### Setup the Environment in your system

- Install Python

This project is written in Python and uses PyQt5 for GUI. So, you need to install Python first. This project is tested on Python 3.12.13.

- Clone the repository

```bash
mkdir -p ~/Dev/video-player
cd ~/Dev/video-player
git clone https://github.com/arvind-4/video-player-in-pyqt5.git .
```

- Setup the virtual environment

You can use virtual environment to create a separate environment for this project. This will help you to keep your project dependencies separate from your system dependencies.

```bash
uv venv --python=python3.12
```

- Sync the dependencies

After setting up the virtual environment, you can sync the dependencies using the following command.

```bash
uv sync
```

- Run the application

To run the application, you can use the following command.

```bash
uv run python src/main.py
```

### Run the tests

To run the tests, you can use the following command.

```bash
uv run pytest tests/
```

### Run the code quality checks

To run the code quality checks, you can use the following command.

```bash
uv run ruff check .
uv run ruff format --check .
uv run bandit -r ./src
uv run pip-audit -l
uv run yamllint --strict ./.github/workflows
```
