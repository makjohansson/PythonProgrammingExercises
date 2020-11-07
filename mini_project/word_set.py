# A list based hash table implementation for strings.
# Initial bucket size is 10, we the double the bucket size
# when nElements = bucketSize.

size = 0      # global variable, current number of elements
# Returns a new empty set
# The complete function is given and should not be changed.
def new_empty_set():
    global size
    size = 0
    buckets = []
    for i in range(10):
        buckets.append([])
    return buckets 


# Adds word to word set if not already added
def add(word_set, word):
    global size
    if size == bucket_list_size(word_set):
        rehashing(word_set)
    if not contains(word_set, word):
        key = get_bucket_number(word_set, word)
        word_set[key].append(word)
        size += 1
    


# Returns current number of elements in set
def count(word_set):
    return size

# Returns current size of bucket list
def bucket_list_size(word_set):
    return len(word_set)

# Returns a string representation of the set content
def to_string(word_set):
    result = "{ "
    for key in word_set:
        for element in key:
            result += element + " "
    
    return result + "}"

# Returns True if word in set, otherwise False    
def contains(word_set, word):
    key = get_bucket_number(word_set, word)
    return word in word_set[key]


# Removes word from set if there, does nothing 
# if word not in set
def remove(word_set, word):
    global size
    if contains(word_set, word):
        key = get_bucket_number(word_set, word)
        word_set[key].remove(word)      
        size -= 1       
           


# Returns the size of the bucket with most elements
def max_bucket_size(word_set):
    max_size = 0
    for key in word_set:
        if len(key) > max_size:
            max_size = len(key)

    return max_size


# Rehash the set if bucket_list_size == number of elements
def rehashing(word_set):
    global size
    set_copy = word_set.copy()
    word_set.clear()
    for i in range(len(set_copy) * 2):
        word_set.append([])
    for key in set_copy:
        for element in key:
            add(word_set, element)
            size -= 1 # Decrease size because it is incremented in the add function
    

# Place word to bucket where the length of the bucket is less then 2
def linear_probing(word_set, word, key):
    global size
    index = 0 if key == bucket_list_size(word_set) - 1 else key 
    for i in range(index, bucket_list_size(word_set)):
        if len(word_set[i]) < 2:
            word_set[i].append(word)
            size += 1
            break


# Hash word by adding the ASCII for each letter in word
def hash_word(word):
    hash_sum = 0
    for char in range(len(word)):
        hash_sum += ord(word[char]) if char % 2 == 0 else ord(word[char]) * 2
    return hash_sum


# Returns bucket number for word. Words hash_sum modulus word_sets length
def get_bucket_number(word_set, word):
    hash = hash_word(word)
    bucket_number = hash % bucket_list_size(word_set)
    return bucket_number



    


