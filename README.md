# DockerPractices
This is the folder where my Docker exercises will be located.

In order to try these applications, you must have Docker installed on your device.

If you haven't a Docker -> https://docs.docker.com/engine/install/

### GuessNumberGame

A random number between 1-50 is kept by the computer. The user tries to find this number according to the answers given by the computer. Returns the number of attempts up to the time found.

*Ex Image*

![Guess Number Game Ex Image](https://github.com/MelihSelamiUrkmezz/DockerPractices/blob/master/GuessNumberGame/ExImage.png)

-> If you want to try the app;

- docker image pull melihselamiurkmez/guessgame
- docker container run --name <containername> -it melihselamiurkmez/guessapp 

### Stream Website with Flask

It is python code that enables publishing a website from Flask.

*Ex Image*

![Website Ex Image](https://github.com/MelihSelamiUrkmezz/DockerPractices/blob/master/FlaskStream/website.png)

-> If you want see my website;

- docker image pull melihselamiurkmez/website
- docker container run --name <containername> -d -p <port>:5000 melihselamiurkmez/website 

### Instagram Automation

It allows you to find unfollowers of yourself or the people you follow on your Instagram account. It also allows to return the url of the profile photo of any desired account.

*Ex Image*

![Instagram Automation Ex Image](https://github.com/MelihSelamiUrkmezz/DockerPractices/blob/master/InstagramAutomation/instauto.png)

-> If you want to try the app;

- docker image pull melihselamiurkmez/instagramscript
- docker container run --name <containername> -it melihselamiurkmez/instagramscript

### Container Cluster With Docker Swarm

It is a swarm stack yaml file that run a website with 3 replicas and a database with 3 replicas on 1 manager node.

-> If you want to try the app;
- git clone https://github.com/MelihSelamiUrkmezz/DockerPractices.git
- cd DockerSwarm
- docker swarm init --advertise-addr <ip_addr> 
- docker stack deploy -c \<composename>\.yaml \<stackname>\

### Apache Kafka with KafDrop on Docker Swarm

I created a deployment by making apache kafka and kafdrop into a compose file. When this deployment is run, a kafka interface published at 127.0.0.1:9000, zookeeper and kafka are running.

-> If you want to try the app;
- mkdir GitDockerPractices
- cd GitDockerPractices
- git clone https://github.com/MelihSelamiUrkmezz/DockerPractices.git
- cd ApacheKafka
- docker swarm init --advertise-addr <ip_addr> ( If your machine not initialized) 
- docker stack deploy -c docker-compose.yaml \<stackname>\
- docker ps 
- Check


