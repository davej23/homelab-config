docker run -d \
  --name=plex \
  --net=host \
  -e PUID=1000 \
  -e PGID=1000 \
  -e VERSION=docker \
  -v /config:/config \
  -v /films:/movies \
  --restart unless-stopped \
  lscr.io/linuxserver/plex