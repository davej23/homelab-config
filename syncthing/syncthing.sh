docker run -d \
  --name=syncthing \
  -e PUID=1000 \
  -e PGID=1000 \
  -e TZ=Europe/London \
  -p 8384:8384 \
  -p 22000:22000/tcp \
  -p 22000:22000/udp \
  -p 21027:21027/udp \
  -v /syncthing/config:/config \
  -v /syncthing/data:/data \
  --restart unless-stopped \
  lscr.io/linuxserver/syncthing