docker run -d \
  --name=duplicati \
  -e PUID=1000 \
  -e PGID=1000 \
  -e TZ=Europe/London \
  -p 8200:8200 \
  -v PATH_TO_CONFIG:/config \
  -v PATH_FOR_LOCAL_BACKUP:/backups \
  -v PATH_TO_BACKUP_1:/data_1 \
  -v PATH_TO_BACKUP_2:/data_2 \
  --restart unless-stopped \
  lscr.io/linuxserver/duplicati:latest
