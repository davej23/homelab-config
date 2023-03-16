# Configure Nextcloud with CloudFlare Proxy
- Set static IP for system that will host Nextcloud
- Open ports 443, 8080, 8443
- Set DNS settings in CloudFlare (for domain to be used with Nextcloud) to point to IP of Nextcloud system and disable CloudFlare Proxy for the DNS entry
- Run `nextcloud.sh`
- Open link provided and follow setup
- Go to DOMAIN:8443 (provides certificate according to Nextcloud Documentation)
- Close ports 8443 and 8080
- Enable CloudFlare Proxy on DNS entry

## Follow-Up Configuration

**Auto-Update CloudFlare DNS Entry IP**
If IP address is not static, see my other repository [here](https://github.com/davej23/cloudflare-dynamic-dns) to autoupdate DNS entry to match current system IP address.

**Autorenew SSL certificates**
When behind CloudFlare Proxy, certificates cannot autorenew. See my other repository [here](https://github.com/davej23/nextcloud-aio-cloudflare-proxy) to avoid this issue.

# Additional Admin Things

**Backup Nextcloud Data Folder**
Run `nc-backup.sh` on Nextcloud AIO container host machine, change variables in script to match what is required.

This script uses `rsync` to clone Nextcloud data directory to a user-specified backup location.

**Backup Nextcloud Database**
Run `backup_db.py` on Nextcloud AIO container host machine, change variables in script to match what is required.

This script obtains the Nextcloud PostgreSQL database credentials using `docker inspect`, dumps the database and copies it to a user-specified location, as well as removing backup dumps older than N days.
