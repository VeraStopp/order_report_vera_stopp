# Order Report Generator
A python project designed to automate the processing, validation and analysis of order data. 

- Python version: 3.13.17
- Required packages: managed via `pyproject.py` 

## Installation
1. Clone the repository 
```bash
git clone https://github.com/VeraStopp/order_report_vera_stopp.git
cd order_report
```
### 2. Create and activate a virtual enviroment
```bash
python -m venv -venv
source -venv/Scripts/activate
```
### 3. Install dependencies and the package
```bash
python -m pip install --upgrade pip
python -m pip install -e .
```

## Usage
Ensure your inpit CSV file is placed at `data/order.csv`
Run the application from the project root using 
```bash
python -m order_report
```
The outputs will be generated av saved in the `output/` folder

## Running test
Tests are mananged using `pytest`. Run the test suite with:
```bash
pytest 
```