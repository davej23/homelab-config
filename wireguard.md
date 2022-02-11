# Wireguard setup
## using https://upcloud.com/community/tutorials/get-started-wireguard-vpn/
## and https://www.digitalocean.com/community/tutorials/how-to-set-up-wireguard-on-ubuntu-20-04

# Set up IPv4 forwarding
nano /etc/sysctl.conf
Uncomment 'net.ipv4.ip_forward=1'
sysctl -p

# Install wg and enable ufw
apt install wireguard qrencode ufw -y
ufw allow ssh
ufw allow 51820/udp 
ufw enable
cd /etc/wireguard
umask 077
wg genkey | tee privatekey | wg pubkey > publickey
wg-quick up wg0

# Phone app setup
- Generate private/public key
- address = 192.168.1.2/32
- dns 1.1.1.1
- listen port 51820
- add peer --> server public key + 0.0.0.0/0 + SERVERIP:51820

# Configure server conf -- /etc/wireguard/wg0.conf
[Interface]
Address = 192.168.1.1/24
SaveConfig = true
PostUp = ufw route allow in on wg0 out on eth0
PostUp = iptables -t nat -I POSTROUTING -o eth0 -j MASQUERADE
PreDown = ufw route delete allow in on wg0 out on eth0
PreDown = iptables -t nat -D POSTROUTING -o eth0 -j MASQUERADE
ListenPort = 51820
PrivateKey = [private server key here]

[Peer]
PublicKey = [public peer key here]
AllowedIPs = 192.168.1.2/32

# Start wg
systemctl enable wg-quick@wg0.service --now