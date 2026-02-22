# tiktak

A platform where users challenge each other in the classic tic-tac-toe game.

This project was made for a collaborative programming session.

The project consists of a backend built with Python and Flask and a UI built with
Vite and React.

## Running the code

### Prerequisites

- Python 3.x
- Node 22.12.0 or higher

### Setup

Create a Python virtual environment in `server`:

```
python3 -m venv server/env
source .server/env/bin/activate
pip install -r server/requirements.txt
```

Install Vite

```
npm --prefix ui install
```

### Run

To start the backend, run

```
flask --app server/src/flaskr run --host 0.0.0.0 --port 1234
```

To start the UI in development mode, run

```
npx vite ui
```

## Running tiktak in Docker

The `Dockerfile` defines an image which has a server running the backend services
and serving a production build of the UI.

To try this out, simply do
```
docker build --tag tiktak .
docker run -p 1234:1234 -d tiktak
```

## Testing

### Unit tests
The directory `server/src/flaskr/test` contains a unit test suite, written using
the module [unitest](https://docs.python.org/3/library/unittest.html).

To run this test suite, run the command
```
python3 -m unittest
```
from within the `server` directory.

If 
you write a new unit test, you must import it in `src/__init__.py` in order for the
`unittest` module to find it.

### API tests
The folder `server/system-testing/test-resources/postman/collections` contains Postman collections in 
Postman collections in
JSON format. [Postman](https://www.postman.com) can be used as a tool for testing APIs. 
You can run these collections as API tests by importing them in the Postman application
or by using 
[newman](https://learning.postman.com/docs/collections/using-newman-cli/command-line-integration-with-newman/), 
Postman's CLI tool.

These tests may fail if the database that the server uses is not empty.

### Performance tests
The folder `server/system-testing/test-resources/k6/scripts` contains scripts for running
performance tests with [k6](https://k6.io/docs/). k6 scripts are written in JavaScript and
k6 provides a simple API for making HTTP
requests. You execute the k6 test defined by the script user-flow.js by running
```
k6 run -e BASE_URL=<tiktak URL> --vus 3 --duration 1m user-flow.js
```
The `--vus` option specifies the number of users that should connect to the server in 
the test and `--duration` specifies for how long.
