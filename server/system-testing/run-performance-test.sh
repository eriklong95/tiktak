echo "This is a performance test of the tiktak server."
if [ $# -ne 1 ]; then
    echo "Usage: sh run-performance-test.sh [k6 script file name]"
    exit 1
fi

# start tiktak in docker container
docker run -p 1234:1234 -d --name tiktak_container tiktak

docker run -v $PWD/test-resources/k6/scripts:/src \
    --net host \
    --name k6_container \
    grafana/k6 \
    run -e BASE_URL=http://0.0.0.0:1234/api --vus 5 --duration 1m /src/$1

echo "Wait for the Docker containers to stop and be removed"

docker stop k6_container
echo "... stopped."
docker rm k6_container
echo "... was removed."

docker stop tiktak_container
echo "... stopped."
docker rm tiktak_container
echo "... was removed."
