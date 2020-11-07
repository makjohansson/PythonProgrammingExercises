"""
Python script used to demonastrate the tests for part 4
in the mini project
4.1 - Measure time to look-up 20000 keys in three BTS of different size
4.2 - Measure time to add 1000 keys to hashset with different sizes.
"""
import os, time
import word_set as ws, text_splitter as ts
import matplotlib.pyplot as plt
import table as tbl
import random
from word_set import rehashing
import numpy as np


path_eng_news = os.getcwd() + "/eng_news_100k-sentences_list.txt"
words_eng_news = ts.get_text_as_word_list(path_eng_news)
words_set = set(words_eng_news)
word_set_list = list(words_set)

hash_word_set_warm_up = ws.new_empty_set()
hash_word_set = ws.new_empty_set()

# Count words in dictionary, returns a new dictionary
def count_words(lst_words):
    dict_ = {}
    for word in lst_words:
        dict_[word] = dict_[word] + 1 if word in dict_ else 1

    return dict_


#returns a list of 20k random words in the range 0 to x
def get_random_words(lst,range_):
    rand_words = lst[0:range_]
    random.shuffle(rand_words)
    return rand_words[0:20000]


word_dict = count_words(words_eng_news)

# 4.1
root_1 = tbl.new_empty_root()
root_2 = tbl.new_empty_root()
root_3 = tbl.new_empty_root()

dict_ = word_dict.items()
list_dict = list(dict_)

# Add 40000, 60000, 80000 words to three different BST
for word in list_dict[:40000]:
    tbl.add(root_1,word[0],word[1])

for word in list_dict[:60000]:
    tbl.add(root_2,word[0],word[1])

for word in list_dict[:80000]:
    tbl.add(root_3,word[0],word[1])

##### Console prints, can be ignored #####
#print(f" tbl 1:{tbl.max_depth(root_1)}, tbl 2: {tbl.max_depth(root_2)}, tbl 3: {tbl.max_depth(root_3)}")
#print(f'Tables: {tbl.count(root_1)}, {tbl.count(root_2)}, {tbl.count(root_3)}')

bst_times = [0,0,0]
bst_depths = [0,0,0]
for x in range(10):
    rand_words = get_random_words(list_dict, 40000)
    bst_start = time.time()
    for x in rand_words:
        tbl.get(root_1, x[0])
    time_elapsed = time.time() - bst_start
    bst_times[0] += time_elapsed
    bst_depths[0] += tbl.max_depth(root_1)

    rand_words = get_random_words(list_dict, 60000)
    bst_start_2 = time.time()
    for x in rand_words:
        tbl.get(root_2, x[0])
    time_elapsed_2 = time.time() - bst_start_2
    bst_times[1] += time_elapsed_2
    bst_depths[1] += tbl.max_depth(root_2)

    rand_words = get_random_words(list_dict, 80000)
    bst_start_3 = time.time()
    for x in rand_words:
        tbl.get(root_3, x[0])
    time_elapsed_3 = time.time() - bst_start_3
    bst_times[2] += time_elapsed_3
    bst_depths[2] += tbl.max_depth(root_3)

##### Console prints, can be ignored #####
#print(f'Average times for finding 20000 words\nBST_1: {(bst_times[0] / 10) * 1000} depth:{bst_depths[0] / 10}\nBST_2: {(bst_times[1] / 10) * 1000} depth:{bst_depths[1] / 10}\nBST_3:{(bst_times[2] / 10) * 1000} depth:{bst_depths[2] / 10}')

bst_time_ = {"BST_40k" : (bst_times[0] / 10) * 1000,"BST_60k" : (bst_times[1] / 10) * 1000, "BST_80k" : (bst_times[2] / 10) * 1000}
bst_depth_ = {"BST_40k" : bst_depths[0] / 10,"BST_60k" : bst_depths[1] / 10, "BST_80k" : bst_depths[2] / 10}


# Results 4.2, hashtable
range_a = 0
range_b = 1000
rounds = 1
elements_vs_time = {}
bucket_size_vs_set_size = {}
bucket_size_vs_word_count = {}
set_size_vs_word_count = {}

while rounds < 100:
    start_time = time.time()
    for words in word_set_list[range_a:range_b]:
        ws.add(hash_word_set, words)
        if ws.bucket_list_size(hash_word_set) == ws.count(hash_word_set):
            set_size_vs_word_count[str(ws.bucket_list_size(hash_word_set))] = ws.count(hash_word_set)
    time_elapsed = time.time() - start_time

    ##### Console prints, can be ignored #####
    # print(f"Round {rounds}: Added {range_b - range_a} unique words in {time_elapsed} sec")
    # print(f"{ws.count(hash_word_set)} words in set")
    # print(f"Max bucket size: {ws.max_bucket_size(hash_word_set)}")

    elements_vs_time[str(ws.count(hash_word_set))] = time_elapsed * 1000
    bucket_size_vs_set_size[str(ws.bucket_list_size(hash_word_set))] = ws.max_bucket_size(hash_word_set)
    bucket_size_vs_word_count[str(ws.count(hash_word_set))] = ws.max_bucket_size(hash_word_set)
    set_size_vs_word_count[str(ws.bucket_list_size(hash_word_set))] = ws.count(hash_word_set)
    range_a += 1001
    range_b += 1001
    rounds += 1


# Setup for the barcharts for 4.1 and 4.2
fig, ((el_vs_tim, buck_vs_word), (buck_vs_size, size_vs_words)) = plt.subplots(2,2, figsize=(15,10))

#4.2
# Plot for time to add words
el_vs_tim.plot(*zip(*elements_vs_time.items()))
el_vs_tim.set_title("Time it takes to add new elements")
el_vs_tim.set_ylabel("Time in milliseconds")
el_vs_tim.set_xlabel("Words in set")
start, end = el_vs_tim.get_xlim()
el_vs_tim.set_xticks(np.arange(start, end, 10))

# Plot for max bucket vs words added
buck_vs_word.plot(*zip(*bucket_size_vs_word_count.items()))
buck_vs_word.set_title("Max bucket size changes with the total words")
buck_vs_word.set_ylabel("Max bucket size")
buck_vs_word.set_xlabel("Words in set")
start, end = buck_vs_word.get_xlim()
buck_vs_word.set_xticks(np.arange(start, end, 10))

# Plot for max bucket vs table size
buck_vs_size.plot(*zip(*bucket_size_vs_set_size.items()))
buck_vs_size.set_title("Max bucket size changes with the set sizes")
buck_vs_size.set_ylabel("Max bucket size")
buck_vs_size.set_xlabel("Size of set")

# Plot for table size vs words
size_vs_words.plot(*zip(*set_size_vs_word_count.items()))
size_vs_words.set_title("Size of set changes compared to added words")
size_vs_words.set_ylabel("Words in set")
size_vs_words.set_xlabel("Size of set")
start, end = size_vs_words.get_xlim()
size_vs_words.set_xticks(np.arange(start, end, 2))

#4.1
fig, (bst_size_vs_time, depth_vs_size) = plt.subplots(1,2, figsize=(15,8))
bst_size_vs_time.axis(ymin=100, ymax=320)
depth_vs_size.axis(ymin=30, ymax=50)
#Plot for bst time
bst_size_vs_time.bar(*zip(*bst_time_.items()))
bst_size_vs_time.set_title("Look up time bst")
bst_size_vs_time.set_ylabel("Time in milliseconds")
bst_size_vs_time.set_xlabel("Size")

#Depth
depth_vs_size.bar(*zip(*bst_depth_.items()))
depth_vs_size.set_title("Depth bst")
depth_vs_size.set_ylabel("Depth")
depth_vs_size.set_xlabel("Size")
plt.show()



