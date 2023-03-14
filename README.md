A platform where users challenge each other in the classic tic-tac-toe game.

## Get started
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