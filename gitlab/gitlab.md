curl -s https://packages.gitlab.com/install/repositories/gitlab/gitlab-ce/script.deb.sh | sudo bash
sudo apt-get install gitlab-ce=14.7.3-ce.0
# Change external url in /etc/gitlab/gitlab.rb
sudo gitlab-ctl reconfigure
# Root pass in /etc/gitlab/initial_root_password