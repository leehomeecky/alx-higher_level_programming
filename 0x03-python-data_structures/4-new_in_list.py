#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    newList = [x for x in my_list]
    if idx < 0 or idx > (len(my_list) - 1):
        return my_list
    newList[idx] = element
    return (my_list)
