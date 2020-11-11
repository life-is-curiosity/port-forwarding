Port-Forward-By-Python
======================

In computer networking, Port forwarding or Port mapping is an application of network address translation (NAT) that redirects a communication request from one address and port number combination to another while the packets are traversing a network gateway. This technique is most commonly used to make services on a host residing on a protected or masqueraded (internal) network available to hosts on the opposite side of the gateway (external network), by remapping the destination IP address and port number of the communication to an internal host.

![Port Forwarding](/port-forwading-in-python.png)

The client side is not allowed to access subnet 192.168.2.0 directly but server 192.168.1.2 can help to redirect the TCP request to the subnet 192.168.2.0. It can also prevent to expose the subnet IP to the public.

### Implementation

We are going to build a tunnel by two threads on the script. One of threads is a socket client and another one is socket server. What we are going to do is connect both of them together and the packet stream can be streaming here.