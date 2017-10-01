# -*- mode: ruby -*-
# vi: set ft=ruby :

# Vagrantfile API/syntax version. Don't touch unless you know what you're doing!
VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|

  config.vm.provider :virtualbox do |v|
    v.customize ["modifyvm", :id, "--memory", "512"]
    v.customize ["modifyvm", :id, "--natdnshostresolver1", "on"]
  end

  config.vm.box = "ubuntu/xenial64"

  config.ssh.username = "ubuntu"
  config.ssh.password = "b92862643097472e25275e87"


  # Sharing this folder to /home/ubuntu/app
  config.vm.synced_folder ".", "/home/ubuntu/app", create:true
  config.vm.provision :shell, :path => "setup_vagrant.sh"
  config.vm.network :private_network, ip: "192.168.55.56"
  config.vm.network :forwarded_port, guest: 5000, host: 5000
  config.vm.network :forwarded_port, guest: 5432, host: 5432

end