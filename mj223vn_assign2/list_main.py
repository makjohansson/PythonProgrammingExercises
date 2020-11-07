import list_functions as lf


test_list = lf.random_list(15)

# Test random_list function
print("Random list in the interval 1 to 100:\n", test_list)

# Test average function
print("\nAverage of values in list:", lf.average(test_list))

# Test only odd function
print("\nOnly the odd values in test_list:\n", lf.only_odd(test_list))

# Test to_string function
print("\nList to string:\n", lf.to_string(test_list))

# Test contains function
list_to_test_contains = [10, 32, 96, 25, 3, 54, 12]
print("\nIs \"a\" directly followed by \"b\"?")
print("a = 32 and after comes b = 96 is:", lf.contains(list_to_test_contains, 32, 96))
print("a = 32 and after comes b = 25 is:", lf.contains(list_to_test_contains, 32, 25))

# Test has_duplicates function
list_to_test_has_duplicates = [1, 2, 3, 4, 5, 1]
print(f"\nList: {list_to_test_has_duplicates}\nList contains duplicate? {lf.has_duplicates(list_to_test_has_duplicates)}")
list_to_test_has_duplicates = [1, 2, 3, 4, 5]
print(f"\nList: {list_to_test_has_duplicates}\nList contains duplicate? {lf.has_duplicates(list_to_test_has_duplicates)}")

