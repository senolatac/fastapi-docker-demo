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

### Run via docker
```
docker buildx create --name mybuilder --driver docker-container --bootstrap --use
docker buildx build --platform linux/amd64,linux/arm64,linux/arm/v7 -t senolatac/demo-ec2-docker-swarm:latest --push .
docker build -t senolatac/demo-ec2-docker-swarm:latest -f Dockerfile .
docker push senolatac/demo-ec2-docker-swarm:latest
docker container run --publish 9595:9595 --name demo-fast-api-container senolatac/demo-ec2-docker-swarm:latest
```
