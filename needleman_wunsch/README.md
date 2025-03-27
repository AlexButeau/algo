# Needleman-Wunsch Algorithm

## Overview
This project implements the Needleman-Wunsch algorithm for global sequence alignment. The algorithm is widely used in bioinformatics to align DNA, RNA, or protein sequences by maximizing similarity while accounting for gaps and mismatches.

## Features
- Implements the Needleman-Wunsch algorithm in Python
- Supports customizable match, mismatch, and gap penalties

## Installation
To install the required dependencies:
```sh
pip install -r requirements.txt
```

## Project Structure
```
needleman_wunsch/
│── __init__.py
│── needleman_wunsch.py   # Implementation of the algorithm
│
├── tests/
│   ├── __init__.py
│   ├── test_needleman.py           # Unit tests for the algorithm
│
├── requirements.txt      # Dependencies
├── setup.py              # Package configuration
├── pytest.ini            # Pytest configuration
└── README.md             # Project documentation
```

## Running Tests
To ensure the correctness of the implementation, you can run unit tests using pytest:
```sh
python -m pytest -v
```