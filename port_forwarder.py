import time
import socket
import _thread
import sys
import getopt


# Buffer size
buffer = 2048
backlog = 10
localhost = '127.0.0.1'

def socket_pipeline(source, sink):
    print("Socket pipeline created from {} to {}".format(
        source.getpeername(), sink.getpeername()))
    global buffer
    while True:
        try:
            data = source.recv(buffer)
            if not data:
                break
            sink.send(data)
        except Exception as ex:
            print("error {}".format(ex))
            raise ex
    source.close()
    sink.close()


def build_tunnel(socket, forward):
    try:
        _thread.start_new_thread(socket_pipeline, (socket, forward))
        _thread.start_new_thread(socket_pipeline, (forward, socket))
    except Exception as e:
        print("error {}".format(e))
        raise e
    while True:
        pass


def full_address(ip, port):
    return "{}:{}".format(ip, port)


def tunnel(from_port, to_ip, to_port, local_ip=''):
    global backlog
    if local_ip is '':
        local_ip = localhost
    if to_ip is '':
        to_ip = localhost
    print("Listening from {} to {}".format(
        full_address(local_ip, from_port), full_address(to_ip, to_port)))
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((local_ip, from_port))
    sock.listen(backlog)
    while True:
        sock, address = sock.accept()
        print("Connected from local port{} to destination {}".format(
            from_port, address[0]))
        forward = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            forward.connect((to_ip, to_port))
            build_tunnel(sock, forward)
        except Exception as ex:
            print("Connection Error {}, retry after 5 seconds ".format(ex))
            time.sleep(5)
            tunnel(from_port, to_ip, to_port, local_ip)


def exception():
    print('Usage : port_forward.py -f <From Port> -i <IP> -p <To Port>')
    sys.exit()


def test():
    tunnel(8089, '127.0.0.1', 8081)


def main(argv):
    from_port = 0
    ip = ''
    to_port = 0
    try:
        opts, args = getopt.getopt(
            argv, "h:f:i:t:", ["help", "from_port=", "ip=", "to_port="])
        if len(opts) != 3:
            exception()
        for opt, arg in opts:
            if opt in ("-h", "--help"):
                exception()
            elif opt in ("-f", "--from_port"):
                from_port = int(arg)
            elif opt in ("-i", "--ip"):
                ip = arg
            elif opt in ("-t", "--to_port"):
                to_port = int(arg)
    except getopt.GetoptError:
        exception()
    tunnel(from_port, ip, to_port)


if __name__ == '__main__':
    test()
    # main(sys.argv[1:])
