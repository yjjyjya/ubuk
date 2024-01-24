## 一、环境准备

> ### 1.1 环境

`sudo passwd root`
`sudo ufw disable`

> ### 1.2 换源

`sudo vi /etc/apt/sources.list`
```
deb http://mirrors.tencentyun.com/ubuntu/ focal main restricted universe multiverse
deb http://mirrors.tencentyun.com/ubuntu/ focal-security main restricted universe multiverse
deb http://mirrors.tencentyun.com/ubuntu/ focal-updates main restricted universe multiverse
# deb http://mirrors.tencentyun.com/ubuntu/ focal-proposed main restricted universe multiverse
# deb http://mirrors.tencentyun.com/ubuntu/ focal-backports main restricted universe multiverse
deb-src http://mirrors.tencentyun.com/ubuntu/ focal main restricted universe multiverse
deb-src http://mirrors.tencentyun.com/ubuntu/ focal-security main restricted universe multiverse
deb-src http://mirrors.tencentyun.com/ubuntu/ focal-updates main restricted universe multiverse
# deb-src http://mirrors.tencentyun.com/ubuntu/ focal-proposed main restricted universe multiverse
# deb-src http://mirrors.tencentyun.com/ubuntu/ focal-backports main restricted universe multiverse
```
`sudo apt update`
`sudo apt upgrade`

> ### 1.3 网络配置

`sudo vi /etc/sysctl.conf`
取消注释下面这行
`net.ipv4.ip_forward=1`
`sudo sysctl -p`
`sudo vi /etc/network/interfaces`
```
auto lo
iface lo inet loopback
# The primary network interface
auto eth0
iface eth0 inet static
address 10.0.24.13
network 10.0.24.0
netmask 255.255.255.0
broadcast 10.0.24.255
gateway 10.0.24.1
```
试试是否可以 ping 通百度 `ping baidu.com`

> ### 1.4 修改主机名和IP映射

注意是用内网映射
`sudo vi /etc/hostname` 改成 controller，意思即该主机作为控制节点
`sudo vi /etc/hosts` 注释掉 127.0.1.1 那一行
在 `127.0.0.1 localhost` 后面加上 controller
然后另起一行添加 `对应的IP地址 controller`
再重启 `reboot`

> ### 1.5 设置时间服务

`sudo apt install chrony`
`sudo vi /etc/chrony/chrony.conf`
修改为如下内容：
```
#注意注释掉几个pool，添加server、allow、local

# Welcome to the chrony configuration file. See chrony.conf(5) for more
# information about usuable directives.

# This will use (up to):
# - 4 sources from ntp.ubuntu.com which some are ipv6 enabled
# - 2 sources from 2.ubuntu.pool.ntp.org which is ipv6 enabled as well
# - 1 source from [01].ubuntu.pool.ntp.org each (ipv4 only atm)
# This means by default, up to 6 dual-stack and up to 2 additional IPv4-only
# sources will be used.
# At the same time it retains some protection against one of the entries being
# down (compare to just using one of the lines). See (LP: #1754358) for the
# discussion.
#
# About using servers from the NTP Pool Project in general see (LP: #104525).
# Approved by Ubuntu Technical Board on 2011-02-08.
# See http://www.pool.ntp.org/join.html for more information.
#pool ntp.ubuntu.com        iburst maxsources 4
#pool 0.ubuntu.pool.ntp.org iburst maxsources 1
#pool 1.ubuntu.pool.ntp.org iburst maxsources 1
#pool 2.ubuntu.pool.ntp.org iburst maxsources 2

#这里是新添加的
server controller iburst
allow 0.0.0.0/0

# This directive specify the location of the file containing ID/key pairs for
# NTP authentication.
keyfile /etc/chrony/chrony.keys

# This directive specify the file into which chronyd will store the rate
# information.
driftfile /var/lib/chrony/chrony.drift

# Uncomment the following line to turn logging on.
#log tracking measurements statistics

# Log files location.
logdir /var/log/chrony

# Stop bad estimates upsetting machine clock.
maxupdateskew 100.0

# This directive enables kernel synchronisation (every 11 minutes) of the
# real-time clock. Note that it can’t be used along with the 'rtcfile' directive.
rtcsync

# Step the system clock instead of slewing it if the adjustment is larger than
# one second, but only in the first three clock updates.
makestep 1 3
#这里是新添加的
local stratum 10
```
重启 chrony 服务 `sudo service chrony restart`
检查是否设置成功
执行 `chronyc sources` 如果是 ^* 说明配置好了，如果是 ? 说明没有连接服务器
或者执行 `timedatectl` System clock synchronized 会变成 yes，否则是 no

设置时间同步：
```
sudo dpkg-reconfigure tzdata   #选择亚洲上海
sudo apt-get install ntpdate
sudo ntpdate cn.pool.ntp.org
```

> ### 1.6 下载OpenStack软件包

`sudo add-apt-repository cloud-archive:yoga`
安装客户端
`sudo apt install python3-openstackclient python3-pip`
1. 数据库
`sudo apt install python3-pymysql`
`sudo apt install mariadb-server`
创建并写入文件 `sudo vi /etc/mysql/mariadb.conf.d/99-openstack.cnf`
内容如下
```
[mysqld]
bind-address = 10.0.24.13
default-storage-engine = innodb
innodb_file_per_table = on
max_connections = 4096
collation-server = utf8_general_ci
character-set-server = utf8
```
重启数据库 `sudo service mysql restart`
切换到 root，随后配置一下密码 `mysql_secure_installation`
2. 消息队列
`sudo apt install rabbitmq-server`
创建 openstack 用户 `sudo rabbitmqctl add_user openstack admin` 用户名为 openstack ，密码为 admin
赋予权限 `sudo rabbitmqctl set_permissions openstack ".*" ".*" ".*"`
文件目录在 /usr/lib/rabbitmq/lib/rabbitmq_server-3.8.2/sbin
3. 缓存
安装 `sudo apt install memcached python3-memcache -y`
修改配置文件 `sudo vi /etc/memcached.conf` 将 127.0.0.1 替换为 controller 对应的 IP 地址
重启服务 `sudo service memcached restart`
4. etcd
`sudo apt install etcd -y`
修改配置文件 `sudo vi /etc/default/etcd` 内容如下，注意一些需要换成 IP 地址的地方
```
ETCD_NAME="controller"
ETCD_DATA_DIR="/var/lib/etcd"
ETCD_INITIAL_CLUSTER_STATE="new"
ETCD_INITIAL_CLUSTER_TOKEN="etcd-cluster-01"
ETCD_INITIAL_CLUSTER="controller=http://10.0.24.13:2380"
ETCD_INITIAL_ADVERTISE_PEER_URLS="http://10.0.24.13:2380"
ETCD_ADVERTISE_CLIENT_URLS="http://10.0.24.13:2379"
ETCD_LISTEN_PEER_URLS="http://0.0.0.0:2380"
ETCD_LISTEN_CLIENT_URLS="http://10.0.24.13:2379"
```
启动 etcd 服务
`systemctl enable etcd`
`systemctl restart etcd`

***

## 二、OpenStack

> ### 2.1 Keystone

进入root
进入 MySQL `mysql -uroot -p` 输入密码
或者 `mysql` 不用输入密码
```
CREATE DATABASE keystone;
GRANT ALL PRIVILEGES ON keystone.* TO 'keystone'@'localhost' IDENTIFIED BY 'admin';
GRANT ALL PRIVILEGES ON keystone.* TO 'keystone'@'%' IDENTIFIED BY 'admin';
```
注意这里的 IDENTIFIED BY 后面的 admin，意思是设置 MySQL 中 keystone 用户的密码
安装 keystone 组件 `sudo apt install keystone`
安装一个小工具，方便修改配置文件
`sudo apt install git`
`sduo git config --global --unset http.https://github.com.proxy`
`sudo git clone https://github.com/pixelb/crudini`
`sudo apt install crudini`
修改配置文件 `sudo vi /etc/keystone/keystone.conf`
```
[database]
"mysql+pymysql://keystone:上面设置的密码@controller/keystone"

[token]
provider fernet
```
也可以用 crudini：
`crudini --set /etc/keystone/keystone.conf database connection "mysql+pymysql://keystone:admin@controller/keystone"`
`crudini --set /etc/keystone/keystone.conf token provider fernet`
填充数据库 `su -s /bin/sh -c "keystone-manage db_sync" keystone`
初始化令牌仓库
`keystone-manage fernet_setup --keystone-user keystone --keystone-group keystone`
`keystone-manage credential_setup --keystone-user keystone --keystone-group keystone`
创建管理员用户
```
keystone-manage bootstrap --bootstrap-password admin \
  --bootstrap-admin-url http://controller:5000/v3/ \
  --bootstrap-internal-url http://controller:5000/v3/ \
  --bootstrap-public-url http://controller:5000/v3/ \
  --bootstrap-region-id RegionOne
```
`sudo vi /etc/apache2/apache2.conf`
往文件中添加 `ServerName controller`
重启apache，`sudo service apache2 restart`
注意处在普通用户下，创建一个文件 `vi adminrc_keystone`，输入内容如下
```
export OS_USERNAME=admin
export OS_PASSWORD=admin
export OS_PROJECT_NAME=admin
export OS_USER_DOMAIN_NAME=Default
export OS_PROJECT_DOMAIN_NAME=Default
export OS_AUTH_URL=http://controller:5000/v3
export OS_IDENTITY_API_VERSION=3
```
`source adminrc_keystone`
分别创建相应的domain、projects等：
```
openstack project create --domain default --description "Service Project" service
openstack project create --domain default --description "Demo Project" demo
openstack user create --domain default --password demo demo
openstack role create role_demo
openstack role add --project demo --user demo role_demo
```
最后验证一下 `openstack token issue`

> ### 2.2 Glance

```
CREATE DATABASE glance;
GRANT ALL PRIVILEGES ON glance.* TO 'glance'@'localhost' IDENTIFIED BY 'admin';
GRANT ALL PRIVILEGES ON glance.* TO 'glance'@'%' IDENTIFIED BY 'admin';
```
`apt install glance -y`
```
openstack user create --domain default --password-prompt glance
或者
openstack user create --domain default --password admin glance

openstack role add --project service --user glance admin
openstack service create --name glance --description "OpenStack Image" image
openstack endpoint create --region RegionOne image public http://controller:9292
openstack endpoint create --region RegionOne image internal http://controller:9292
openstack endpoint create --region RegionOne image admin http://controller:9292
```
`sudo vi /etc/glance/glance-api.conf`
```
[database] 1746
# ...
connection = mysql+pymysql://glance:admin@controller/glance

[glance_store] 3141
# ...
stores = file,http
default_store = file
filesystem_store_datadir = /var/lib/glance/images/

[keystone_authtoken] 4970
# ...
www_authenticate_uri = http://controller:5000
auth_url = http://controller:5000
memcached_servers = controller:11211
auth_type = password
project_domain_name = Default
user_domain_name = Default
project_name = service
username = glance
password = admin

[oslo_limit]
auth_url = http://controller:5000
auth_type = password
user_domain_id = default
username = glance
system_scope = all
password = admin
service_name = glance
region_name = RegionOne

[paste_deploy] 5685
# ...
flavor = keystone
```
处于普通用户下，授予glance用户权限 `openstack role add --user glance --user-domain Default --system all reader`
填充数据库 `su -s /bin/sh -c "glance-manage db_sync" glance`
重启服务 `service glance-api restart`
下载镜像 `wget http://download.cirros-cloud.net/0.4.0/cirros-0.4.0-x86_64-disk.img`
上传 glance
```
glance image-create --name "cirros" \
  --file cirros-0.4.0-x86_64-disk.img \
  --disk-format qcow2 --container-format bare \
  --visibility=public
```
可以使用 `openstack image list` 或者 `glance image-list` 查看镜像

> ### 2.3 Placement

```
CREATE DATABASE placement;
GRANT ALL PRIVILEGES ON placement.* TO 'placement'@'localhost' IDENTIFIED BY 'admin';
GRANT ALL PRIVILEGES ON placement.* TO 'placement'@'%' IDENTIFIED BY 'admin';
```
```
openstack user create --domain default --password admin placement
openstack role add --project service --user placement admin
openstack service create --name placement --description "Placement API" placement
openstack endpoint create --region RegionOne placement public http://controller:8778
openstack endpoint create --region RegionOne placement internal http://controller:8778
openstack endpoint create --region RegionOne placement admin http://controller:8778
```
`apt install placement-api`
```
crudini --set /etc/placement/placement.conf placement_database connection "mysql+pymysql://placement:admin@controller/placement"
crudini --set /etc/placement/placement.conf api auth_strategy "keystone"

crudini --set /etc/placement/placement.conf keystone_authtoken auth_url "http://controller:5000/v3"
crudini --set /etc/placement/placement.conf keystone_authtoken memcached_servers "controller:11211"
crudini --set /etc/placement/placement.conf keystone_authtoken auth_type "password"
crudini --set /etc/placement/placement.conf keystone_authtoken project_domain_name "Default"
crudini --set /etc/placement/placement.conf keystone_authtoken user_domain_name "Default"
crudini --set /etc/placement/placement.conf keystone_authtoken project_name "service"
crudini --set /etc/placement/placement.conf keystone_authtoken username "placement"
crudini --set /etc/placement/placement.conf keystone_authtoken password admin
echo 'succeed to config placement.conf [keystone_authtoken]'

su -s /bin/sh -c "placement-manage db sync" placement
echo 'succeed to fullfill placement database'

service apache2 restart
echo 'succeed restart apache2'
```
验证是否配置好 `placement-status upgrade check`
`pip3 install osc-placement`

> ### 2.4 Nova

因为是allinone的模式，所以先执行控制节点，然后再执行计算节点
```
CREATE DATABASE nova_api;
CREATE DATABASE nova;
CREATE DATABASE nova_cell0;

GRANT ALL PRIVILEGES ON nova_api.* TO 'nova'@'localhost' IDENTIFIED BY 'admin';
GRANT ALL PRIVILEGES ON nova_api.* TO 'nova'@'%' IDENTIFIED BY 'admin';

GRANT ALL PRIVILEGES ON nova.* TO 'nova'@'localhost' IDENTIFIED BY 'admin';
GRANT ALL PRIVILEGES ON nova.* TO 'nova'@'%' IDENTIFIED BY 'admin';

GRANT ALL PRIVILEGES ON nova_cell0.* TO 'nova'@'localhost' IDENTIFIED BY 'admin';
GRANT ALL PRIVILEGES ON nova_cell0.* TO 'nova'@'%' IDENTIFIED BY 'admin';
```
```
openstack user create --domain default --password admin nova
openstack role add --project service --user nova admin
openstack service create --name nova --description "OpenStack Compute" compute

openstack endpoint create --region RegionOne compute public http://controller:8774/v2.1
openstack endpoint create --region RegionOne compute internal http://controller:8774/v2.1
openstack endpoint create --region RegionOne compute admin http://controller:8774/v2.1
```
控制节点
`apt install nova-api nova-conductor nova-novncproxy nova-scheduler`
`vi /etc/nova/nova.conf`
```
[api_database] 1090
connection = mysql+pymysql://nova:admin@10.0.24.13/nova_api
[database] 1775
connection = mysql+pymysql://nova:admin@10.0.24.13/nova
[default]
transport_url = rabbit://openstack:admin@10.0.24.13:5672/
[api] 880
auth_strategy = keystone
[keystone_authtoken] 2700
www_authenticate_uri = http://10.0.24.13:5000/
auth_url = http://10.0.24.13:5000/
memcached_servers = 10.0.24.13:11211
auth_type = password
project_domain_name = Default
user_domain_name = Default
project_name = service
username = nova
password = admin

[DEFAULT]
my_ip = 10.0.24.13

[vnc] 5373
enabled = true
server_listen = 10.0.24.13
server_proxyclient_address = 10.0.24.13

[glance] 2078
api_servers = http://10.0.24.13:9292

[oslo_concurrency] 3767
lock_path = /var/lib/nova/tmp

[placement] 4335
region_name = RegionOne
project_domain_name = Default
project_name = service
auth_type = password
user_domain_name = Default
auth_url = http://10.0.24.13:5000/v3
username = placement
password = admin
```
```
crudini --set /etc/nova/nova.conf api_database connection "mysql+pymysql://nova:admin@controller/nova_api"
crudini --set /etc/nova/nova.conf database connection "mysql+pymysql://nova:admin@controller/nova"
crudini --set /etc/nova/nova.conf DEFAULT transport_url "rabbit://openstack:admin@controller:5672/"
crudini --set /etc/nova/nova.conf api auth_strategy "keystone"
echo 'succeed to config database ,DEFAULT ,api in nova.conf'

crudini --set /etc/nova/nova.conf keystone_authtoken www_authenticate_uri "http://controller:5000/"
crudini --set /etc/nova/nova.conf keystone_authtoken auth_url "http://controller:5000/"
crudini --set /etc/nova/nova.conf keystone_authtoken memcached_servers "controller:11211"
crudini --set /etc/nova/nova.conf keystone_authtoken auth_type password
crudini --set /etc/nova/nova.conf keystone_authtoken project_domain_name Default
crudini --set /etc/nova/nova.conf keystone_authtoken user_domain_name Default
crudini --set /etc/nova/nova.conf keystone_authtoken project_name service
crudini --set /etc/nova/nova.conf keystone_authtoken username nova
crudini --set /etc/nova/nova.conf keystone_authtoken password admin
echo 'succeed to config keystone_authtoken in nova.conf'

crudini --set /etc/nova/nova.conf DEFAULT my_ip 10.0.24.13

crudini --set /etc/nova/nova.conf vnc enabled true
crudini --set /etc/nova/nova.conf vnc my_ip 10.0.24.13

crudini --set /etc/nova/nova.conf glance api_servers "http://controller:9292"
crudini --set /etc/nova/nova.conf oslo_concurrency lock_path "/var/lib/nova/tmp"
echo 'succeed config my_ip ,vnc ,glance in nova.conf'

crudini --set /etc/nova/nova.conf placement region_name RegionOne
crudini --set /etc/nova/nova.conf placement project_domain_name Default
crudini --set /etc/nova/nova.conf placement project_name service
crudini --set /etc/nova/nova.conf placement auth_type password
crudini --set /etc/nova/nova.conf placement user_domain_name Default
crudini --set /etc/nova/nova.conf placement auth_url "http://controller:5000/v3"
crudini --set /etc/nova/nova.conf placement username placement
crudini --set /etc/nova/nova.conf placement password admin
echo 'succeed to config placement in nova.conf'

su -s /bin/sh -c "nova-manage api_db sync" nova
echo 'succeed to sync nova api database'
su -s /bin/sh -c "nova-manage cell_v2 map_cell0" nova
echo 'succeed to register cell0 database'
su -s /bin/sh -c "nova-manage cell_v2 create_cell --name=cell1 --verbose" nova
su -s /bin/sh -c "nova-manage db sync" nova
echo 'succeed to fullfill nova database'
su -s /bin/sh -c "nova-manage cell_v2 list_cells" nova

service nova-api restart
service nova-scheduler restart
service nova-conductor restart
service nova-novncproxy restart
```
下面是计算节点
`apt install nova-compute`
`vi /etc/nova/nova.conf`
```
[DEFAULT]
transport_url = rabbit://openstack:admin@10.0.24.13

[api]
auth_strategy = keystone

[keystone_authtoken]
www_authenticate_uri = http://10.0.24.13:5000/
auth_url = http://10.0.24.13:5000/
memcached_servers = 10.0.24.13:11211
auth_type = password
project_domain_name = Default
user_domain_name = Default
project_name = service
username = nova
password = admin

[DEFAULT]
my_ip = 10.0.24.13

[vnc]
enabled = true
server_listen = 0.0.0.0
server_proxyclient_address = 10.0.24.13
novncproxy_base_url = http://10.0.24.13:6080/vnc_auto.html

[glance]
api_servers = http://10.0.24.13:9292

[oslo_concurrency]
lock_path = /var/lib/nova/tmp

[placement]
region_name = RegionOne
project_domain_name = Default
project_name = service
auth_type = password
user_domain_name = Default
auth_url = http://10.0.24.13:5000/v3
username = placement
password = admin
```
```
crudini --set /etc/nova/nova.conf DEFAULT transport_url "rabbit://openstack:admin@controller"
crudini --set /etc/nova/nova.conf api auth_strategy keystone
echo 'succeed to config database ,api in nova.conf'

crudini --set /etc/nova/nova.conf keystone_authtoken www_authenticate_uri "http://controller:5000/"
crudini --set /etc/nova/nova.conf keystone_authtoken auth_url "http://controller:5000/"
crudini --set /etc/nova/nova.conf keystone_authtoken memcached_servers "controller:11211"
crudini --set /etc/nova/nova.conf keystone_authtoken auth_type password
crudini --set /etc/nova/nova.conf keystone_authtoken project_domain_name Default
crudini --set /etc/nova/nova.conf keystone_authtoken user_domain_name Default
crudini --set /etc/nova/nova.conf keystone_authtoken project_name service
crudini --set /etc/nova/nova.conf keystone_authtoken username nova
crudini --set /etc/nova/nova.conf keystone_authtoken password admin
echo 'succeed to config keystone_authtoken in nova.conf'

crudini --set /etc/nova/nova.conf DEFAULT my_ip 10.0.24.13
crudini --set /etc/nova/nova.conf vnc enabled true
crudini --set /etc/nova/nova.conf vnc server_listen "0.0.0.0"
crudini --set /etc/nova/nova.conf vnc server_proxyclient_address 10.0.24.13
crudini --set /etc/nova/nova.conf vnc novncproxy_base_url "http://controller:6080/vnc_auto.html"
echo 'succeed to config vnc in nova.conf'

crudini --set /etc/nova/nova.conf glance api_servers "http://controller:9292"
crudini --set /etc/nova/nova.conf oslo_concurrency lock_path "/var/lib/nova/tmp"
echo 'succeed to config glance ,oslo_concurrency in nova.conf'

crudini --set /etc/nova/nova.conf placement region_name RegionOne
crudini --set /etc/nova/nova.conf placement project_domain_name Default
crudini --set /etc/nova/nova.conf placement project_name service
crudini --set /etc/nova/nova.conf placement auth_type password
crudini --set /etc/nova/nova.conf placement user_domain_name Default
crudini --set /etc/nova/nova.conf placement auth_url "http://controller:5000/v3"
crudini --set /etc/nova/nova.conf placement username placement
crudini --set /etc/nova/nova.conf placement password admin
echo 'succeed to config placement in nova.conf'

crudini --set /etc/nova/nova-compute.conf libvirt virt_type qemu

service nova-compute restart
echo 'succeed to restart nova-compute'
```

> ### 2.5 Neutron

先是控制节点
```
CREATE DATABASE neutron;
GRANT ALL PRIVILEGES ON neutron.* TO 'neutron'@'localhost' IDENTIFIED BY 'admin';
GRANT ALL PRIVILEGES ON neutron.* TO 'neutron'@'%' IDENTIFIED BY 'admin';
```
```
openstack user create --domain default --password admin neutron
openstack role add --project service --user neutron admin
openstack service create --name neutron --description "OpenStack Networking" network
openstack endpoint create --region RegionOne network public http://controller:9696
openstack endpoint create --region RegionOne network internal http://controller:9696
openstack endpoint create --region RegionOne network admin http://controller:9696
```
选择创建自服务服务网络
`apt install neutron-server neutron-plugin-ml2 neutron-linuxbridge-agent neutron-l3-agent neutron-dhcp-agent neutron-metadata-agent`
```
crudini --set /etc/neutron/neutron.conf database connection "mysql+pymysql://neutron:admin@controller/neutron"
crudini --set /etc/neutron/neutron.conf DEFAULT core_plugin ml2
crudini --set /etc/neutron/neutron.conf DEFAULT service_plugins router
crudini --set /etc/neutron/neutron.conf DEFAULT allow_overlapping_ips true
crudini --set /etc/neutron/neutron.conf DEFAULT transport_url "rabbit://openstack:admin@controller"
crudini --set /etc/neutron/neutron.conf DEFAULT auth_strategy keystone
crudini --set /etc/neutron/neutron.conf DEFAULT notify_nova_on_port_status_changes true
crudini --set /etc/neutron/neutron.conf DEFAULT notify_nova_on_port_data_changes true
echo 'succeed to config DEFAULT in neutron.conf'

crudini --set /etc/neutron/neutron.conf keystone_authtoken www_authenticate_uri "http://controller:5000"
crudini --set /etc/neutron/neutron.conf keystone_authtoken auth_url "http://controller:5000"
crudini --set /etc/neutron/neutron.conf keystone_authtoken memcached_servers "controller:11211"
crudini --set /etc/neutron/neutron.conf keystone_authtoken auth_type password
crudini --set /etc/neutron/neutron.conf keystone_authtoken project_domain_name Default
crudini --set /etc/neutron/neutron.conf keystone_authtoken user_domain_name Default
crudini --set /etc/neutron/neutron.conf keystone_authtoken project_name service
crudini --set /etc/neutron/neutron.conf keystone_authtoken username neutron
crudini --set /etc/neutron/neutron.conf keystone_authtoken password admin
echo 'succeed to config keystone_authtoken in neutron.conf'

crudini --set /etc/neutron/neutron.conf nova auth_url "http://controller:5000"
crudini --set /etc/neutron/neutron.conf nova auth_type password
crudini --set /etc/neutron/neutron.conf nova project_domain_name Default
crudini --set /etc/neutron/neutron.conf nova user_domain_name Default
crudini --set /etc/neutron/neutron.conf nova region_name RegionOne
crudini --set /etc/neutron/neutron.conf nova project_name service
crudini --set /etc/neutron/neutron.conf nova username nova
crudini --set /etc/neutron/neutron.conf nova password admin
echo 'succeed to config nova in neutron.conf'

crudini --set /etc/neutron/neutron.conf oslo_concurrency lock_path "/var/lib/neutron/tmp"
echo 'succeed to config oslo_concurrency in neutron.conf'

crudini --set /etc/neutron/plugins/ml2/ml2_conf.ini ml2 type_drivers "flat,vlan,vxlan"
crudini --set /etc/neutron/plugins/ml2/ml2_conf.ini ml2 tenant_network_types vxlan
crudini --set /etc/neutron/plugins/ml2/ml2_conf.ini ml2 mechanism_drivers "linuxbridge,l2population"
crudini --set /etc/neutron/plugins/ml2/ml2_conf.ini ml2 extension_drivers port_security
echo 'succeed to config ml2 in ml2_conf.conf'

crudini --set /etc/neutron/plugins/ml2/ml2_conf.ini ml2_type_flat flat_networks provider
crudini --set /etc/neutron/plugins/ml2/ml2_conf.ini securitygroup enable_ipset true
crudini --set /etc/neutron/plugins/ml2/ml2_conf.ini ml2_type_vxlan vni_ranges "1:1000"
echo 'succeed to config ml2_type_* in ml2_conf.conf'

# 注意这里的 ens33
crudini --set /etc/neutron/plugins/ml2/linuxbridge_agent.ini linux_bridge physical_interface_mappings "provider:eth0"
crudini --set /etc/neutron/plugins/ml2/linuxbridge_agent.ini vxlan enable_vxlan true
crudini --set /etc/neutron/plugins/ml2/linuxbridge_agent.ini vxlan local_ip 10.0.24.13
crudini --set /etc/neutron/plugins/ml2/linuxbridge_agent.ini vxlan l2_population true
crudini --set /etc/neutron/plugins/ml2/linuxbridge_agent.ini securitygroup enable_security_group true
crudini --set /etc/neutron/plugins/ml2/linuxbridge_agent.ini securitygroup firewall_driver "neutron.agent.linux.iptables_firewall.IptablesFirewallDriver"
echo 'succeed to config linuxbridge.conf'

crudini --set /etc/neutron/l3_agent.ini DEFAULT interface_driver linuxbridge
echo 'succeed to config l3_agent.conf'

crudini --set /etc/neutron/dhcp_agent.ini DEFAULT interface_driver linuxbridge
crudini --set /etc/neutron/dhcp_agent.ini DEFAULT dhcp_driver "neutron.agent.linux.dhcp.Dnsmasq"
crudini --set /etc/neutron/dhcp_agent.ini DEFAULT enable_isolated_metadata true
echo 'succeed to config dhcp_agent.conf'

crudini --set /etc/neutron/metadata_agent.ini DEFAULT nova_metadata_host controller
crudini --set /etc/neutron/metadata_agent.ini DEFAULT metadata_proxy_shared_secret 123456
echo 'succeed to config metadata_agent.conf'

crudini --set /etc/nova/nova.conf neutron auth_url "http://controller:5000"
crudini --set /etc/nova/nova.conf neutron auth_type password
crudini --set /etc/nova/nova.conf neutron project_domain_name Default
crudini --set /etc/nova/nova.conf neutron user_domain_name Default
crudini --set /etc/nova/nova.conf neutron region_name RegionOne
crudini --set /etc/nova/nova.conf neutron project_name service
crudini --set /etc/nova/nova.conf neutron username neutron
crudini --set /etc/nova/nova.conf neutron password admin
crudini --set /etc/nova/nova.conf neutron service_metadata_proxy true
crudini --set /etc/nova/nova.conf neutron metadata_proxy_shared_secret 123456
echo 'succeed to config neutron in nova.conf'

su -s /bin/sh -c "neutron-db-manage --config-file /etc/neutron/neutron.conf --config-file /etc/neutron/plugins/ml2/ml2_conf.ini upgrade head" neutron
echo 'succeed to fullfill neutron database'

service nova-api restart
service neutron-server restart
service neutron-linuxbridge-agent restart
service neutron-dhcp-agent restart
service neutron-metadata-agent restart
service neutron-l3-agent restart
echo 'succeed to restart services'
```
计算节点
`apt install neutron-linuxbridge-agent`
```
crudini --set /etc/neutron/neutron.conf DEFAULT transport_url "rabbit://openstack:admin@controller"
crudini --set /etc/neutron/neutron.conf DEFAULT auth_strategy keystone
echo 'succeed to config DEFAULT in neutron.conf'

crudini --set /etc/neutron/neutron.conf keystone_authtoken www_authenticate_uri "http://controller:5000"
crudini --set /etc/neutron/neutron.conf keystone_authtoken auth_url "http://controller:5000"
crudini --set /etc/neutron/neutron.conf keystone_authtoken memcached_servers "controller:11211"
crudini --set /etc/neutron/neutron.conf keystone_authtoken auth_type password
crudini --set /etc/neutron/neutron.conf keystone_authtoken project_domain_name Default
crudini --set /etc/neutron/neutron.conf keystone_authtoken user_domain_name Default
crudini --set /etc/neutron/neutron.conf keystone_authtoken project_name service
crudini --set /etc/neutron/neutron.conf keystone_authtoken username neutron
crudini --set /etc/neutron/neutron.conf keystone_authtoken password admin
echo 'succeed to config keystone_authtoken in neutron.conf'

crudini --set /etc/neutron/neutron.conf oslo_concurrency lock_path "/var/lib/neutron/tmp"
echo 'succeed to config oslo in neutron.conf'

# 注意下面的provider:ens33，用ifconfig命令查看一下
crudini --set /etc/neutron/plugins/ml2/linuxbridge_agent.ini linux_bridge physical_interface_mappings "provider:eth0"
crudini --set /etc/neutron/plugins/ml2/linuxbridge_agent.ini vxlan enable_vxlan true
crudini --set /etc/neutron/plugins/ml2/linuxbridge_agent.ini vxlan local_ip 10.0.24.13
crudini --set /etc/neutron/plugins/ml2/linuxbridge_agent.ini vxlan l2_population true
crudini --set /etc/neutron/plugins/ml2/linuxbridge_agent.ini securitygroup enable_security_group true
crudini --set /etc/neutron/plugins/ml2/linuxbridge_agent.ini securitygroup firewall_driver "neutron.agent.linux.iptables_firewall.IptablesFirewallDriver"
echo 'succeed to config linuxbridge_agent.ini'

crudini --set /etc/nova/nova.conf neutron auth_url "http://controller:5000"
crudini --set /etc/nova/nova.conf neutron auth_type password
crudini --set /etc/nova/nova.conf neutron project_domain_name Default
crudini --set /etc/nova/nova.conf neutron user_domain_name Default
crudini --set /etc/nova/nova.conf neutron region_name RegionOne
crudini --set /etc/nova/nova.conf neutron project_name service
crudini --set /etc/nova/nova.conf neutron username neutron
crudini --set /etc/nova/nova.conf neutron password admin
echo 'succeed to config neutron in nova.conf'

service nova-compute restart
service neutron-linuxbridge-agent restart
echo 'succeed to restart services'
```
验证 `openstack extension list --network`
`openstack network agent list`

> ### 2.6 Horizon

`apt install openstack-dashboard`
`vi /etc/openstack-dashboard/local_settings.py`
```
126
OPENSTACK_HOST = "controller"
399
ALLOWED_HOSTS = ['*']
112
SESSION_ENGINE = 'django.contrib.sessions.backends.cache'

CACHES = {
    'default': {
         'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
         'LOCATION': 'controller:11211',
    }
}
OPENSTACK_KEYSTONE_URL = "http://%s:5000" % OPENSTACK_HOST
OPENSTACK_KEYSTONE_MULTIDOMAIN_SUPPORT = True
OPENSTACK_API_VERSIONS = {
    "identity": 3,
    "image": 2,
    "volume": 3,
}
OPENSTACK_KEYSTONE_DEFAULT_DOMAIN = "Default"
OPENSTACK_KEYSTONE_DEFAULT_ROLE = "member"
OPENSTACK_NEUTRON_NETWORK = {
    ...
    'enable_router': False,
    'enable_quotas': False,
    'enable_ipv6': False,
    'enable_distributed_router': False,
    'enable_ha_router': False,
    'enable_fip_topology_check': False,
}
TIME_ZONE = "Asia/Shanghai"
```

检验安装结果 `nova-status upgrade check`
使用可视化界面，浏览器访问 `http://IP地址/horizon`
账号密码即 adminrc_keystone 里面的内容

***

## 三、遇到的一些问题

> ### 3.1 [ifconfig 命令无网络接口 ens33](https://www.cnblogs.com/PatrickLiu/p/8443019.html#:~:text=%E6%88%91%E5%B0%B1%E4%BD%BF%E7%94%A8%20ifconfig%20%E5%91%BD%E4%BB%A4%E5%9C%A8Linux,%E7%B3%BB%E7%BB%9F%E4%B8%8B%E7%9A%84%E5%91%BD%E4%BB%A4%E8%A1%8C%E6%89%A7%E8%A1%8C%E6%9D%A5%E6%A3%80%E6%9F%A5%E4%B8%80%E4%B8%8BIP%E9%85%8D%E7%BD%AE%E4%BF%A1%E6%81%AF%EF%BC%8Cifconfig%20%E5%91%BD%E4%BB%A4%E4%B8%8B%E5%8F%91%E7%8E%B0%E7%BD%91%E7%BB%9C%E6%8E%A5%E5%8F%A3ens33%E4%B8%8D%E8%A7%81%E4%BA%86%EF%BC%8C%E5%8F%AA%E6%9C%89%E7%8E%AF%E5%9B%9E%E5%8F%A3%EF%BC%8C%E6%95%88%E6%9E%9C%E5%A6%82%E4%B8%8B%E6%88%AA%E5%9B%BE%EF%BC%9A%20%E4%BB%A5%E5%89%8D%E7%9A%84IP%E5%9C%B0%E5%9D%80%E6%B2%A1%E6%9C%89%E4%BA%86%EF%BC%8C%E5%8F%AA%E5%89%A9%E4%B8%8B%E8%BF%99%E4%B8%AA%E6%9C%AC%E5%9C%B0%E5%9C%B0%E5%9D%80%E4%BA%86127.0.0.1%EF%BC%8C%E5%8E%9F%E6%9D%A5%E9%97%AE%E9%A2%98%E5%87%BA%E7%8E%B0%E5%9C%A8%E8%BF%99%E9%87%8C%E3%80%82)

不是接口不存在，只是接口没有UP。需要先启用网络，启用网络时会调用/sbin/dhclient，于是执行 `sudo /sbin/dhclient` 即可

> ### 3.2 [log文件中报错 Failed to create resource provider controller](https://www.cnblogs.com/jimmyyang/p/13143453.html)

`mysql`
```
SHOW databases;
USE nova-api;
SELECT * FROM resource_provider;
```
数据库中的表resource_provider要是没有任何数据，应该是没有写入成功，所以可能是placement的相关权限出了问题
返回查看安装步骤中，配置文件是否出现错误

> ### 3.3 [rabbitmq问题](https://blog.csdn.net/Qevery678/article/details/102599863)

https://blog.csdn.net/qq_41887560/article/details/106194494
注意 /etc/hosts 文件的配置
127.0.0.1 那一行后面需要加上 hostname
127.0.1.1 那一行需要注释掉
重启服务 `sudo systemctl restart rabbitmq.server`
查看状态 `sudo systemctl status rabbitmq.server`


> ### 3.4 [dashboard 登陆认证失败，显示 invalid credentials](https://blog.csdn.net/weixin_43863487/article/details/109604903)

`vi /etc/openstack-dashboard/local_settings.py`
修改端口号

> ### 3.5 如何创建flavor 

`nova flavor-list`
`nova flavor-create --is-public true boshen_ram_1024_disk_1_vcpus_1 boshen_ram_1024_disk_1_vcpus_1 1024 1 1`
`nova flavor-delete {name}`

> ### 3.6 openstack用户管理

`openstack user list`
`openstack user delete glance`

`openstack service list`
`openstack service delete <service ID>`

> ### 3.7 [运行 VNC 灰屏问题](https://blog.csdn.net/weixin_56017984/article/details/120519449?utm_medium=distribute.pc_relevant.none-task-blog-2~default~baidujs_baidulandingword~default-4-120519449-blog-109578971.pc_relevant_3mothn_strategy_recovery&spm=1001.2101.3001.4242.3&utm_relevant_index=7)

配置防火墙端口
`sudo -i`
`sudo apt update`
`sudo apt install gnome-panel gnome-settings-daemon metacity nautilus gnome-terminal ubuntu-desktop`
`sudo apt-get install tightvncserver`
`sudo vncserver`
`sudo vi ~/.vnc/xstartup`
```
#!/bin/bash
export $(dbus-launch)  
export XKL_XMODMAP_DISABLE=1
unset SESSION_MANAGER

gnome-panel &
gnome-settings-daemon &
metacity &
nautilus &
gnome-terminal &

# [ -x /etc/vnc/xstartup ] && exec /etc/vnc/xstartup
# [ -r $HOME/.Xresources ] && xrdb $HOME/.Xresources

xsetroot -solid grey
vncconfig -iconic &
x-terminal-emulator -geometry 80x24+10+10 -ls -title "$VNCDESKTOP Desktop" &
gnome-session &

VNCSERVERS="2:root"
VNCSERVERARGS[1]="-GEOMETRY 800×600"
```
`sudo vncserver -kill :1 #杀掉原桌面进程，输入命令（其中的:1是桌面号）`
`sudo vncserver -geometry 1920x1080 :1 #生成新的会话`
下载 VNC viewer，https://www.realvnc.com/en/connect/download/viewer/

***

## 参考文档

1. https://blog.csdn.net/qq_41037945/article/details/124286616
2. crudini工具，https://github.com/pixelb/crudini









