# PythonExample

## Documentation

Python Interpreter: 3.10 higher  
Abhängikeiten von Packages:  
- `pip`
- `pipenv`
- `langdetect`


## Functionality

Reads a text from a file and print the language the file is written in and it's probability.  

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
- Ausgabe im Terminal:  
["language":"probability"]