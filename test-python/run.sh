docker-compose build
docker-compose up -d
docker wait testpython_test_1
docker-compose rm -f
