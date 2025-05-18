# Das Makefile ist ein Skript, das die Ausführung von Befehlen automatisiert.
# An dieser Stelle illustriert es die Referenzierung von Abhängigkeiten
# Die Umsetzung könnte zum Beispiel durch eine Umsetzung verbessert werden,
# die die Aktivierung der Python Umgebung automatisiert abprüft. 

all: install run 

run: run.py test.txt
	@echo "Running run.py with test.txt"
	poetry run python3 run.py test.txt

install: pyproject.toml
	@echo "Executing poetry install"
	poetry install --no-root

test:
	@echo "Executing tests"
	poetry run pytest
