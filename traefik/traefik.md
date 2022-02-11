# Setup Traefik with Docker + External Service

## Pre-requisites
- No certificate on domain
- Add domain to CF
- Create API key for Edit DNS
- Expose 80 and 443 ports on router

## Setup container
- apt install apache2-utils
- echo $(htpasswd -nb <USER> <PASSWORD>) | sed -e s/\\$/\\$\\$/g
    - Replace USER:HASHEDPASSWORD with output from command
- chmod 600 acme.json
- docker-compose up -d

## Crontab to autostart
@reboot sleep 60 && /usr/local/bin/docker-compose -f /traefik/docker-compose.yml up -d
@reboot sleep 60 && echo "nameserver 8.8.8.8" >> /etc/resolv.conf