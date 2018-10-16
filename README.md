In order to use the repo creating a virtual environment is recommended:

Assuming you are in the repo top directory:
```commandline
python3 -m venv ./python
cd ./python
source bin/activate
pip3 install -r requirements.txt
```

The editor used for creating this project is PyCharm. 

# Docu
You find a general overview of the game logic and implementation 
[here](./doc/overview.md)


# Running a Game
(not yet fully implemented)
`terminal.py` tries to start a game only between (yet dysfunctional) AI.

# Tests and Coverage
The tests for this project are written using py.test. For the coverage
of the test tha pytest-cov plugin is used.
Repo directory, change into the python directory
```commandline
cd ./python
py.test --cov=src/pychu/ tests/
```

In order for py.test to discover the actual classes, the 
`src` directory is appended to the path. Knowning this 
might help debugging import issues. 

tests/__init.py__
```python
sys.path.append('./src')
```