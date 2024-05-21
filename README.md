# PythonExample

This Program reads a text from a file and prints the language the file is written in and it's probability.

## Documentation

Python Interpreter: 3.10 or higher  
Required Packages:  
- `pip`
- `pipenv`
- `langdetect`


## Functionality  

Usage:
- Windows/Linux:
    1. install `pipenv`:  
        - `pip install pipenv`
        - `pip install --upgrade pipenv`
        - `pipenv install langdetect`
    2. create a virtual environment:
        - `pipenv shell`
    3. run the `run.py`:
        - `python run.py <filename>`   
        - Example: `python run.py test.txt`

- MacOS:
    1. install `pipenv`:  
        - `pip3 install pipenv`
        - `pip3 install --upgrade pipenv`
        - `pipenv install langdetect`
    2. create a virtual environment:
        - `pipenv shell`
    3. run the `run.py`:
        - `python3 run.py <filename>`   
        - Example: `python3 run.py test.txt`

Expected result:
- Output in the terminal:  
["language":"probability"]