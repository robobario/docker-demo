docker build . -t gradle -f ./Dockerfile.gradle
docker run -v `pwd`:/opt/hello-java -w /opt/hello-java gradle /opt/hello-java/gradlew build
docker build -t hello-java .
