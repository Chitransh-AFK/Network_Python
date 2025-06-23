import socket
import threading
from concurrent.futures import ThreadPoolExecutor

target=input("Enter the targer IP ADDRESS: ")

start_port=1
end_port=1024

threads=[] #list of threads
print(f"\n Scanning {target} from port {start_port} to {end_port}")

#this command block gives the port name by port 
def get_service(port):
    try :
        return socket.getservbyport(port)
    except:
        return 'unknown'

def scan_port(port):
    try:
        s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        
        result=s.connect_ex((target,port))#give the error 0 if port is open (ex stands for exception)
        s.settimeout(0.5)
        if result==0:
            service=get_service(port)
            print(f"PORT {port} ({service}) is OPEN")
        s.close()
    except:
        pass
with ThreadPoolExecutor(max_workers=500) as executor:#max thread at a time 500 limits the number of thread
    for port in range(start_port,end_port+1): #starts a new thread for every port
        t=threading.Thread(target=scan_port,args=(port,))#arg=(port,) start the scan_port
        threads.append(t)#appending the thread in threads list
        t.start()

for t in threads:
    t.join() #this command tells every finish thread to wait until other threads are done scanning before printing complete

print(f"\n Scan Complete")