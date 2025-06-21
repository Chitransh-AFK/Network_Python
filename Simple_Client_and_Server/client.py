import socket #importing the socket module


#Making the client socket 
client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#AF_INET= signifies client to use IPv4 family Ex- 192.168.31.1 
#SOCK_STREAM= signifies client to use TCP protocol to connect


ip_connect=input("Enter the Ip address: ") #entering the server ip addr (just for fun :>) 

#IMPORTANT:- If you are beginner in networking use enter 127.0.0.1 (Explaination in server.py)

client.connect((ip_connect,12345))

mssg=input("Enter Your Message: ")

client.send(f"{mssg}".encode())#client sends the mssg to the server in binary encoded form
response=client.recv(1024).decode()
#client listining to server for the response and only accept the info not more than 1024 bytes and decode it to string and store it to response variable
print(f"Server Says: {response}")

print("closing the connection...")

client.close()#closing the client cnnection