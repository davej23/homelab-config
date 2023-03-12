# Configure InfluxDB and Telegraf
- Install Telegraf using instructions [here](https://www.influxdata.com/time-series-platform/telegraf/)
- Setup InfluxDB using `influxdb.sh` script (make sure to change `PATH_TO_STORE_INFLUX_DATA`)
- Open IP:PORT, e.g. 192.168.0.2:8086, in a browser
- Fill in details such as user account name, password, organisation name, first bucket name
- In `monitoringconfig.conf` file, change `organization`, `url`, `bucket` to match values used
- Go to InfluxDB admin panel -> Load Data -> API Token, Generate API Token (All Access). Create an API token for Proxmox.
- Go to Proxmox -> Datacenter -> Metric Server -> Add -> HTTP 8086, OrgName, Bucket Name, API Token
- Go to InfluxDB admin panel -> Load Data -> Telegraf -> Create Configuration -> Pick a bucket, select Disk, click Continue Configuring, paste contents of `monitoringconfig.conf` into box, give the config a name in the `Configuration Name` box, click `Save and test`, copy the `TOKEN` in `export INFLUX_TOKEN=TOKEN` to `telegraf.sh` (in place of `INSERT_TOKEN_HERE`) and copy the `telegraf --config ...` line into the `telegraf.sh` file (in place of the second line)
- Set `telegraf.sh` to executable using `chmod +x telegraf.sh`
- Run the `telegraf.sh` script

**Optional - Run Telegraf script on boot**
- Add contents of `crontab.template` to crontab on system containing Telegraf

## Proxmox Plugin
Useful Link -> https://saelzler.com/tech/use-influxdb-2-as-a-metric-server-for-proxmox/