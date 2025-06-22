import socket 
import threading

host='0.0.0.0'
port=12345

#setup server socket

server_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_socket.bind((host,port))
server_socket.listen()


clients=[]
usernames=[]
print(f"[+] Waiting for connection on {host}:{port}....")

def handler_client(client):
    try:
        client.send("USERNAME".encode('utf-8'))
        username=client.recv(1024).decode('utf-8')
        usernames.append(username)
        clients.append(client)
        print(f"[+] {username} connected.")

        while True:
            header= client.recv(1024).decode('utf-8')
            if not header:
                break
            if header.startswith("MSG:"):
                message=header[4:]
                broadcast(f"{username}:{message}",client)
            elif header.startswith("FILE:"):
                _,filename,filesize=header.split(":")
                filesize =int(filesize)

                file_data=b''
                while len(file_data)<filesize:
                    chunck=client.recv(min(4096,filesize-len(file_data)))
                    if not chunck :
                        break
                    file_data+=chunck
                print(f'[FILE] {username} sent file: {filename} ({filesize}bytes)')

                #foreward file to other clients
                for c in clients:
                    if c !=client:
                        try:
                            c.send(f"FILE: {filename}:{filesize}".encode('utf-8'))
                            c.sendall(file_data)
                        except:
                            print("[!] Error in sending the file")
                            client.remove(c)
    except Exception as e:
        print(f"[!] Error :{e}")
        if client in clients:
            index=clients.index(client)
            username=usernames[index]
            clients.remove(client)
            usernames.remove(username)
            client.close()

def broadcast(message,sender_client):
    for client in clients:
        if client!=sender_client:
            try:
                client.send(message.encode('utf-8'))
            except:
                print('[!] Error occured in sending mssg')
                client.close()
                clients.remove(client)


while True:
    client_socket,client_address=server_socket.accept()
    print(f"[✓] Connected to {client_address}")
    thread=threading.Thread(target=handler_client,args=(client_socket,))
    thread.start()