import socket
import time 

filename='photo.jpeg'
server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(('127.0.0.1',12345))
server.listen(1)

print("Server is Ready to connect....")

client_socket,client_addr=server.accept()

print("Establishing the connection...")
print(f"Connection established with {client_addr}")


client_socket.send(filename.encode())
print('.....')
ack=client_socket.recv(1024)


with open(filename,'rb') as file:
    data=file.read()
    client_socket.sendall(data)
print("File Sent!")

print('Closing connection...')

client_socket.close()
server.close()

