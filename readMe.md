## How to init database and run app

```bash
flask --app flaskr init-db
flask --app flaskr run --debug
```

## How to run tests &

Can't just run `pytest`, have to run pytest as a module in python (which adds the current directory to sys.path).
[Read More](https://docs.pytest.org/en/latest/usage.html#calling-pytest-through-python-m-pytest)

```bash
python -m pytest -vv
```

or

```
coverage run -m pytest
coverage report
```
