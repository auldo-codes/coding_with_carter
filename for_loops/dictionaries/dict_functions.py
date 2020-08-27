
from actual_dictionaries import *

def change_key_name(data_dict):
    for old_key in data_dict.keys():
        new_key = input("Who wants " + data_dict[old_key] + " ? ")
        data_dict[new_key] = data_dict.pop(old_key)
    print(data_dict)