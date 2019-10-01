
#copy files to remote raspberry used for building the docker image
scp -r ../personal_website pi@192.168.1.116:~/

#login to remote raspberry and build and push docker image
ssh pi@192.168.1.116 'cd personal_website/ ; docker build -t tthebst/my_web . ; docker push tthebst/my_web ; sudo rm -r ../personal_website ; exit'
