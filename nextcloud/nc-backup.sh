#!/bin/bash
rsync -Aavx NEXTCLOUD_DATADIR BACKUP_DIR/backup_`date +"%Y%m%d"`/ &