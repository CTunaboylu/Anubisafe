""" key format : """
# MAC+IP+num_cpu+CPU_IDs+
# another script for configuration is necessary to config the host pc 

import sys, os
import dmidecode
import hashlib
__verbose = False
__debug = True
__comparison = True
__fname = 'key_elements_'
def write(dict_list):
    try:
        with open(__fname +'.txt', 'a') as the_file:
            [the_file.write(f"{key}:{value}\n") for key,value in dict_list.items()]
    except IOError:
        with open(__fname + '.txt', 'w') as the_file:
            [the_file.write(f"{key}:{value}\n") for key,value in dict_list.items()]
def compare_files():
    txts = list()
    for f in os.listdir("./"):
        if f.endswith(".txt") and 'key' in f:
            txts.append(f)
            if __debug:
                print(os.path.join("./", f))
    same = None
    out = open('analysis.txt', 'w')
    with open( txts[0], 'r') as file_one:
        with open( txts[1], 'r') as file_two:
            same = set(file_one).intersection(file_two)
            same.discard('\n')
            for line in same:
                out.write(line)

            
def type_1_system_information():
    if __verbose:
        print("Gathering system information... ")
    
    # potentially unique or can be different for some reason
    l = ["Serial Number", "UUID", "SKU Number"]
    data = list()
    __type = 1
    if __verbose:
        print(dmidecode.get_by_type(__type)[0])
    for elm in l:
        piece = dmidecode.get_by_type(__type)[0][elm]
        if __verbose:
            print(piece)    
        data.append(piece)
    write(dmidecode.get_by_type(__type)[0])
    return data


def type_2_base_board_information():
    if __verbose:
        print("Gathering base board information...")
    
    # potentially unique or can be different for some reason
    l = ["Serial Number", "Product Name", "Version"]
    data = list()
    __type = 2
    if __verbose:
        print(dmidecode.get_by_type(__type)[0])
    for elm in l:
        piece = dmidecode.get_by_type(__type)[0][elm]
        if __verbose:
            print(piece)    
        data.append(piece)
    write(dmidecode.get_by_type(__type)[0])
    return data

def type_3_chassis_information():
    if __verbose:
        print("Gathering chassis information... ")
    # potentially unique or can be different for some reason
    l = ["Manufacturer", "Serial Number", "Number Of Power Cords", "SKU Number"]
    data = list()
    __type = 3
    if __verbose:
        print(dmidecode.get_by_type(__type)[0])
    for elm in l:
        piece = dmidecode.get_by_type(__type)[0][elm]
        if __verbose:
            print(piece)    
        data.append(piece)
    write(dmidecode.get_by_type(__type)[0])
    return data

""" TO BE COMPLETED """    
def type_4_processor_information():
    if __verbose:
        print("Gathering processor information")
    core ="Core"
    # potentially unique or can be different for some reason
    l = ["Signature", "Upgrade", "Version", "External Clock", "Core Enabled", "Thread Count", "ID"]
    data = list()
    __type = 4
    if __verbose:
        print(dmidecode.get_by_type(__type)[0])
    for elm in l:
        piece = dmidecode.get_by_type(__type)[0][elm]
        if __verbose:
            print(piece)    
        data.append(piece)

    write(dmidecode.get_by_type(__type)[0])
    return data

def type_9_system_slots():
    if __verbose:
        print("Gathering sytem slots information...")
    l = ["Bus Address"]
    data = list()
    __type = 9
    if __verbose:
        print(dmidecode.get_by_type(__type)[0])
    for elm in l:
        piece = dmidecode.get_by_type(__type)[0][elm]
        if __verbose:
            print(piece)    
        data.append(piece)
    
    write(dmidecode.get_by_type(__type)[0])
    return data

def type_11_OEM_strings():
    if __verbose:
        print("Gathering OEM strings...")
    l = ["Bus Address"]
    data = list()
    __type = 11
    count = len(dmidecode.get_by_type(__type)[0])-2 # 8 can be used for simplicity  
    if __verbose:
        print(dmidecode.get_by_type(__type)[0])
        print("Count: ", count)
    for elm in range(count):
        str_x = f"String {elm}"
        if str_x in dmidecode.get_by_type(__type)[0]:
            piece = dmidecode.get_by_type(__type)[0][str_x]
            if __verbose:
                print(piece)    
            data.append(piece)
    write(dmidecode.get_by_type(__type)[0])
    return data
def type_15_system_log():
    if __verbose:
        print("Gathering system log information...")
    __type = 15
    if __verbose:
        print(dmidecode.get_by_type(__type)[0])
    clean = list()
    out = dmidecode.get_by_type(__type)[0] 
    for k  in out:
        clean.append(out[k])
    
    write(out)
    return clean 

def generate_the_unique_key():
    type_1_info = type_1_system_information()
    type_2_info = type_2_base_board_information()
    type_3_info = type_3_chassis_information()
    type_4_info = type_4_processor_information()
    type_9_info = type_9_system_slots()
    type_11_info = type_11_OEM_strings()
    type_15_info = type_15_system_log()

    hasher = hashlib.sha256()
    [hasher.update(str(i).encode()) for i in type_1_info]
    [hasher.update(str(i).encode()) for i in type_2_info]
    [hasher.update(str(i).encode()) for i in type_3_info]
    [hasher.update(str(i).encode()) for i in type_4_info]
    [hasher.update(str(i).encode()) for i in type_9_info]
    [hasher.update(str(i).encode()) for i in type_11_info]
    [hasher.update(str(i).encode()) for i in type_15_info]
   
    signature = hasher.hexdigest()
    if __debug:
        print("Signature: ", signature)
        print("Block size: ", hasher.block_size)

def check_for_new():
    args=len(sys.argv)
    for i in range(args):
        if i == 0:
            continue
        print(dmidecode.get_by_type(int(sys.argv[i])))
os.system('pip install -r requirements.txt')
n = sys.argv[-1]
ex_file = __fname
__fname += n
generate_the_unique_key()
__fname = ex_file + sys.argv[-2]
generate_the_unique_key()
compare_files()
