# IowaWildRedditBot
Reddit bot to post and update game threads to /r/IowaWild

**Setup Virtual Environment**

```
make init
```

or 

```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

For Windows Users:

```
python3 -m venv venv
./venv/bin/Scripts/activate
pip install -r requirements.txt
```

### Run tests

#### Run Unit and Linting

From the root of your project, run: 

```
tox
```

#### Unit

From the root of the project, run:

```
tox -e pytest
```

This will run unit tests and give you a coverage report of lines and branches.

### Run lint

From the root of the project, run:

```
tox -e pylint
```
