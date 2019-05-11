Vagrant.configure("2") do |config|
  config.vm.define "node1" do |node1|
    node1.vm.box = "centos/7"
    node1.vm.network "private_network", ip: "192.168.50.50", virtualbox__intnet: "intnet"
  end

  config.vm.define "node2" do |node2|
    node2.vm.box = "centos/7"
    node2.vm.network "private_network", ip: "192.168.50.51", virtualbox__intnet: "intnet"
  end

  config.vm.define "ansible" do |ansible|
    ansible.vm.box = "centos/7"
    ansible.vm.network "private_network", ip: "192.168.50.52", virtualbox__intnet: "intnet"
  end

end
