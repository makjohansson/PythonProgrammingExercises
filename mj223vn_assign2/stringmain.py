import stringfunctions as sf

s = "hello"
n = 5

#Test the concat function
print(f"The string \"{s}\" concatenating with it self {n} times")
print(sf.concat(s, n))

#Test count function
x = "l"
print(f"\nThe number of times character \"{x}\" occurse in string \"{s}\"")
print(sf.count(s, x))

#Test reverse function
print(f"\nThe string \"{s}\" in reverse")
print(sf.reverse(s))

#Test first_last function
print(f"\nThe first and last character in the string \"{s}\"")
first, last = sf.first_last(s)
print(f"First: {first} and last {last}")

#Test the has_two_X function
X = "doubleXX"
print(f"\nWill be true if the string the string \"{X}\" contains exactly two instaces of the character X")
print(sf.has_two_X(X))

#Test the has_duplicats function
print(f"\nWill be true if the string \"{s}\" contains any duplicates characters")
print(sf.has_duplicates(s))