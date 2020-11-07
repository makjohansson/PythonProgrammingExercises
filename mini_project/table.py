# A binary search based dictionary imlementation 
# only using list of length 4.

# Each node is a list of length four where positions
# 0 = key, 1 = value, 2 = left-child, 3 = right-child

# Creates and returns the root to a new empty table.
# The complete function is given and should not be changed.
def new_empty_root():
    return [None,None,None,None]

# Add a new key-value pair to table if the key doean't already exist.
# Update value if already key exists in the table.
def add(root,key,value):
    if root[0] is not None:
        if root[0] == key:
            root[1] = value
        elif root[0] < key:
            if root[3] is None:
                root[3] = [key, value, None, None]
            else:
                add(root[3], key, value)
        elif root[0] > key:
            if root[2] is None:
                root[2] = [key, value, None, None]
            else:
                add(root[2], key, value)
    else:
        root[0] = key
        root[1] = value
        root[2] = None
        root[3] = None

# Returns a string representation of the table content.
# That is, all key-value pairs
def to_string(node):
    text = ''
    if node[0] is not None:
        if node[2] is not None:
            text += to_string(node[2])
        text += f'({node[0]},{node[1]}) '
        if node[3] is not None:
            text += to_string(node[3])
        return text
    else:
        return text

# Returns the value for the given key. Returns None if key doesn't exists.
def get(node,key):
    if node[0] is not None:
        if key < node[0]:
            if node[2] is None:
                return None
            else:
                return get(node[2], key)
        elif key > node[0]:
            if node[3] is None:
                return None
            else:
                return get(node[3], key)
        return node[1]
    else:
        return None


# Returns the maximum depth (an integer) of the tree.
# That is, the length of longest root-to-leaf path.
def max_depth(node):
    if node is None:
        return 0
    else:
        return 1 + max(max_depth(node[2]), max_depth(node[3]))
   
    

# Returns the number og key-value pairs currently stored in the table
def count(node):
    counter = 0
    if node[0] is not None:
        counter += 1
        if node[2] is not None:
            counter += count(node[2])
        if node[3] is not None:
            counter += count(node[3])
        return counter
    else:
        return 0


# Returns a list of all key-value pairs as tuples 
# sorted as left-to-right, in-order
def get_all_pairs(root):
    lst = list()
    if root[0] is not None:
        if root[2] is not None:
            lst.extend(get_all_pairs(root[2]))
        lst.append((root[0] , root[1]))
        if root[3] is not None:
            lst.extend(get_all_pairs(root[3]))
        return lst
    else:
        return lst


