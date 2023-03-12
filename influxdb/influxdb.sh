docker run -d \
    --name influxdb \
    -p 8086:8086 \
    -v PATH_TO_STORE_INFLUX_DATA:/var/lib/influxdb2 \
    --restart unless-stopped \
    influxdb:latest