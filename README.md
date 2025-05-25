# SQL Alchemy Example, with Unit Tests

## Requirements
- sqlalchemy
- pyodbc or pymssql (see Database.py to change the connection string)
- unittest (part of the standard Python library from [python.org](https://python.org))

We don't teach SQL Alchemy in CIS 133Y or CIS 233Y, but a lot of students are starting to use it, and
they get confused by the technology. So here's an example of the whole thing along with PyUnit unit testing,
which we cover in the back-half of the class.

**Note**: You don't have to use SQL Alchemy (and you shouldn't, unless your team is already
familiar with it and knows how to use it. The stories in this class are most definitely simple
enough to just send queries to the database using SQL).

## Usage
Run:
```python
python main.py
```
to execute the names app, and run:
```python
python -m unittest test_Name.py
```
to run the unit tests.