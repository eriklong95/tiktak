echo "This is a test of the tiktak API."

# start tiktak in docker container
docker run -p 1234:1234 -d --name tiktak_container tiktak

docker run -v $PWD/test-resources/k6/scripts:/src \
    --net host \
    --name k6_container \
    grafana/k6 \
    run -e BASE_URL=http://0.0.0.0:1234 /src/user-creation.js

docker stop tiktak_container
docker rm tiktak_container

docker stop k6_container
docker rm k6_container
