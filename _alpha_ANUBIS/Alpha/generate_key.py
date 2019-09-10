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
    cmd_dmi = "sudo dmidecode -t 3 | grep Manufacturer"
    manu = list(cmd_dmi.split(" "))
    os.system(cmd_dmi)
    cmd_dmi = "sudo dmidecode -t 3 | grep Serial" 
    serial = list(cmd_dmi.split(" "))
    os.system(cmd_dmi)
    cmd_dmi = "sudo dmidecode -t 3 | grep SKU" 
    sku = list(cmd_dmi.split(" "))
    os.system(cmd_dmi)
    return manu

def system_info():
    if _debug:
        print("System information ")
    cmd_dmi = "sudo dmidecode -t 1 | grep Serial"
    serial = list(cmd_dmi.split(" "))
    print(serial)
    os.system(cmd_dmi)
    cmd_dmi = "sudo dmidecode -t 1 | grep UUID"
    os.system(cmd_dmi)
    cmd_dmi = "sudo dmidecode -t 1 | grep SKU"
    os.system(cmd_dmi)
    return serial
def base_board_f():
    if _debug:
        print("base board f")
    cmd_dmi = "sudo dmidecode -t 2 | grep Product"
    os.system(cmd_dmi)
    cmd_dmi = "sudo dmidecode -t 2 | grep Version"
    os.system(cmd_dmi)
    cmd_dmi = "sudo dmidecode -t 2 | grep Serial"
    os.system(cmd_dmi)

def processor_f():
    if _debug:
        print("proc f")
    cmd_dmi = "sudo dmidecode -t 4 | grep Core"
    os.system(cmd_dmi)
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
    chassis = subprocess.Popen(chassis_f(), stdout=subprocess.PIPE)
    chas_out, chas_err = chassis.communicate()
    if chas_err == None:
        print("Chass_err ", chas_err)
        print("Chassis\n", chas_out)

    #chassis_f()
    system_info()
    base_board_f()
    processor_f()


all_f()
