from DataStructures.Map import map_functions as mp
from DataStructures.Map import map_entry as me
from DataStructures.List import array_list as al
import random
import math

def new_map(num_elements,load_factor,prime):
    if prime == None:
        prime = 109345121
    if load_factor <= 0:
        return ("ValueError. load_factor debe ser > 0")
    
    capacity = int(math.ceil(num_elements/load_factor))
    capacity = mp.next_prime(capacity)
    
    scale = random.randint(1,prime-1)
    shift = random.randint(0,prime-1) 
    table = al.new_list()
    for i in range(capacity):
        al.add_last(table,{"key":None,"value":None})
        
    map = {
        "prime": prime,
        "capacity": capacity,
        "scale": scale,
        "shift": shift,
        "table": table,
        "current_factor": 0,
        "limit_factor": load_factor,
        "size": 0,
    }
    return map

def is_available(table, pos):

    entry = al.get_element(table, pos)
    if me.get_key(entry) is None or me.get_key(entry) == "__EMPTY__":
        return True
    return False

def default_compare(key, entry):

    if key == me.get_key(entry):
        return 0
    elif key > me.get_key(entry):
        return 1
    return -1

def find_slot(my_map, key, hash_value):
    first_avail = None
    found = False
    ocupied = False
    while not found:
        if is_available(my_map["table"], hash_value):
            if first_avail is None:
                first_avail = hash_value
            entry = al.get_element(my_map["table"], hash_value)
            if me.get_key(entry) is None:
                found = True
        elif default_compare(key, al.get_element(my_map["table"], hash_value)) == 0:
            first_avail = hash_value
            found = True
            ocupied = True
    hash_value = (hash_value + 1) % my_map["capacity"]
    return ocupied, first_avail

def rehash(my_map):
    capacity = (my_map["capacity"] * 2)
    capacity = int(math.ceil(capacity))
    capacity = mp.next_prime(capacity)
    
    table = al.new_list()
    for i in range(capacity):
        al.add_last(table,{"key":None,"value":None})
        
    old_table = my_map["table"]
    old_table = old_table["elements"]
    my_map["capacity"] = capacity
    my_map["size"] = 0
    my_map["current_factor"] = 0
    my_map["table"] = table
    for i in old_table:
        if i["key"] is not None and i["value"] is not None:
            put(my_map,i["key"],i["value"])
    return my_map

def put(my_map,key,value):
    hash = mp.hash_value(my_map,key)
    position = find_slot(my_map,key,hash)
    if position[0] == True:
        my_map["table"]["elements"][position[1]]["value"] = value
    else:
        my_map["table"]["elements"][position[1]]= {"key": key, "value": value}
        my_map["size"] +=1
        my_map["current_factor"] = my_map["size"]/my_map["capacity"]
        if my_map["current_factor"] > my_map["limit_factor"]:
            rehash(my_map)
    
    return my_map

def contains(my_map, key):
    hash_index = mp.hash_value(my_map, key)
    slot = find_slot(my_map, key, hash_index)
    
    if slot["key"] is None:
        return False
    if slot["key"] == key:
        return True
    else:
        return False
    
def get(my_map, key):
    hash_index = mp.hash_value(my_map, key)
    slot = find_slot(my_map, key, hash_index)
    
    if slot["key"] is None:
        return None
    if slot["key"] == key:
        return slot["value"]
    else:
        return None


    