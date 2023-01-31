## Python FAST-API Docker Demo
### Install dependencies
```
pip install -r requirements.txt
```

### Run project
```
uvicorn --port 9595 --host 127.0.0.1 app.main:app --reload
```

### Create dependencies
```
pip freeze > requirements.txt  
```

### Run tests
```
pytest  
```

### Run via virtualenv
```
virtualenv --python=/usr/local/bin/python3.10 myenv
source myenv/bin/activate
pip install -r requirements.txt
uvicorn --port 9595 --host 127.0.0.1 app.main:app --reload
```

### Run via docker
```
docker buildx create --name mybuilder --driver docker-container --bootstrap --use
docker buildx build --platform linux/amd64,linux/arm64,linux/arm/v7 -t senolatac/demo-ec2-docker-swarm:latest --push .
docker build -t senolatac/demo-ec2-docker-swarm:latest -f Dockerfile .
docker push senolatac/demo-ec2-docker-swarm:latest
docker container run --publish 9595:9595 --name demo-fast-api-container senolatac/demo-ec2-docker-swarm:latest
```

### EC2 install steps
```
sudo apt-get update
sudo apt install docker.io
sudo apt install openjdk-11-jdk-headless #necessary for jenkins-slave
sudo groupadd docker #necessary to get rid of permission errors 
sudo usermod -aG docker $USER
newgrp docker
```

### Init Docker Swarm in EC2
```
sudo docker swarm init --advertise-addr "'private-ip':2377"
sudo docker swarm join --token 'token' 'private-ip':2377 //to join on other instances.
docker service create --name senol-demo --replicas 2 --publish 9595:9595 senolatac/demo-ec2-docker-swarm:latest //to create docker swarm service
docker service rm senol-demo //to delete docker swarm service
```

### EC2 Security Group Inbound Ports
```
9595(TCP) //for app
2377(TCP), 7946(TCP), 4789(UDP), 7946(UDP) //for docker swarm
```

### Jenkins Requirements
```
jenkins-plugin-cli --plugins config-file-provider ssh-slaves
cat key-pair //On local machine, to read pem file.
```
