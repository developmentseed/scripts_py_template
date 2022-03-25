#! /bin/bash -e

echo "Running Black..."
black .

echo "Running Flake8..."
flake8 .

echo "Running pyDocStyle..."
pydocstyle .

echo "Running MyPy..."
mypy src

echo "Congratulations! All went well."
