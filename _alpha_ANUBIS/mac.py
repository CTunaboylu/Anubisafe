import netifaces
import sys
from bitstring import BitArray
#bitstring notes: c.bin -> str  
#mac_hex -> bytes 
verbose = True
"""Check OS 
if 'darwin' in sys.platform:
    print("Macbook detected.")
    #arg = 'fw0'
else:"""

if _verbose:
    print(sys.platform)
    interfaces = netifaces.interfaces()
    #['lo', 'eth0', 'tun2']
    print(interfaces)
    l = list()
    addrs = list()
    for i in interfaces:
        l.append(i)
        addrs.append(netifaces.ifaddresses(str(i))[netifaces.AF_LINK])
        print(addrs[-1])

MAC_ADDR = addrs[-1]
MAC_ADDR = MAC_ADDR[0]['addr']

print('MAC: ',MAC_ADDR)
mac_hex = MAC_ADDR.encode('utf-8')
c = BitArray(bytes=mac_hex)

print(c.bin)
#b"abcde".decode("utf-8") 

#Mutate the MAC address according to the mutation coefficient 
#mutation anatomy: 
#def crossover(genome:bytes, mutation:int)->bytes:
 

