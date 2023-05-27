echo "This is a test of the tiktak API."
# start tiktak in docker container

# print stuff from the newman run for the user to see
docker run -v $PWD/test-resources/postman:/etc/newman -t postman/newman \ 
    run --env-var "baseUrl=http://localhost:5000" \
    collections/user-creation-test.postman_collection.json

# remove Docker containers
