import socket
import os
import math
import json
from typing import Callable, Dict, Any

def floor(x: float) -> int:
    return math.floor(x)

def nroot(x: int, n: int) -> float:
    return math.pow(x, 1/n)

def reverse(s: str) -> str:
    return s[::-1]

def validAnagram(str1: str, str2: str) -> bool:
    str1 = ''.join(str1.lower().split())
    str2 = ''.join(str1.lower().split())

    if(len(str1) != len(str2)):
        return False
    
    return sorted(str1) == sorted(str2)

def sort(strArr: list[str]) -> list[str]:
    return sorted(strArr)

function_map = {
    "floor": floor,
    "nroot": nroot,
    "reverse": reverse,
    "validAnagram": validAnagram,
    "sort": sort
}

def execute_method(request):
        result = function_map[request['method']](*request['params'])
        return result

def check_result_type(result):
    if isinstance(result, float):
        return 'float'
    elif isinstance(result, bool):
        return 'bool'
    elif isinstance(result, str):
        return 'str'
    elif isinstance(result, list):
        return 'list'
    else:
        return 'something'
    

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
            print('connection from\n', client_address)
            while True:
                # データを受け取り、バイナリから文字列へデコード、jsonファイルとしてロード
                data = connection.recv(1024)
                data_str = data.decode('utf-8')
                request = json.loads(data_str)

                result = function_map[request['method']](*request['params'])

                result_map = {
                    'result': str(result),
                    'result_Type': check_result_type(result),
                    'id': request['id']
                }

                results = json.dumps(result_map)
                print(results)
                connection.sendall(results.encode())

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