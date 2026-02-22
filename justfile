server:
    flask --app=server/src/flaskr run --host=0.0.0.0 --port=1234

ui:
    npx vite ui

build:
    docker build --tag tiktak .
