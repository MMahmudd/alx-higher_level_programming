#!/usr/bin/python3

def uniq_add(my_list=[]):
    unique_set = set(my_list)
    
    numb = 0

    # Iterate over each element in the input list
    for i in unique_set:
        numb += i
        return (numb)
