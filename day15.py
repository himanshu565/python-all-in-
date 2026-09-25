# Q1 Merge Dictionaries
def merge(dict1, dict2):
    new = {}

    for i in dict1:
        new[i] = dict1[i]

    for i in dict2:
        new[i] = dict2[i]

    return new
# The key idea to remember is:

# new[key] = value is how you add/update an item in a dictionary.
