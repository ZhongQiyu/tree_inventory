# IN DEV: a class of trees (Tree)
# linking the idea of visualizing the features of a tree in a three-dimensional way
# input: (maybe) eight photo captures of a tree
# output: the states of the branches, etc. (like the physical status but decomposed to many things)

# would it be useful to import the tree inventory file, and then extract all the features it has right now,
# to perform analytics?

import re
import time
import stanfordkarel
import pandas as pd
# from googlesearch import search


# sci_names = open("/Users/allenzhong/Downloads/tree_inventory/Accurate Treelist Scientific 2.1.txt",encoding='latin-1')
# name_data = sci_names.readline()#
# while name_data:
#     print(name_data)
#     search_string = f'scientific family name of {name_data}'
#     results = search(search_string, num_results=1)
#     found_family = False
#     for result in results:
#         if result.find("aceae") != -1:
#             found_family = True
#             print(f'The family of {name_data} is found.')  # need regex to extract the family
#             break  # handling the generator data structure and searching threshold of 1
#     if not found_family:
#         print(f"The family of {name_data} is not found.")
#     name_data = sci_names.readline()#


# test_re = re.compile("//w{3}")
# family_re = "/([A-Z]){1}([a-z]){1,10}aceae"
# print(test_re.match("http://www.theplantlist.org/browse/A/Malvaceae/Tilia/"))
