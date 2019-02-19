import socket, struct
def ip2long(ip):
    return struct.unpack("!L",socket.inet_aton(ip))[0]
def long2ip(longip):
    return socket.inet_ntoa(struct.pack('!L', longip))
if __name__ == '__main__':
    print('local ip address to long is %s'%ip2long('127.0.0.1'))
    print('local ip address long to ip is %s'%long2ip(2130706433))
