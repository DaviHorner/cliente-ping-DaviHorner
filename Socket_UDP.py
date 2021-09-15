# Importação das bibliotecas usadas
import socket
import time 

# inicialização das variaveis
n = 50
rtt = []
i = 0
perc = 0.0
final = 0
cont = 0
delta = 0.0
sum_rtt = 0.0

# Socket UDP
skt = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while i < n:
    skt.settimeout(0.25)
    i = i + 1
    try:
        inicial = time.time()
        skt.sendto(b'Oi\n',("52.65.104.154",6000))
        print(f"Recebeu: {skt.recv(1024).decode()}")
        skt.settimeout(None)
        final = time.time()
        delta = ( final - inicial )
        rtt.append(delta)
        
    except socket.timeout:
        cont = cont + 1 
        print("Falhou\n")
    time.sleep(1)

# Soma de todos os rtt
sum_rtt = sum(rtt)
# Calculo da media dos rtt
rtt_medio = (sum_rtt / (n - cont)) * 1000
# Calculo da porcentagem
perc = (100 * cont)/n

# Impressões
print("RTT médio:", '%.2f'%rtt_medio)
print("Porcentagem de falhas", perc)




