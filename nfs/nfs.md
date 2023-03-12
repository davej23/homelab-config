# Server setup
- mkdir -p /srv/nfs/example
- sudo chown -R nobody:nogroup /srv/nfs/example
- sudo chmod 777 /srv/nfs/example
- In /etc/exports --> /srv/nfs/example 192.168.0.0/24(rw,sync,no_subtree_check)
- sudo exportfs -ar
- sudo systemctl restart nfs-kernel-server


# Client Setup
- sudo mkdir -p /mnt/srv/nfs/example
- sudo mount -t nfs -o vers=3 [SERVERIPADDR]:/srv/nfs/examples /mnt/srv/nfs/example