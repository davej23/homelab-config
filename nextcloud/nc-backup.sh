#!/bin/bash

# Enable Maintenance mode
docker exec --user www-data -it nextcloud-aio-nextcloud php occ maintenance:mode --on

# Backup files
rsync -Aavx NEXTCLOUD_DATADIR BACKUP_DIR/backup_`date +"%Y%m%d"`/

# Disable Maintenance mode
docker exec --user www-data -it nextcloud-aio-nextcloud php occ maintenance:mode --off
