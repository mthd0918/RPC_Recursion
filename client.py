import socket
import sys

sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)

server_address = '/tmp/socket_file'
print('connecting to {}'.format(server_address))

try:
    sock.connect(server_address)
except socket.error as err:
    print(err)
    sys.exit(1)

try:
    message = b'Sending a message to the server side'
    sock.sendall(message)
    sock.settimeout(2)
    
    try:
        while True:
            data = str(sock.recv(32))
        
            if data:
                print('server response: ' + data)
            else:
                break
    except(TimeoutError):
        print('Socket timeout, ending litening for server message')
finally:
    print('slosing socket')
    sock.close()