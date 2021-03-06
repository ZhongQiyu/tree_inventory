# IN DEV: a class of trees (Tree)
# linking the idea of visualizing the features of a tree in a three-dimensional way
# input: (maybe) eight photo captures of a tree
# output: the states of the branches, etc. (like the physical status but decomposed to many things)
# update GitHub
# would it be useful to import the tree inventory file, and then extract all the features it has right now,
# to perform analytics?

# import re
# import time
# import stanfordkarel
import pandas as pd
from constants import *
# from googlesearch import search

# set up a generic representation of the trees in the inventory data
# the trees work like instances in the dataset
# migrate some of the constants to tree.py

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


class Tree:
    def __init__(self, com_name):
        """
        Initialize an instance of a tree, given its common name.
        :param com_name: the common name of the tree.
        """
        self.com_name = com_name
        self.sci_name = ...  # a method that maps common name to scientific name
        self.dbh = ...
        self.over_road_or_sidewalk = ...
        self.against_over_building = ...
        # ask for more features if need to extend project

    # def reformat(self, mode): map/decompose representations of the tree's scientific name
    def com_to_sci(self):
        """
        Convert the common name representation to a scientifically-named one.
        :return: the scientific name representation.
        """


inventory_data = pd.read_csv("/Users/allenzhong/Downloads/tree_inventory/Tree_TableToExcel3.csv")
tree_features = inventory_data.columns
print(tree_features)
