## About
A sample Blog application made with Python Flask v2.3.3, Jinja2 v3.1.2 and Bootstrap v5.3.2

Using Bootstrap for relieving pain writing css. A few practice borrowed from Node.js + EJS stack, such as:
* using different layouts for different pages
* introduced controllers (that of MVC) to take over request processing and response sending
## How to init database and run app
### Activate virtual env
```bash
source ./venv/bin/activate
```
### Run application in debug mode
```bash
flask --app flaskr init-db
flask --app flaskr run --debug
```

### Features
- [ ] [Sidebar Implementation](https://dev.to/codeply/bootstrap-5-sidebar-examples-38pb)

### Links
[Markdown Cheatsheet](https://markdown.com.cn/cheat-sheet.html)
[Example of Flask App](https://www.digitalocean.com/community/tutorials/how-to-structure-a-large-flask-application-with-flask-blueprints-and-flask-sqlalchemy)

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
