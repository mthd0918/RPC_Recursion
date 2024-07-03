import socket
import sys
import math

def floor(x):
    return math.floor(x)

def nroot(x, n):
    return math.pow(x, 1/n)

def reverse(s):
    return s[::-1]

def validAnagram(str1, str2):
    str1 = ''.join(str1.lower().split())
    str2 = ''.join(str1.lower().split())

    if(len(str1) != len(str2)):
        return False
    
    return sorted(str1) == sorted(str2)

def sort(strArr):
    return sorted(strArr)

def main():

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

if __name__ == "__main__":
    main()