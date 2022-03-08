sudo pacman -Syu
yay -S chrome-gnome-shell touchegg xorg-xrandr
xrandr --output eDP --scale 1.5x1.5
sudo gpasswd -a [USER] input
sudo systemctl enable --now touchegg.service
cat "WaylandEnable=false" >> /etc/gdm/custom.conf
