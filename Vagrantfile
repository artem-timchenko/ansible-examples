Vagrant.configure("2") do |config|
  config.vm.define "node1_centos" do |node1_centos|
    node1_centos.vm.box = "centos/7"
    node1_centos.vm.network "private_network", ip: "192.168.50.50", virtualbox__intnet: "intnet"
  end

  config.vm.define "node2_centos" do |node2_centos|
    node2_centos.vm.box = "centos/7"
    node2_centos.vm.network "private_network", ip: "192.168.50.51", virtualbox__intnet: "intnet"
  end

  config.vm.define "node1_ubuntu" do |node1_ubuntu|
    node1_ubuntu.vm.box = "ubuntu/xenial64"
    node1_ubuntu.vm.network "private_network", ip: "192.168.50.53", virtualbox__intnet: "intnet"
  end

  config.vm.define "node2_ubuntu" do |node2_ubuntu|
    node2_ubuntu.vm.box = "ubuntu/xenial64"
    node2_ubuntu.vm.network "private_network", ip: "192.168.50.54", virtualbox__intnet: "intnet"
  end

  config.vm.define "ansible" do |ansible|
    ansible.vm.box = "centos/7"
    ansible.vm.network "private_network", ip: "192.168.50.52", virtualbox__intnet: "intnet"
  end

end
