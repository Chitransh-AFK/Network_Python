import os 
import platform 
import socket
from concurrent.futures import ThreadPoolExecutor

#Ex=> 192.168.31.166, So 192.168.31 is the network part and 166 is host part
#RUN THE PROGRAM 2 TO 3 Time for better results

def get_local_ip_prefix():
    hostname=socket.gethostname()
    local_ip=socket.gethostbyname(hostname)
    return '.'.join(local_ip.split('.')[:3])#make the full netwok it after 192.162. '.'


def ping_host(ip):
    #Decides whether to use -n (Windows) or -c (Linux/macOS) in the ping command.
    parameter='-n' if platform.system().lower()=='windows' else '-c'
    result=os.system(f'ping {parameter} 1 -w 500 {ip} >nul 2>&1') #>nul = hide standard output (stdout) 2>&1 = hide error messages (stderr) too
    #-w timeout after 500ms
    if result==0:
        print(f"🟢 {ip} is alive")
        return ip
    return None
def ping_sweep(base_ip):
    print(f"🔍 Starting LAN sweep on {base_ip}.1 to {base_ip}.254...\n")
    active_host=[]#make list of active host

    with ThreadPoolExecutor(max_workers=500) as executor:
        results=executor.map(ping_host,[f"{base_ip}.{i}" for i in range(1,255)])#map all the active host network and append only the active host in the active_host list

    for ip in results:
        if ip:
            active_host.append(ip)
    
    print(f"\n Found {len(active_host)} active Device(s)")
    return active_host

if __name__=='__main__':
    prefix=get_local_ip_prefix()#get the network addr the 3 rd digit
    active_devices=ping_sweep(prefix)#pass the 3 rd digit and make all the possible client in a network and try to ping them

