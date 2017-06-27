# -*- mode: ruby -*-
# vi: set ft=ruby ts=2 sw=2 expandtab :

PROJECT = "gunicorn-kibana-logstash"
ENV['VAGRANT_NO_PARALLEL'] = 'yes'
ENV['VAGRANT_DEFAULT_PROVIDER'] = 'docker'
VAGRANTFILE_VERSION = "2"

Vagrant.configure(VAGRANTFILE_VERSION) do |config|

  environment_variables = {
    # used for 'dev' containers to have same permissions as current user
    "HOST_USER_UID" => Process.euid,
    "ENV_NAME" => "devdocker",
    "APP_PATH" => "/vagrant",
    "VIRTUAL_ENV_PATH" => "/tmp/virtual_env35",
    "PROJECT" => PROJECT,
  }

  config.vm.define "cassandra" do |app|
    app.vm.provider "docker" do |d|
      d.image = "kibana"
      d.name = "#{PROJECT}_kibana"
    end
  end

  config.ssh.insert_key = true
  config.vm.define "dev", primary: true do |app|
    app.vm.provider "docker" do |d|
      d.image = "allansimon/allan-docker-dev-python"
      d.name = "#{PROJECT}_dev"
      d.has_ssh = true
      d.env = environment_variables
    end
    app.ssh.username = "vagrant"

    app.vm.provision "ansible", type: "shell" do |ansible|
      ansible.env = environment_variables
      ansible.inline = "
        set -e
        cd $APP_PATH
        ansible-playbook bootstrap.yml
        echo 'done, you can now run `vagrant ssh`'
      "
    end
  end
end
