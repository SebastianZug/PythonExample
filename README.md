# PythonExample

This Program reads a text from a file and prints the language the file is written in and it's probability.  
Added to that, it prints the amount of lines, sentences and words the file includes.

## Documentation

Python Interpreter: 3.11 or higher  
Required Packages:  

### System

- `pipx`
- `poetry`

### Python Libraries

- `langdetect`

## Functionality  

### Usage

- Windows/Linux/MacOS:
    1. install `poetry`:  
        - [poetry install](https://python-poetry.org/docs/#installation)
        - There are options for using `pipx` or a standalone installer to install poetry.
        - `pipx install poetry`
        - `pipx` is the modern way to install and run Python applications in isolated environments.
    2. install requirements:
        - `poetry install --no-root`
        - This command will install the dependencies listed in the `pyproject.toml` file. Without installing the package itself.
    3. run the `run.py`:
        - As poetry is managing the virtual environment, you can run the script using poetry:
        - `poetry run python3 run.py <filename>`
        - Example: `poetry run python3 run.py test.txt`

### Expected result

- Output in the terminal:  

    ["language":"probability"]  
    Number of lines: "…"  
    Number of sentences: "…"  
    Number of words: "…"
