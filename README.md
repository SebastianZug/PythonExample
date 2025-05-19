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
    4. run tests:
        - `poetry add pytest --dev` -- to add `pytest` as a development dependency (already in `pyproject.toml`)
        - To run the tests, you can use the `pytest` command:
        - `poetry run pytest`
        - This command will run all the tests in the `tests` directory.
        - Tests need to start with `test_` and be in the `tests` directory.
        - You can also run a specific test file or test function by specifying the path to the test file or function name.

### Expected result

- Output in the terminal:  

    ["language":"probability"]  
    Number of lines: "…"  
    Number of sentences: "…"  
    Number of words: "…"

### Notes

- If you manage python projects with `poetry`, its better to use `poetry new <projectname>` to create a new project.
- This will create a new directory with the name of the project and a basic structure for your project.
- your project files should be put in the src/<projectname> directory.
- and all tests in the tests directory.

```shell
<projectname>/
├── README.md
├── pyproject.toml
├── src
│   └── testproject
│       └── __init__.py
└── tests
    └── __init__.py
```

