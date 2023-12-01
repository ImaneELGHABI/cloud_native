## Run localy with docker (Linux)
```bash
cd Mid-Term
# backend
cd fastapi
docker build -t fastapi .
docker run -d --name fastapi --network host fastapi
# frontend
cd flask
docker build -t flask .
docker run -d --name flask --network host flask
```
The flask web interface will be available on : http://localhost:2222/
