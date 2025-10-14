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

def default_sort_criteria(element_1, element_2):
    return element_1 <= element_2

def selection_sort(my_list, sort_crit):
    elements = my_list["elements"]
    size = my_list["size"]

    for i in range(size - 1):
        min_idx = i
        for j in range(i + 1, size):
            if not sort_crit(elements[min_idx], elements[j]):
                min_idx = j
        elements[i], elements[min_idx] = elements[min_idx], elements[i]

    return my_list

def insertion_sort(my_list, sort_crit):
    
    elements = my_list["elements"]
    
    for i in range(1, my_list["size"]):
        key = elements[i]
        j = i - 1
        while j >= 0 and not sort_crit(elements[j],key):
            elements[j+1] = elements[j]
            j -= 1
        elements[j+1] = key
    return my_list    
    
    
def shell_sort(my_list, sort_crit):
 
    gap = my_list["size"] // 2
    elements = my_list["elements"]
    
    if (my_list["elements"] == None) or (my_list["size"] == 1):
        return my_list
    else:
        while gap > 0:
            for i in range(gap, my_list["size"]):
                tempo = elements[i]
                j = i
                while j >= gap and not sort_crit(elements[j - gap], tempo):
                    elements[j] = elements[j - gap]
                    j -= gap
                elements[j] = tempo
            gap //= 2
            
        return my_list
    
def merge_sort(my_list, sort_crit):
    if my_list["size"] <= 1:
        return my_list
    else:
        mid = my_list["size"] // 2
        left = new_list()
        right = new_list()
        
        for i in range(mid):
            add_last(left, my_list["elements"][i])
        for i in range(mid, my_list["size"]):
            add_last(right, my_list["elements"][i])
        
        merge_sort(left, sort_crit)
        merge_sort(right, sort_crit)
        
        i = 0
        j = 0
        
        temp = new_list()
        while i < left["size"] and j < right["size"]:
            if sort_crit(left["elements"][i], right["elements"][j]):
                add_last(temp, left["elements"][i])
                i += 1
            else:
                add_last(temp, right["elements"][j])
                j += 1
        while i < left["size"]:
            add_last(temp, left["elements"][i])
            i += 1
        while j < right["size"]:
            add_last(temp, right["elements"][j])
            j += 1
        
        my_list["elements"] = temp["elements"]
        my_list["size"] = temp["size"]
        
        return my_list

def quick_sort(my_list, sort_crit):
    if my_list["size"] <= 1:
        return my_list
    else:
        pivot = my_list["elements"][-1]
        left = new_list()
        right = new_list()
        
        for i in range (my_list["size"]-1):
            elem = my_list["elements"][i]
            if sort_crit(elem, pivot):
                add_last(left, elem)
            else:
                add_last(right, elem)
        sorted_left = quick_sort(left, sort_crit)
        sorted_right = quick_sort(right, sort_crit)
        
        result = new_list()
        for e in sorted_left["elements"]:
            add_last(result, e)
        add_last(result, pivot)
        for e in sorted_right["elements"]:
            add_last(result, e)
        return result