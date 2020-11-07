def concat(s, n):
    temp = ""
    for i in range(n):
        temp += s
    return temp

def count(s, x):
    counter = 0
    for i in range(len(s)):
        if s[i] == x:
            counter += 1
    return counter

def reverse(s):
    sInReverse = ""
    for i in range(len(s) - 1 , -1 , -1):
        sInReverse += s[i]
    return sInReverse

def first_last(s):
    return s[0], s[-1]

def has_two_X(s):
    X_counter = 0
    for i in range(len(s)):
        if s[i] == "X":
            X_counter += 1
    if X_counter == 2:
        return True
    else:
        return False

def has_duplicates(s):
    duplicateFound = False
    for i in range(len(s)):
        for j in range(i+1, len(s)):
            if(s[i] == s[j]):
                duplicateFound = True
                break
        if duplicateFound:
            break
    return duplicateFound
