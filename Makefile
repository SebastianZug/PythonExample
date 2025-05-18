# Das Makefile ist ein Skript, das die Ausführung von Befehlen automatisiert.
# An dieser Stelle illustriert es die Referenzierung von Abhänigkeiten
# Die Umsetzung könnte zum Beispiel durch eine Umsetzung verbessert werden,
# die die Aktivierung der Python Umgebung automatisiert abprüft. 

all: install run 

run: run.py test.txt
	@echo "Running run.py with test.txt"
	python3 run.py test.txt > run

install: Pipfile
	@echo "Executing pipenv install"
	pipenv install

test:
	@echo "Executing tests"
	python -m unittest -v test_example.py