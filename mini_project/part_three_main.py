"""
Python script used to demonastrate the use of the functions in word_set.py and table.py for part 3
in the mini project
"""
import word_set as ws
import text_splitter as ts
import os
import table as tbl
import matplotlib.pyplot as plt


def longest_words_bst(lst):
    longest = 0
    for x in lst:
        if len(x[0]) > longest:
            longest = len(x[0])
    return longest


def count_words_bst(lst,longest_word):
    count_lst = []
    #Create a list with the length of the longest word
    for x in range(longest_word):
        count_lst.append(0)
    for x in lst:
        count_lst[len(x[0]) -1] += x[1]
    return count_lst


def count_words(words):
    dict_ = {}
    for word in words:
        dict_[word] = dict_[word] + 1 if word in dict_ else 1
    
    return dict_


def top_ten_finder(sorted_lst):
    top_ten = []
    counter = 0
    for word in sorted_lst:
        if len(word) > 4:
            top_ten.append(word)
            counter += 1
        if counter >= 10:
            break
    return top_ten
    

path_eng_news = os.getcwd() + "/eng_news_100K-sentences_list.txt"
path_holy_grail = os.getcwd() + "/holy_grail_list.txt"

words_eng_news = ts.get_text_as_word_list(path_eng_news)
words_holy_grail = ts.get_text_as_word_list(path_holy_grail)

################## Part 3.1 ############################
# Using word_set to count how many unique words that are 
# used in the two given texts files.
# Also using the Python set to compare the results
word_set_grail = ws.new_empty_set()

for word in words_holy_grail:
    ws.add(word_set_grail, word)

print("holy _grail unique word count:")
print("word_set count:", ws.count(word_set_grail))
print("Python set count:", len(set(words_holy_grail)))

word_set_eng = ws.new_empty_set()

for word in words_eng_news:
    ws.add(word_set_eng, word)

print("\neng_news unique word count:")
print("word_set count:", ws.count(word_set_eng))
print("Python set count:", len(set(words_eng_news)))

################## Part 3.2 ############################
# Using table to count how many words of a given length  
# each text has, and present a histogram (length vs count)


#Adding words to BST
root_eng = tbl.new_empty_root()
root_holy = tbl.new_empty_root()
value = 0
for x in words_holy_grail:
    value = 1 if tbl.get(root_holy, x) is None else tbl.get(root_holy, x) + 1
    tbl.add(root_holy,x,value)
for x in words_eng_news:
    value = 1 if tbl.get(root_eng, x) is None else tbl.get(root_eng, x) + 1
    tbl.add(root_eng,x, value)

bst_lst_eng = tbl.get_all_pairs(root_eng)
bst_lst_holy = tbl.get_all_pairs(root_holy)

print("Longest word holy:", longest_words_bst(bst_lst_holy))
print("Longest word eng: ", longest_words_bst(bst_lst_eng))

#Bst holy
word_length_holy_bst = list(range(0,longest_words_bst(bst_lst_holy)))
word_counter_holy_bst = count_words_bst(bst_lst_holy, longest_words_bst(bst_lst_holy))
#Bst news
word_length_news_bst = list(range(0,longest_words_bst(bst_lst_eng)))
word_counter_news_bst = count_words_bst(bst_lst_eng, longest_words_bst(bst_lst_eng))

# Setup for the histogram
fig, (holy_bst, news_bst) = plt.subplots(1,2, figsize=(15,8))

holy_bst.bar(word_length_holy_bst, word_counter_holy_bst)
holy_bst.set_title("Holy Grail")
holy_bst.set_xlabel("word length")
holy_bst.set_ylabel("word count")

news_bst.bar(word_length_news_bst, word_counter_news_bst)
news_bst. set_title("eng_news")
news_bst.set_xlabel("word length")
news_bst.set_ylabel("word count")



################## Part 3.3 ############################
# Using to present a list of the top-10 most frequently 
# used words having a length larger than 4. 
# Also using Pythons dictionary to present the comparison.

word_dict_grail = count_words(words_holy_grail)
word_dict_eng_news = count_words(words_eng_news)

most_frequent_words_grail = [word for word in sorted(word_dict_grail, key=word_dict_grail.get, reverse=True)]
top_ten_grail = top_ten_finder(most_frequent_words_grail)

most_frequent_words_eng_news = [word for word in sorted(word_dict_eng_news, key=word_dict_eng_news.get, reverse=True)]
top_ten_eng_news = top_ten_finder(most_frequent_words_eng_news)

bst_lst_eng = tbl.get_all_pairs(root_eng)
bst_lst_holy = tbl.get_all_pairs(root_holy)

#Filtering the list from words shorter than 4 characters
eng_filtered = filter(lambda x: len(x[0]) > 4, bst_lst_eng)
holy_filtered = filter(lambda x: len(x[0]) > 4, bst_lst_holy)
filtered_eng_list = list(eng_filtered)
filtered_holy_list = list(holy_filtered)
freq_bst_eng = [word for word in sorted(filtered_eng_list, key=lambda x:x[1], reverse=True)]
freq_bst_holy = [word for word in sorted(filtered_holy_list, key=lambda x:x[1], reverse=True)]


print("\nCount of the top-10 most frequently " +
        "used words having a\nlength larger than 4 using table.py: ")
print("\nHoly Grail:")
for word in freq_bst_holy[:10]:
    print(f"{word[0]}: {word[1]}")
print("\nEng news sentences:")
for word in freq_bst_eng[:10]:
    print(f"{word[0]}: {word[1]}")

# Using pythons dictionary
print("\nCount of the top-10 most frequently " +
        "used words having a\nlength larger than 4 using Pythons dictionary: ")
print("\nHoly Grail:")
for word in top_ten_grail:
    print(f"{word}: {word_dict_grail[word]}")
print("\nEng news sentences:")
for word in top_ten_eng_news:
    print(f"{word}: {word_dict_eng_news[word]}")

# Open and present the histogram
plt.show()