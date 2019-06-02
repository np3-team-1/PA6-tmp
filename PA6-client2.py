import sys,socket


def echo_client(server_addr):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STRAEM)
    sock.connect(server_addr)
    print('conneted: ',sock.getpeername())
    while True:
        message = sys.stdin.readline()
        if message :
            msg = "type:get\r\ntime:{0}\r\n".format(message)
            sock.send(msg.encode('utf-8'))
        data = sock.recv(1024).decode('utf-8')
        print(data)
    sock.close()

if __name__ == '__main__':
    echo_client(('192.168.0.63',50011))
