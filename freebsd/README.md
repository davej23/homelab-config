# My Install Process

```bash
# go through setup as expected, enabling ports

freebsd-update fetch update

pkg install xorg plasma5-plasma konsole dolphin sddm zsh git drm-kmod firefox doas vim

cp /usr/local/etc/doas.conf.sample /usr/local/etc/doas.conf

pw groupmod video -m USER

pw groupmod wheel -m USER

sysrc kld_list="amdgpu"

# Add Xorg AMD conf (didn't work for me?)

sysrc dbus_enable="YES"

sysrc sddm_enable="YES"

echo "exec ck-launch-session startplasma-x11" > ~/.xinitrc

# Add `snd_hda_load="YES"` and `snd_driver_load="YES"` to /boot/loader.conf

pkg install virtual_oss

# Add `cuse_load="YES"` to /boot/loader.conf

# Follow this guide for Widevine https://github.com/mrclksr/linux-browser-installer

pkg install vscode signal-desktop
sysrc sound_load="YES"

# Move .zshrc to ~/.zshrc

# Disable kwallet, remove kwalletmanager

# Install gnome-keyring and gnome-keyring-sharp
```

For GitHub credential management, one way is:
- `git config --global credential.helper store`
- Create `~/.git-credentials` file with format `https://user:name@github.com`

Make sure LVIM installed

```
LV_BRANCH='release-1.2/neovim-0.8' bash <(curl -s https://raw.githubusercontent.com/lunarvim/lunarvim/fc6873809934917b470bff1b072171879899a36b/utils/installer/install.sh)

# Then

export PATH=~/.local/bin:$PATH

# Add PATH=~/.local/bin:$PATH to .zshenv
```
