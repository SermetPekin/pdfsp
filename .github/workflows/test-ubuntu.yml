name: Pypi Ubuntu Server

on:
  push:
    paths: 
      - "**.py"
      - "*.yml"
  pull_request:
    branches: ["main"]

jobs:
  build:
    runs-on: ubuntu-latest
    strategy:
      fail-fast: false
      matrix:
        python-version: [  "3.10" ,"3.11", "3.12", "3.13"]

    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Set up Python ${{ matrix.python-version }}
        uses: actions/setup-python@v3
        with:
          python-version: ${{ matrix.python-version }}

      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install flake8 pytest
          # if [ -f requirements.txt ]; then pip install -r requirements.txt; fi
          pip install uv pdfsp 
          uv venv
          source .venv/bin/activate

      - name: Run tests
        run: |
          pytest -v
      
      
