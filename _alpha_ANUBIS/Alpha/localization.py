import netifaces
import sys
from bitstring import BitArray
#bitstring notes: c.bin -> str  
#mac_hex -> bytes

_verbose = True
_sterile = '00:00:00:00:00:00'
"""
eno1 is the onboard Ethernet (wired) adapter: this should be on Linux machine.
This is a way of representing the Ethernet names. If machine has already eth1 in its config file for the second adapter it will use eno1 rather than using eth2.

They both are same. Its just a name of config file. You can also change the name eno1 to eth2 by doing a simple Google search.


"""
def localize():
    # possible interfaces : ['lo', 'eth0', 'tun2'], there may also be 'en0'
    if _verbose:
        print(sys.platform)
    interfaces = netifaces.interfaces()
    addrs = list()
    l = list()
    for i in interfaces:
        l.append(i)
        addrs.append(netifaces.ifaddresses(str(i))[netifaces.AF_LINK])
        if _verbose:
            print(interfaces)
            print(addrs[-1])
    return l, addrs

def clean(l:list, addrs:list) -> dict:
    print("List l :", l)
    print("List addrs:", addrs)
    #Checking the all 00 MAC binary
    length = len(addrs)
    for i in range (length):
        b_format = addrs[i]
        b_arg = b_format[0]['addr']
        if b_arg in _sterile:
            print(f"{b_arg} is sterile")
            del addrs[i][0]
            addrs[i].pop()
            print(" New addrs: ",addrs)
        bits = BitArray(bytes=b_arg.encode('utf-8'))
        print(f"Binary for {b_arg}:{type(b_arg)} is {bits}; {type(bits)}")
    
    pass

l, addr = localize()
clean(l, addr)
print("Cleaned : ", addr, len(addr))


"""
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
 
"""
