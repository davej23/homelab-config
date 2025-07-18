To run tailscale inside an LXC container, put this inside /etc/pve/lxc/ID.conf

lxc.cgroup2.devices.allow: c 10:200 rwm
lxc.mount.entry: /dev/net/tun dev/net/tun none bind,create=file

then run on container

curl -fsSL https://tailscale.com/install.sh | sh
sudo systemctl enable --now tailscaled
tailscale up

follow steps
