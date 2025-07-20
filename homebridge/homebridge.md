```
sudo apt update && sudo apt upgrade
sudo apt install docker.io docker-compose
sudo apt install python3-setuptools
```

get docker-compose from homebridge site

```
nano /homebridge/docker-compose.yaml  # paste in docker compose and modify
cd /homebridge
docker-compose up -d
```