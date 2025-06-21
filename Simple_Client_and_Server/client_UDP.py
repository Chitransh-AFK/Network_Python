import socket #importing the module

UDP_IP= input("Enter the IP: ")
UDP_PORT=12345
mssg="Hello, UDP Server!"

client=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)#Main SOCK_DGRAM=UDP connection 

client.sendto(mssg.encode(),(UDP_IP,UDP_PORT)) #sends the mssg to the server on the port and ip 

print("Message sent to server")


