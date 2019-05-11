$script = <<-SCRIPT
echo "12345" | passwd vagrant --stdin
sed -i "s/.*PasswordAuthentication.*/PasswordAuthentication yes/g" /etc/ssh/sshd_config
systemctl restart sshd
SCRIPT

$ssh = <<-SCRIPT
sudo yum install -y sshpass
ssh-keygen -N "" -f /home/vagrant/.ssh/id_rsa
echo -e "192.168.50.50\n192.168.50.51\n192.168.50.53\n192.168.50.54\n192.168.50.52" > host_list
ssh-keyscan -f host_list  >> /home/vagrant/.ssh/known_hosts
rm host_list
sshpass -p 12345 ssh-copy-id 192.168.50.50
sshpass -p 12345 ssh-copy-id 192.168.50.51
sshpass -p 12345 ssh-copy-id 192.168.50.52
sshpass -p 12345 ssh-copy-id 192.168.50.53
sshpass -p 12345 ssh-copy-id 192.168.50.54
SCRIPT

Vagrant.configure("2") do |config|
  config.vm.provision "shell", inline: $script

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
    ansible.vm.provision "shell", privileged: false, inline: $ssh
  end

end
