A platform where users challenge each other in the classic tic-tac-toe game.

This project was made for a workshop at SofaBytes v1.3.0.

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

If you want the server to be accessible from other computers on the local network, you should run
```
flask --app src/flaskr run --host 0.0.0.0 --port 1234
```
The port doesn't really matter but Flask's default port (5000) may not work as the port
may already be in use by some other program on your computer. 
Other computers on the local network can now connect to
server using the URL `http://<LAN IP address of your computer>:1234`. From the host machine, you 
can connect to it at `http://0.0.0.0:1234`.

## Running tiktak in Docker
You can run tiktak in a Docker container if you want to. 
The project includes a Dockerfile, a description of how to build a tiktak Docker
image. To do run this, `cd` to the project's root directory and run
```
docker build --tag tiktak .
```
The `--tag` option sets the name of the Docker image you are creating. You can specify any name 
you want but why not use "tiktak"? By specifying `.`, we let Docker know where to find 
our Dockerfile.

Now run
```
docker run -p 1234:1234 -d tiktak
```
You can now connect to the tiktak server as in the "How to run" section. The last part
of the command is the name of the image you want to use for starting the container so
if you made some silly type, like "tiktok", when building the image you'll have to
repeat that here.

The easiest way to get started using Docker is to install 
the [Docker Desktop](https://www.docker.com/products/docker-desktop/) application.

## API documentation
The tiktak API is defined in a JSON-file conforming to 
the OpenAPI Specification v3.0.3. 
With the server running on `host-url`, a Swagger UI with the API documentation 
can be found at `host-url/docs`. 

## Testing

### Unit tests
The directory `src/flaskr/test` contains a unit test suite, written using
the module [unitest](https://docs.python.org/3/library/unittest.html). 
To run this test suite, run the command
```
python3 -m unittest
```
from the project root directory. Use the `-v` option to get more verbose output. If 
you write a new unit test, you must import it in `src/__init__.py` in order for the
`unittest` module to find it.

### API tests
The folder `system-testing/test-resources/postman/collections` contains Postman collections in 
Postman collections in
JSON format. [Postman](https://www.postman.com) can be used as a tool for testing APIs. 
You can run these collections as API tests by importing them in the Postman application
or by using 
[newman](https://learning.postman.com/docs/collections/using-newman-cli/command-line-integration-with-newman/), 
Postman's CLI tool.

These tests may fail if the database that the server uses is not empty. One way to
ensure that you start up with a fresh database is to delete the file database.db before
starting the server. Another way is to run tiktak in a Docker container: by including
database.db in .dockerignore, we force the creation of a new database when starting a
fresh tiktak Docker container.

### Performance tests
The folder `system-testing/test-resources/k6/scripts` contains scripts for running k6
performance tests. [k6](https://k6.io/docs/) is a popular tool for making performance
tests. k6 scripts are written in JavaScript and k6 provides a simple API for making HTTP
requests. You execute the k6 test defined by the script user-creation.js by running
```
k6 run -e BASE_URL=<tiktak URL> --vus 3 --iterations 10 user-creation.js
```
The `--vus` option specifies the number of users that should connect to the server in 
the test and `--iterations` specifies for how long. k6 provides many different ways of
configuring the test such as ramping the number of users up and down during the test.

### Wrapper scripts
Some shell scripts have been put in the `system-testing` folder for more convenient API and 
performance testing. These scripts starts tiktak and the testing framework in
Docker containers and the executes the tests. You specify the test (Postman collection JSON file 
or k6 JavaScript file) by passing the file name as CLI argument e.g.
```
sh run-api-test.sh user-creation-test.postman_collection.json
```
