""" key format : """
# MAC+IP+num_cpu+CPU_IDs+
# another script for configuration is necessary to config the host pc 

import platform, os 
import dmidecode
import subprocess
__verbose = True

def chassis_f():
    if __verbose:

        print("Chassis Function calling... ")
    l = ["Manufacturer", "Serial", "SKU"]
    data = list()
    for i in range(3):
        job = subprocess.Popen(["sudo", "dmidecode", "-t", "3","|grep", l[i]], stdout=subprocess.PIPE)
        out, err = job.communicate()
        if err == None:
            data.append(out)
    return data
def system_info():
    if __verbose:
        print("System information ")
    base = "sudo dmidecode -t 1 | grep"
    serial = "Serial"
    uuid = "UUID"
    sku = "SKU"
    base = list(base.split(" "))
    return base, serial, uuid, sku
def base_board_f():
    if __verbose:
        print("base board f")
    base = "sudo dmidecode -t 2 |grep"
    pro = "Product"
    v = "Version"
    serial = "Serial"
    base = list(base.split(" "))
    return base, pro, v, serial
""" TO BE COMPLETED """    
def processor_f():
    if __verbose:
        print("proc f")
    base = "sudo dmidecode -t 4 | grep"
    core ="Core"
    return base, core
def sys_slots():
    cmd_dmi = "sudo dmidecode -t 9"#Bus address
    os.system(cmd_dmi)

def OEM_strings():
    cmd_dmi = "sudo dmidecode -t 11"# Identify?
    os.system(cmd_dmi)

"""
cmd_dmi = "sudo  dmidecode -t " + sys.argv[1]
os.system(cmd_dmi)
"""

#cmd_dmi = "sudo  dmidecode -t 4|grep ID | sed 's/.*ID://;s/ //g'"
#cmd_if = "ifconfig |grep eth1| awk '{print $NF}' |sed 's/://g'"
#print(dmidecode.parse())
"""os.system(cmd_dmi)
print("cmddmi finished")
os.system(cmd_if)
print("cmdif finished")
"""
#print(dmidecode.get_by_type(1))
#print(platform.system())
#print(platform.processor())

def all_f():
    print(chassis_f())
    #system_info()
    #base_board_f()
    #processor_f()

print(type(dmidecode.get_by_type(3)[0]))
#all_f()
