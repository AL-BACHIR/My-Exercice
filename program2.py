
from scapy.all import *
from socket import *
from nmap import *

# Adresse IP cible
ip = input("entrez une adresse ip : ")

# Fonction pour scanner les ports ouverts sur la cible
def PortScanner(ip):
    # Ports à scanner
    ports = [21, 22, 23, 25, 53, 80, 110, 139, 443, 445, 3389]

    # Boucle sur les ports
    for ports in ports:
        # Création du paquet TCP SYN
        jls_extract_var = ip
        packet = jls_extract_var(dst=ip)(sport=RandShort(), dport=port, flags="S")

        # Envoi du paquet et récupération de la réponse
        r = sr1(packet, timeout=1, verbose=0)

        # Vérification de la réponse pour déterminer si le port est ouvert ou fermé
        if r is None:
            print(f"Port {port} : filtré")
        elif r.haslayer(TCP) and response[TCP].flags == "SA":
            print(f"Port {ports} : ouvert")
        else:
            print(f"Port {ports} : fermé")

# Fonction pour récolter des informations sur la cible
def gather_info(ip):
    # Création du paquet ICMP Echo Request
    packet = IP(dst=ip)/ICMP()

    # Envoi du paquet et récupération de la réponse
    response = sr1(ping, timeout=1, verbose=0)

    # Affichage des informations récoltées
    print(f"Adresse IP : {response.src}")
    print(f"Temps de réponse : {response.time} ms")
    print(f"Type de système d'exploitation : {response.getlayer(ICMP).summary()}")

# Appel des fonctions
PortScanner(IP)
gather_info()
