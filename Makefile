# Makefile for GST App

.PHONY: help install run test clean migrate shell

help:
	@echo "GST App - Makefile Commands"
	@echo "============================"
	@echo "make install    - Install dependencies"
	@echo "make run        - Run development server"
	@echo "make test       - Run tests"
	@echo "make migrate    - Run database migrations"
	@echo "make shell      - Open Flask shell"
	@echo "make clean      - Clean up cache and temp files"

install:
	pip install -r requirements.txt

run:
	python run.py

test:
	pytest tests/ -v

migrate:
	flask db upgrade

shell:
	flask shell

clean:
	find . -type d -name __pycache__ -exec rm -r {} +
	find . -type f -name '*.pyc' -delete
	find . -type d -name '.pytest_cache' -exec rm -r {} +
	find . -name '*.db' -delete
