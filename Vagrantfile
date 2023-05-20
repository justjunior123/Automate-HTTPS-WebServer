# -*- mode: ruby -*-
# vi: set ft=ruby :

# All Vagrant configuration is done below. The "2" in Vagrant.configure
# configures the configuration version (we support older styles for
# backwards compatibility). Please don't change it unless you know what
# you're doing.
Vagrant.configure("2") do |config|
  # The most common configuration options are documented and commented below.
  # For a complete reference, please see the online documentation at
  # https://docs.vagrantup.com.

  # Every Vagrant development environment requires a box. You can search for
  # boxes at https://vagrantcloud.com/search.
  config.vm.box = "ubuntu/trusty64"
  config.vm.guest = :ubuntu

  # Disable automatic box update checking. If you disable this, then
  # boxes will only be checked for updates when the user runs
  # `vagrant box outdated`. This is not recommended.
  # config.vm.box_check_update = false

  # Create a forwarded port mapping which allows access to a specific port
  # within the machine from a port on the host machine. In the example below,
  # accessing "localhost:8080" will access port 80 on the guest machine.
  # NOTE: This will enable public access to the opened port
  # config.vm.network "forwarded_port", guest: 80, host: 8080

  # Create a forwarded port mapping which allows access to a specific port
  # within the machine from a port on the host machine and only allow access
  # via 127.0.0.1 to disable public access
  # config.vm.network "forwarded_port", guest: 80, host: 8080, host_ip: "127.0.0.1"

  # Create a private network, which allows host-only access to the machine
  # using a specific IP.
  # config.vm.network "private_network", ip: "192.168.33.10"

  # This line of code configures a forwarded port in the virtual 
  # machine (guest). It maps port 4443 in the virtual machine to port 6080 on the host machine, 
  # and binds it to the loopback address (127.0.0.1) of the host. This means that when you 
  # access 127.0.0.1:6080 on the host machine, it will forward the request to port 4443 on the 
  # virtual machine. This allows you to access services running in the virtual machine as if they
  # were running on the host machine, while still isolating the virtual machine from the host 
  # network.
  config.vm.network "forwarded_port", guest: 4443, host: 6080, host_ip: "127.0.0.1"

  # Create a public network, which generally matched to bridged network.
  # Bridged networks make the machine appear as another physical device on
  # your network.
  # config.vm.network "public_network"

  # Share an additional folder to the guest VM. The first argument is
  # the path on the host to the actual folder. The second argument is
  # the path on the guest to mount the folder. And the optional third
  # argument is a set of non-required options.
  # config.vm.synced_folder "../data", "/vagrant_data"
  config.vm.synced_folder "~/Desktop/python-webpage/webpage", "/home/vagrant/webpage"



  # Provider-specific configuration so you can fine-tune various
  # backing providers for Vagrant. These expose provider-specific options.
  # Example for VirtualBox:
  #
  # config.vm.provider "virtualbox" do |vb|
  #   # Display the VirtualBox GUI when booting the machine
  #   vb.gui = true
  #
  #   # Customize the amount of memory on the VM:
  #   vb.memory = "1024"
  # end
  #
  # View the documentation for the provider you are using for more
  # information on available options.

  # Enable provisioning with a shell script. Additional provisioners such as
  # Ansible, Chef, Docker, Puppet and Salt are also available. Please see the
  # documentation for more information about their specific syntax and use.
  # config.vm.provision "shell", inline: <<-SHELL
  #   apt-get update
  #   apt-get install -y apache2
  # SHELL

  # This code block below is used to provision the virtual machine managed by Vagrant. 
  # The config.vm.provision method is used to specify a shell script that will be executed on the virtual machine 
  # after it is created and started. The script is passed to the inline argument as a string literal.

  config.vm.provision "shell", inline: <<-SHELL
  sudo apt-get install systemd
  sudo apt-get update
  sudo apt-get install -y python3 python3-pip

SHELL

# sudo apt-get install systemd: This installs the systemd package, which is a system and service manager for Linux.
# sudo apt-get update: This updates the package list index to the latest version.
# sudo apt-get install -y python3 python3-pip: This installs the python3 and python3-pip packages, which are the 
# Python 3 interpreter and the Python package installer, respectively.

end
