A platform where users challenge each other in the classic tic-tac-toe game.

## How to run
You need to have Python 3.x installed to run the project.

First, clone the repository to a suitable location in your local file system.

Then, from the project root directory, run
```
python -m venv env
```
to create a virtual environment named *env* for this project. `env/` is already in .gitignore.

Next, activate the virtual environment and run
```
pip install requirements.txt
```
to install the project's dependencies.

Finally, run
```
flask --app src/flaskr run
```
to start the server. Use the `--debug` option to start it in debug mode.

## API documentation
The tiktak API is defined in a JSON-file conforming to the OpenAPI Specification v3.0.3. With the server running on `host-url`, a Swagger UI with the API documentation can be found at `host-url/docs`.

## Test suite
The directory `src/flaskr/test` contains a test suite. To run this test suite, run the command
```
python3 -m unittest
```
from the project root directory.
