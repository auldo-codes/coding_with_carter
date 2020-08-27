what_snack_is_that_dict = {

    'snack1': 'nachos',
    'snack2': 'mozerella_sticks',
    'snack3': 'doritos',
    'snack4': 'pears',
    'snack5': 'oreos',
    'snack6': 'popcorn',
    'snack7': 'oranges',
    'snack8': 'swedish fish',
    'snack9': 'almonds',

}


# Instructions
# write a function to change name of each key in a for loop

# Steps

# create a dictionary - DICTS DO NOT LOOP IN ORDER
# define variables for old_key, new_key
# set up a dictionary for loop - keys()
# use input to define each new_key
# call the function
# tests!!!

# Ideas to try/research
# loop through values of dictionary instead
# Use create a test to see if key was already changed



# function



change_key_name(what_snack_is_that_dict)

# errors : infinite looping, not changing all old_keys before cycling re-looping new keys
# solution: create a boolean test that equates to false if the key has already been changed


# print(what_snack_is_that_dict)


# EXAMPLES
"""
dictionary[new_key] = dictionary[old_key]
del dictionary[old_key]
Or in 1 step:

dictionary[new_key] = dictionary.pop(old_key)
"""