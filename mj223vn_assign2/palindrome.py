def rec_helper(s, l, r):
    if r <= l:
        return True
    elif s[l] != s[r]:
        return False
    else:
        return rec_helper(s, l + 1, r - 1)


def is_palindrome(s):
    s = s.replace(" ", "").lower()
    from_the_left, from_the_right = 0, len(s)-1
    return rec_helper(s, from_the_left, from_the_right)


the_palindrome = "Was it a rat I saw"
if is_palindrome(the_palindrome):
    print(f"\"{the_palindrome}\" is a palindrome")
else:
    print(f"\"{the_palindrome}\" is not a palindrome")

