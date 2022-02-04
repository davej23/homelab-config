docker run -d \
    -v /nextcloud/nextcloud:/var/www/html \
    -v /nextcloud/apps:/var/www/html/custom_apps \
    -v /nextcloud/config:/var/www/html/config \
    -v /nextcloud/data:/var/www/html/data \
    -p 80:80 \
    nextcloud