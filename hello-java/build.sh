docker run -v `pwd`:/opt/hello-java -w /opt/hello-java gradle /opt/hello-java/gradlew build
docker build -t hello-java:9 .
