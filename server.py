import socket
import os
import math
import json

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

    try:
        os.unlink(server_address)
    except FileNotFoundError:
        pass
    print('Starting up on {}'.format(server_address))
    sock.bind(server_address)

    sock.listen(1)

    while True:
        connection, client_address = sock.accept()
        try:
            print('connection from', client_address)
            while True:
                # データを受け取り、バイナリから文字列へデコード
                data = connection.recv(1024)
                data_str = data.decode('utf-8')

                requestData = json.loads(data_str)
                print('Method:', requestData.get('method', 'No method specified'))
                print('Params:', requestData.get('params', 'No params specified'))
                print('ID:', requestData.get('id', 'No ID specified'))

                if data:
                    response = 'Processing ' + data_str
                    connection.sendall(response.encode())
                else:
                    print('no data from', client_address)
                    break
        finally:
            print("Closing current connection")
            connection.close()

if __name__ == "__main__":
    main()