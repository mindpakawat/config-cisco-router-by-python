from netmiko import ConnectHandler
            #Authen to Router#
Router_1 = {
            'device_type': 'cisco_ios' ,
            'host': "192.168.2.1" ,
            'username': "admin" ,
            'password': "admin"      }

Router_2 = {
            'device_type': 'cisco_ios' ,
            'host': "192.168.2.2" ,
            'username': "admin" ,
            'password': "admin"      }

Router_3 = {
            'device_type': 'cisco_ios' ,
            'host': "192.168.2.3" ,
            'username': "admin" ,
            'password': "admin"      }

            #Connect to router#
############################################################################ Router 1
net_connect = ConnectHandler(**Router_1)

print("This is Router 1")

config_commands = ['interface f0/1','ip address 192.168.1.1 255.255.255.0',"no shutdown"]
config_int = net_connect.send_config_set(config_commands)
print(config_int)

config_commands = ['router rip','network 192.168.2.0',"network 192.168.1.0"]
config_rip = net_connect.send_config_set(config_commands)
print(config_rip)

ip_brief = net_connect.send_command("show ip int brief")
print(ip_brief)

ip_route = net_connect.send_command('show ip route')
print(ip_route)
############################################################################ Router 2
net_connect = ConnectHandler(**Router_2)

print("This is Router 2")

config_commands = ['interface f0/1','ip address 192.168.3.1 255.255.255.0',"no shutdown"]
config_int = net_connect.send_config_set(config_commands)
print(config_int)

config_commands = ['router rip','network 192.168.2.0',"network 192.168.3.0"]
config_rip = net_connect.send_config_set(config_commands)
print(config_rip)

ip_brief = net_connect.send_command("show ip int brief")
print(ip_brief)

ip_route = net_connect.send_command('show ip route')
print(ip_route)
############################################################################ Router 3
net_connect = ConnectHandler(**Router_3)

print("This is Router 3")

config_commands = ['interface f0/1','ip address 192.168.4.1 255.255.255.0',"no shutdown"]
config_int = net_connect.send_config_set(config_commands)
print(config_int)

config_commands = ['router rip','network 192.168.3.0',"network 192.168.4.0"]
config_rip = net_connect.send_config_set(config_commands)
print(config_rip)

ip_brief = net_connect.send_command("show ip int brief")
print(ip_brief)

ip_route = net_connect.send_command('show ip route')
print(ip_route)