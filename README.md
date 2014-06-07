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

