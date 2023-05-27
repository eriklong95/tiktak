echo "This is a test of the tiktak API."

# start tiktak in docker container
docker run -p 1234:1234 -d --name tiktak_container tiktak

# print stuff from the newman run for the user to see
docker run -v $PWD/test-resources/postman:/etc/newman \
    --net host \
    --name newman_container \
    --platform linux/amd64/v8 \
    postman/newman \
    run --env-var baseUrl=http://0.0.0.0:1234 collections/user-creation-test.postman_collection.json

# stop and remove newman container
docker stop newman_container
docker rm newman_container

# stop and remove tiktak container
docker stop tiktak_container
docker rm tiktak_container
