import socket
import select
import errno
import sys
import threading

HEAEDR_LENGTH = 10
IP = "127.0.0.1"
PORT = 2222


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((IP, PORT))

nickname = input("Choose nickname: ")
def receive():
    while True:
        try:
            message = client.recv(1024).decode('ascii')
            if message == 'NICK':
                client.send(nickname.encode('ascii'))
            else:
                print(message)
        except:
            print("An error occurred...")
            client.close()
            break

def write():
    while True:
        message = f'{nickname}: {input("")}'
        try:
            client.send(message.encode('ascii'))
        except Exception as e:
            print('Exception from client: ' + str(e))


receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()

