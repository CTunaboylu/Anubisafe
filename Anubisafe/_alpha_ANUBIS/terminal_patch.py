import sys

#check if modules necessary are installed or not OR requirements.txt

platform = sys.platform
if 'darwin' in platform:
    print('Macbook detected.')
    arg = 'fw0' # MAC address interface

else:
    print(platform)
    interfaces = netifaces.interfaces()
    print(interfaces)
    l = list()
    for i in interfaces:
        l.append()
        print(l[-1])

debug = True
if debug:
    print(str(sys.argv))
    len = len(sys.argv)
