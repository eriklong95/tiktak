echo "This is a test of the tiktak API."
if [ $# -ne 1 ]; then
    echo "Usage: sh run-api-test.sh [Postman collection JSON file name]"
    exit 1
fi

# start tiktak in docker container
docker run -p 1234:1234 -d --name tiktak_container tiktak

docker run -v $PWD/test-resources/postman:/etc/newman \
    --net host \
    --name newman_container \
    postman/newman \
    run --env-var baseUrl=http://0.0.0.0:1234/api collections/$1

docker stop newman_container
echo "... stopped."
docker rm newman_container
echo "... was removed."

docker stop tiktak_container
echo "... stopped."
docker rm tiktak_container
echo "... was removed."
