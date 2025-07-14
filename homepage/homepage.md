```
sudo apt update && sudo apt upgrade
sudo apt install docker.io
docker run -d -p 80:3000 -e HOMEPAGE_ALLOWED_HOSTS=192.168.1.250,home.int -v /config:/app/config -v /var/run/docker.sock:/var/run/
docker.sock --name homepage ghcr.io/gethomepage/homepage:latest
```

