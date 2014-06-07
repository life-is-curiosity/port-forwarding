Port-Forward-By-Python
======================
Just For Backup at 1 Jun 2014

 >>>　From Wikipedia, the free encyclopedia　＜＜＜

Port forwarding or port mapping[1] is a name given to the combined technique of

translating the address or port number of a packet to a new destination
possibly accepting such packet(s) in a packet filter (firewall)
forwarding the packet according to the routing table.
The destination may be a predetermined network port (assuming protocols like TCP and UDP, though the process is not limited to these) on a host within a NAT-masqueraded, typically private network, based on the port number on which it was received at the gateway from the originating host.

The technique is used to permit communications by external hosts with services provided within a private local area network.

Purpose[edit]
Port forwarding allows remote computers (for example, computers on the Internet) to connect to a specific computer or service within a private local-area network (LAN).[3]

In a typical residential network, nodes obtain Internet access through a DSL or cable modem connected to a router or network address translator (NAT/NAPT). Hosts on the private network are connected to an Ethernet switch or communicate via a wireless LAN. The NAT device's external interface is configured with a public IP address. The computers behind the router, on the other hand, are invisible to hosts on the Internet as they each communicate only with a private IP address.

When configuring port forwarding, the network administrator sets aside one port number on the gateway for the exclusive use of communicating with a service in the private network, located on a specific host. External hosts must know this port number and the address of the gateway to communicate with the network-internal service. Often, the port numbers of well-known Internet services, such as port number 80 for web services (HTTP), are used in port forwarding, so that common Internet services may be implemented on hosts within private networks.

Typical applications include the following:

Running a public HTTP server within a private LAN
Permitting Secure Shell access to a host on the private LAN from the Internet
Permitting FTP access to a host on a private LAN from the Internet
Administrators configure port forwarding in the gateway's operating system. In Linux kernels, this is achieved by packet filter rules in the iptables or netfilter kernel components. BSD and Mac OS X operating systems implement it in the Ipfirewall (ipfw) module.

When used on gateway devices, a port forward may be implemented with a single rule to translate the destination address and port. (On Linux kernels, this is DNAT rule). The source address and port are, in this case, left unchanged. When used on machines that are not the default gateway of the network, the source address must be changed to be the address of the translating machine, or packets will bypass the translator and the connection will fail.

When a port forward is implemented by a proxy process (such as on application layer firewalls, SOCKS based firewalls, or via TCP circuit proxies), then no packets are actually translated, only data is proxied. This usually results in the source address (and port number) being changed to that of the proxy machine.

Usually only one of the private hosts can use a specific forwarded port at one time, but configuration is sometimes possible to differentiate access by the originating host's source address.

Unix-like operating systems sometimes use port forwarding where port numbers smaller than 1024 can only be created by software running as the root user. Running with superuser privileges (in order to bind the port) may be a security risk to the host, therefore port forwarding is used to redirect a low-numbered port to another high-numbered port, so that application software may execute as a common operating system user with reduced privileges.

The Universal Plug and Play protocol (UPnP) provides a feature to automatically install instances of port forwarding in residential Internet gateways. UPnP defines the Internet Gateway Device Protocol (IGD) which is a network service by which an Internet gateway advertises its presence on a private network via the Simple Service Discovery Protocol (SSDP). An application that provides an Internet-based service may discover such gateways and use the UPnP IGD protocol to reserve a port number on the gateway and cause the gateway to forward packets to its listening socket.

Types of port forwarding[edit]
Port forwarding can be divided into the following types:[4]

Local port forwarding
Remote port forwarding
Dynamic port forwarding
Local port forwarding[edit]
Local port forwarding is the most common type of port forwarding. It is used to forward data securely from another client application running on the same computer as the Secure Shell Client. Local Port Forwarding lets a user connect from the local computer to another server. By using local port forwarding, firewalls that block certain web pages are able to be bypassed.[5]

Two important items when using local port forwarding are the destination server, and two port numbers. Connections from the SSH client are forwarded via the SSH server, then to a destination server. As stated above, local port forwarding forwards data from another client application running on the same computer as the Secure Shell Client. The Secure Shell client is configured to redirect data from a specified local port through the secure tunnel to a specified destination host and port. This port is on the same computer as the Secure Shell client. Any other client can be configured that is running on the same computer to connect to the forwarded port (rather than directly to the destination host and port). After this connection is established, the Secure Shell client listens on the specified port and redirects all data sent to that port through the secure tunnel to the Secure Shell server. The server decrypts the data, and then directs it to the destination host and port.[6]

On the command line, “-L” specifies local port forwarding. The destination server, and two port numbers need to be included. Port numbers less than 1024 or greater than 49150 are reserved for the system. Some programs will only work with specific source ports, but for the most part any source port number can be used.

Some uses of local port forwarding:

Using local port forwarding to Receive Mail [7]
Connect from a laptop to a website using an SSH tunnel.
Remote port forwarding[edit]
A form of port forwarding that is used for applications connecting to a Secure Shell server in order to use an application that resides on the Secure Shell client-side.[8] In other words, remote port forwarding lets a user connect from a remote Secure Shell server to another server.

To use remote port forwarding, the address of the destination server and two port numbers must be known. The port numbers chosen depend on what application are to be used.

Remote Port Forwarding allows other computers access to applications hosted on remote servers. Two examples:

An employee of a company hosts an FTP server at his own home and wants to give access to the FTP service to employees using computers in the workplace. In order to do this, he can set up remote port forwarding through SSH on the company computers by including his FTP server’s address and using the correct port numbers for FTP (FTP port tcp/21) [9]
Opening remote desktop sessions is a common use of Remote Port Forwarding. Through SSH, this can be accomplished by opening the Virtual Network Computing port (5900) and including the destination computer’s address [6]
Dynamic port forwarding[edit]
Dynamic Port Forwarding (DPF) is an on-demand method of traversing a firewall/NAT through the use of firewall pinholes. The goal is to enable clients to connect securely to a trusted server that acts as an intermediary for the purpose of sending/receiving data to one or many destination servers.[10]

DPF can be implemented by setting up a local application (such as SSH) as a SOCKS proxy server, which can be used to process data transmissions through the network or over the Internet. Programs (such as web browsers) must be configured individually to direct traffic through the proxy, which acts as a secure tunnel to another server. Once the proxy is no longer needed, the programs must be reconfigured to their original settings. Because of the manual requirements of DPF, it is not often used.[6]

Once the connection is established, DPF can be used to provide additional security for a user connected to an untrusted network. Since data must pass through the secure tunnel to another server before being forwarded to its original destination, the user is protected from packet sniffing that may occur on the LAN.[11]

DPF is a powerful tool with many uses.

A user connected to the Internet through a coffee shop, hotel, or otherwise minimally secure network may wish to use DPF as a way of protecting data.
DPF can be used to bypass firewalls that restrict access to outside websites, such as in a corporate network.
DPF can be used as a precaution against hacking.
See also[edit]
