# s3-monitoring
A mini monitoring system for an S3 bucket

The system have 2 parts.\

logs_api - flask component that get post request with data from monitoring and write all to logs.txt file

monitoring script - component that use multi processing and monitor the s3 with 4 test:
* upload files test
* download files test
* delete files test
* hash test - upload and then download a file and compare the two files with hash

-----------------------------
# HOW TO RUN:

# logs_api - flask app
##### build image 
docker-compose build
##### docker run
docker-compose up


###Monitoring - script
cd monitoring 
##### build image
docker build -t monitoring .
##### docker run
docker run --name monitoring --network="host" monitoring

