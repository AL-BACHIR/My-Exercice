import socket 
host = input("entrez un host a scanner : ")
start_port = 1
end_port = 1024

def scan_port(host_target, target_port):
    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = client.connect_ex((host, target_port))
        client.settimeout(4)
        if result == 0:
            print(f"le port {target_port} est ouvert")
        else:
            print(f"le port {target_port} est fermé")
            client.close()
    except:
        print(f"le port {target_port} est fermé")
for port in range(start_port, end_port +1):
    scan_port(host, port)
