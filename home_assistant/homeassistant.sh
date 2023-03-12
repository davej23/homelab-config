docker run -d \
  --name homeassistant \
  --privileged \
  --restart=unless-stopped \
  -e TZ=Europe/London \
  -v /homeassistant:/config \
  --network=host \
  ghcr.io/home-assistant/home-assistant:stable