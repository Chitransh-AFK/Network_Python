import socket
import threading
import os

host='192.168.31.98'
port=12345
client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect((host,port))

def receive_initial():
    print("To send File type /file in the beginning and enter the filename with extension")
    data=client.recv(1024).decode('utf-8')
    if data=='USERNAME':
        username=input("Enter your username: ")
        client.send(username.encode('utf-8'))

def receive_handler():
    while True:
        try:
            header=client.recv(1024).decode('utf-8')
            if not header:
                break
            if header.startswith('FILE:'):
                _,filename,filesize=header.split(':')
                filesize=int(filesize)
                print(f'\n[Reciving file] {filename} ({filesize} bytes)')
                with open('received'+filename,'wb' ) as f:
                    received=0
                    while received<filesize:
                        chunk=client.recv(min(4096,filesize-received))
                        if not chunk :
                            break
                        f.write(chunk)
                        received+=len(chunk)
                print(f'[✓] File {filename} received successfully \n')
            else:
                print(header)
        except Exception as e:
            print(f'[ERROR] {e}')
            break
    
def send_handler():
    while True:
        msg=input()

        if msg.startswith("/file"):
            filename=msg.split(" ",1)[1]
            if os.path.exists(filename):
                filesize=os.path.getsize(filename)
                client.send(f"FILE:{filename}:{filesize}".encode('utf-8'))
                with open(filename,'rb') as f:
                    while True:
                        chunk=f.read(4096)
                        if not chunk:
                            break
                        client.sendall(chunk)
                print(f"[✓] File {filename} sent")
            else:
                print("[!] File not found")

        else:
            client.send(f'MSG:{msg}'.encode('utf-8'))

receive_initial()

receive_thread=threading.Thread(target=receive_handler)
receive_thread.start()

send_thread=threading.Thread(target=send_handler)
send_thread.start()