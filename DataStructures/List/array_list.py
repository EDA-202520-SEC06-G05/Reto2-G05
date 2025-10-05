#Forma de importarlo en otro archivo 
#from DataStructures.List import array_list as al

def new_list():
    newlist = {
        "elements": [],
        "size": 0
    }
    return newlist

def add_first(my_list, element):
    my_list["elements"].insert(0,element)
    my_list["size"] +=1
    return my_list 

def add_last(my_list, element):
    my_list["elements"][my_list["size"]:] = [element]
    my_list["size"] +=1
    return my_list

def get_element(my_list,index):
    if index < 0 or index >= my_list["size"]:
        return "IndexError: list index out of range"
    else:
        return my_list["elements"][index]

def is_present(my_list, element, cmp_function):
    size = my_list["size"]
    if size > 0:
        keyexist = False
        for keypos in range(0, size):
            info = my_list["elements"][keypos]
            if cmp_function(element, info) == 0:
                keyexist = True
                break
        if keyexist:
            return keypos
    return -1

def size(my_list):
    return my_list["size"]

def first_element(my_list):
    if my_list["elements"] != None:
        first_element = my_list["elements"][0]
    else:
        first_element = None
    return first_element

def is_empty(my_list):
    if my_list["size"] == 0:
        return True
    else:
        return False

def last_element(my_list):
    if my_list["size"] > 0:
        return my_list["elements"][my_list["size"] - 1]
    else:
        return "Index Error: list index out of range"
    
def delete_element(my_list, pos):
    if pos < 0 or pos >= my_list["size"]:
        return "Index Error: list index out of range"
    else:
        new_list = (my_list["elements"][:pos] + my_list["elements"][pos + 1:])
        return {
            "elements": new_list,
            "size": my_list["size"] - 1
        }

def remove_first(my_list):
    if my_list["size"] == 0:
        return "Index Error: list index out of range"
    else:
        deleted = my_list["elements"][0]
        my_list["elements"] = my_list["elements"][1:]
        my_list["size"] -= 1
        return deleted
    
def remove_last(my_list):
    if my_list["size"] == 0:
        return "Index Error: list index out of range"
    else:
        new_list = my_list["elements"][: my_list["size"] - 1]
        return {
            "elements":new_list,
            "size": my_list["size"] - 1
        }
    
def insert_element(my_list, element, pos):
    new_list = (my_list["elements"][:pos] + [element] + my_list["elements"][pos:])
    return {
        "elements": new_list,
        "size": my_list["size"] + 1 
    }

def change_info(my_list, pos, new_info):
    if pos < 0 or pos >= my_list["size"]:
        return "Index Error: list index out of range"
    else:
        my_list["elements"][pos] = new_info
        return my_list

def exchange(my_list, pos_1, pos_2):
    if (pos_1 < 0 or pos_1 >= my_list["size"]) and (pos_2 < 0 or pos_2 >= my_list["size"]):
        return "Index Error: list index out of range"
    else:
        temp = my_list["elements"][pos_1]
        my_list["elements"][pos_1] = my_list["elements"][pos_2]
        my_list["elements"][pos_2] = temp
        return my_list

def sub_list(my_list, pos_i, num_elements):
    if pos_i < 0 or pos_i >= my_list["size"]:
        return "IndexError: list index out of range"
    else:
        new_sublist = {
            "elements" : my_list["elements"][pos_i : pos_i + num_elements],
            "size" : num_elements
            }
        return new_sublist