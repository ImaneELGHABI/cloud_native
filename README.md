## Run localy with docker (Linux)
```bash
# backend
cd fastapi
docker build -t fastapi .
docker run -d --name fastapi --network host fastapi
# frontend
cd flask
docker build -t flask .
docker run -d --name flask --network host flask
```