import json
import socket

print('Escreva um dos comandos:')
print('1. SETUP \'nome do usuário(sem espaço)\' \'tempo led vermelho\' \'tempo led amarelo\' \'tempo led verde\'')
print('2. GETDATA \'tipo de log a ser recolhido (CARS ou SETUP)\'')
texts = input().split(' ')
command = texts[0]
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('127.0.0.1', 2045))
if command == 'SETUP':
    username = texts[1]
    colors = (int(texts[2]), int(texts[3]), int(texts[4]))
    struct = {
        'command': command,
        'username': username,
        'red_time': colors[0],
        'yellow_time': colors[1],
        'green_time': colors[2]
    }
    data = bytes(json.dumps(struct), 'utf-8')
    mysock.sendall(data)
elif command == 'GETDATA':
    log_type = texts[1]
    struct = {
        'command': command,
        'log_type': log_type
    }
    data = bytes(json.dumps(struct), 'utf-8')
    mysock.sendall(data)
    data = mysock.recv(4096)
    decoded_data = data.decode('utf-8')
    struct = json.loads(decoded_data)
    print('Dados recolhidos:')
    print(struct['log'])
