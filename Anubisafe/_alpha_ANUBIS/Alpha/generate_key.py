""" key format : """
# MAC+IP+num_cpu+CPU_IDs+
# another script for configuration is necessary to config the host pc 

import platform, subprocess, os 
import dmidecode
import sys, subprocess
_debug = True

def chassis_f():
    if _debug:
        print("Chassis ")
    base = "sudo dmidecode -t 3 | grep"
    manu = "Manufacturer"
    #manu = list(cmd_dmi.split(" "))
    serial = "Serial" 
    sku = "SKU" 
    base = list(base.split(" "))
    return base, manu, serial, sku

def system_info():
    if _debug:
        print("System information ")
    base = "sudo dmidecode -t 1 | grep"
    serial = "Serial"
    uuid = "UUID"
    sku = "SKU"
    base = list(base.split(" "))
    return base, serial, uuid, sku
def base_board_f():
    if _debug:
        print("base board f")
    base = "sudo dmidecode -t 2 | grep"
    pro = "Product"
    v = "Version"
    serial = "Serial"
    base = list(base.split(" "))
    return base, pro, v, serial
""" TO BE COMPLETED """    
def processor_f():
    if _debug:
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
    an = chassis_f()
    chas_out = list()
    for o in an:
        chassis = subprocess.Popen(an[1], stdout=subprocess.PIPE)
        out, chas_err = chassis.communicate()
    if chas_err == None:
        print("Chass_err ", chas_err)
        print("Chassis\n", chas_out)

    system_info()
    base_board_f()
    processor_f()


all_f()
