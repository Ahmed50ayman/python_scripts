import ipaddress

ip = ipaddress.ip_address("192.168.1.2")  # check the ip is v4 or v6

ip = ipaddress.ip_network('192.0.2.0/24') # make all the guess for this subnet mask for this ip make it with for loop 

ip = ipaddress.IPv4Address(1)             # book a number of int like ip add you want for v4 

ip = ipaddress.IPv6Address(1)             #           //    //  //                     for v6

ip = ipaddress.ip_interface('192.0.2.1') # this detect what ip is it and but the subnet mask or you can but it manualy to check 

addr4 = ipaddress.ip_address('192.0.2.1') # make object v4

addr6 = ipaddress.ip_address('2001:db8::1') #           v6

#print(addr4.version)                       #to print the version write 

host4 = ipaddress.ip_interface('192.0.2.1/24') # more detailed than ip_address

host6 = ipaddress.ip_interface('2001:db8::1/96')

#print(host4.network)                       # it will print the network if you write the prefix in the ip becouse he use 32 by defult so this is the host network  from interface with perfix if not exist


#print(host4.netmask)                       #  //           //                      //                //          and subnet mask in onther line

#print(host4.ip)                            # print the only ip 

net4 = ipaddress.ip_network('192.0.0.0/24')

net6 = ipaddress.ip_network('2001:db8::0/96')

#print(net4.num_addresses)                  # Finding out how many individual addresses are in a network

#print(*net4.hosts(),sep="\n")              # make all the guess for this subnet mask for this ip make it with for loop

#print(net4.netmask)                        # print the subnetmask

#print(net6.exploded)                        # it decombresd ipv6

#print(net6.compressed)                      # it combrsed ipv6

# NOTE: you can index any ip address to know to ip after them or before so you can do in thing with spcefic ip like : 

""" if address in network:

    do something

addr4 in ipaddress.ip_network('192.0.2.0/24')


True

>>> addr4 in ipaddress.ip_network('192.0.3.0/24')

False"""
#print(net4[-2])

# NOTE: you can make Comparisons print(ipaddress.ip_address('192.0.2.1') < ipaddress.ip_address('192.0.2.2'))>>True BUT note A TypeError exception is raised if you try to compare objects of different versions or different types.

#print(str(addr4))

#print(int(addr4))  return ip into bytes 

#print(addr6.max_prefixlen)           32 for ipv4      128 for ipv6

#print(addr6.packed)   The binary representation of this address    This is 4 bytes for IPv4 and 16 bytes for IPv6  

#print(addr6.reverse_pointer) it reverse the ip like wildcard but not with ( - ) 

#print(ipaddress.ip_address('224.2.2.2').is_multicast)


#print(ipaddress.ip_address('192.168.1.2').is_private)

#print(ipaddress.ip_address('224.2.2.2').is_global)

#print(ipaddress.ip_address('0.0.0.0').is_unspecified)

#print(ipaddress.ip_address('127.0.0.1').is_loopback)

#print(ipaddress.ip_address('169.254.1.1').is_link_local)

#print(net4.hostmask)  return the wildcard

#print(net4.with_hostmask) ip wiht wildcard

#print(net4.with_netmask) ip with subnetmask

#print(net4.num_addresses) num of address

#print(net4.prefixlen)       return the preifx

#print(*net4.hosts(),sep="\n") All ip can use in this network

#print(*list(ipaddress.ip_network('192.0.2.0/24').subnets(prefixlen_diff=6)),sep="\n") make a subnet mask contain the num if prefixlen_diif

#print(*list(ipaddress.ip_network('192.0.2.0/24').subnets(new_prefix=26)),sep='\n')    make the new privfex with the new_prifix and subnet it with 66 by defult

a = ipaddress.ip_network('192.168.1.0/24')

b = ipaddress.ip_network('192.168.1.128/30')

#print(b.subnet_of(a))                 Return True if this network is a subnet of other

#print(a.supernet_of(b))                Return True if this network is a supernet of other

#print(ipaddress.ip_network('192.0.2.1/32').compare_networks(ipaddress.ip_network('192.0.2.0/32'))) Compare this network to other. In this comparison only the network addresses are considered; host bits aren’t. Returns either -1, 0 or 1.

