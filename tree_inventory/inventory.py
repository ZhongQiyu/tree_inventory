# import re
# import docx
# import codecs
# import urllib
import pandas as pd
import numpy as np
# from googlesearch import search
from constants import *
# from selenium import webdriver


class Inventory:
    """
    This Python class models a tree inventory in an educational institution's
    context. It mainly contains the data copied from an Excel file where all
    records of trees planted in Union College's campus are stored. The class
    can access the features of data, modify their attributes, calculate stats,
    and format the data back to CSV files at this moment.
    """
    # get_features
    # set_features
    # get_data
    # set_data
    # calc_..._stats
    # format_data (to .csv)
    # pull the databases constructed from constants.py
    def __init__(self, path):
        """
        Initialize a tree inventory object, with a given
        file path of the inventory file.
        :param path: the file path of the tree inventory.
        """
        self.data = pd.read_excel(path)
        self.gen_s_count = 0  # to confirm
        # ?

    @staticmethod
    def test_globals():
        """

        :return:
        """
        for global_name, global_val in globals().items():
            print(f"name: {global_name}, val: {global_val}")

    @staticmethod
    def test_locals():
        """

        :return:
        """
        for local_name, local_val in locals().items():
            print(f"name: {local_name}, val: {local_val}")

    def get_data(self):
        """
        Get the inventory's data.
        :return: the data of the inventory.
        """
        return self.data

    def set_data(self, inventory_path):  # modify Excel sheet directly from Python
        """
        Set the inventory's data, given a file path of an
        existent inventory.
        :param inventory_path: the file path of the inventory.
        """
        self.data = pd.read_excel(inventory_path)

    def get_gen_s_count(self):  # count the number of effective data points
        """

        :return:
        """
        return self.gen_s_count

    def set_gen_s_count(self, new_count):
        """

        :param new_count:
        :return:
        """
        self.gen_s_count = new_count

    def get_family(self):
        """
        Get the families of the trees listed in the inventory as a set.
        :return: the parsed families of the trees listed in the inventory as a set.
        """
        data = self.get_data()
        inst_count = len(data)
        for index in range(inst_count):
            ...  # pick up from here
            # fam
            # get_family()
        com_names = set(COM_SCI_DB.keys())
        # sci_names = self.
        return set()

    # def get_family_stats(inventory):

    # def show_family_stats(inventory):

    def get_genera(self):
        """

        :return:
        """
        return set([sci_name if sci_name.find(" ") == -1 else sci_name[:sci_name.find(" ")]
                    for sci_name in COM_SCI_DB.values()])

    def get_genus_stats(self):
        """

        :return:
        """
        mapping = COM_SCI_DB
        genera = self.get_genera()
        data = self.get_data()
        com_names = pd.Series(data[COM_NAME])
        genus_stats = {}
        for genus in genera:
            genus_stats.update({genus: 0})
        for com_name in com_names:
            sci_name = mapping[com_name]
            if sci_name.find(" ") == -1:  # only have genus in the mapping
                genus = sci_name
            else:  # the mapping has both genus and species
                genus = sci_name[:sci_name.find(" ")]
            genus_stats[genus] += 1
        return genus_stats

    def show_genus_stats(self, genus_stats):
        """

        :param genus_stats:
        :return:
        """
        inventory_length = len(self.get_data()[COM_NAME])
        for genus, count in genus_stats.items():
            genus_percentage = count / inventory_length * 100
            if genus_percentage == 0:
                print(f"There are no trees with genus {genus} in the inventory.")
            else:
                print(f'There are {count} trees with genus {genus} in the inventory,'
                      f' percentage being {genus_percentage:.2f}%.')

    def validate(self):
        """
        # P.S. discrepancy between genus_stats and species_stats
        :return:
        """
        valid_data_points = len(self.get_data()[COM_NAME]) - self.get_gen_s_count()

    # try to combine species statistics with those of genera

    def get_species(self):
        """
        # want to specify what genus does a species belong to, so return the full unprocessed scientific name
        :return:
        """
        return [sci_name for sci_name in COM_SCI_DB.values()]

    def get_species_stats(self):
        """
        Obtain the statistics of the species
        :return:
        """
        # some redundancy when refer to get_genus_stats()
        # maybe better variable names
        mapping = COM_SCI_DB
        species = self.get_species()
        data = self.get_data()
        com_names = data[COM_NAME]
        species_stats = {}
        for s in species:
            species_stats.update({s: 0})
        for com_name in com_names:
            sci_name = mapping[com_name]
            # if sci_name.find(" ") != -1:
            species_stats[sci_name] += 1
        # validate
        # valid_data_points = sum(species_stats.values())
        # text file I/O
        species_stats_path = SUPERDIR_PATH + "species_stats.txt"
        species_stats_file = open(species_stats_path, 'w')
        # write every line into the file
        return species_stats

    def show_species_stats(self, species_stats):
        """

        :return:
        """
        # to transform to a more generic version
        valid_data_points = len(self.get_data()[COM_NAME]) - self.get_gen_s_count()
        all_count = sum(species_stats.values())
        for species, count in species_stats.items():
            species = self.get_com_name(species)
            percentage = count/valid_data_points*100
            if percentage == 0:
                print(f'There are no {species} tree(s) across the campus.')
            else:
                print(f'There are {count} {species} tree(s) across the campus, with a percentage of {percentage:.2f}%.')

    # get the percentage

    # use a generic show() method and then differ

    # def reformat(self, stats):
        # for data in stats:
        #     (refer to the sheets of scratch paper)
        #     (use a generic model and then vary with control logic)

    def gen_report(self, stats):
        """

        :return:
        """
        # one(?) helper on reformatting
        # three helpers on generating text files (family, genus, species)


if __name__ == "__main__":
    # Inventory.test_globals()
    # Inventory.test_locals()
    for name, val in vars("constants.py").items():
        print(f"name: {name}, val: {val}")

# wrap everything modularly in a main() call

# inventory = Inventory(SUPERDIR_PATH + INVENTORY_PATH)  # set the data
# inventory.set_mapping(SUPERDIR_PATH + COM_PATH, SUPERDIR_PATH + SCI_PATH)
# valid_data_points = len(inventory.get_data()[COM_NAME])
# print(f'There are {valid_data_points} valid data points in the inventory.')
# print()
# genus_stats = inventory.get_genus_stats()
# inventory.show_genus_stats(genus_stats)
# print()
# species_stats = inventory.get_species_stats()
# inventory.show_species_stats(species_stats)
# print()

# family_mapping = {}
# sci_names = list(inventory.get_mapping().values())
# type_ct = len(sci_names)
# NUM_RESULTS = 30
# for name in sci_names:
#     # handle the cases where the first result does not match (try to find some patterns)
#     # use urllib if necessary
#     genus = name[:name.index(" ")]
#     results = list(search(FAM_NAME + " " + genus, num_results=NUM_RESULTS))  # try to optimize the data structure
#     family_mapping.update({name: None})
#     found_family = False
#     result_index = 0
#     while not found_family and result_index < NUM_RESULTS:
#         result = results[result_index]
#         if result.find("aceae") == -1:
#             print("Family name not available.")
#         else:
#             print(result)
#             re.match("/[A-Za-z]aceae")
#             # find the index of 'aceae', and then search back to a '/'
#             family_mapping[name] = result[result.rfind("/") + 1:]
# print(f'There are {type_ct} types of trees listed in total, in terms of family represented scientifically.')

# gen_family_file = open(SUPERDIR_PATH + "family.txt", 'w')  # text file I/O
# family_mapping = [pair for pair in list(family_mapping.items()) if pair[1] is not None]
# valid_count = len(family_mapping)
# for index in range(valid_count):
#     fam, sci_name = family_mapping[index]
#     if index != valid_count - 1:
#         gen_family_file.write(f"{fam} - {sci_name}\n")
#     else:
#         gen_family_file.write(f"{fam} - {sci_name}")

# gen_genus_file

# gen_species_file

# results = search("family of fagus sylvatica", num=1, stop=1)
# for result in results:
#     print(result)

# set up a mapping of common names to scientific names, to refer to in the analysis
# extract genus: the ones have a space between genus name and species name need trimming, otherwise no need to
# read and process through tree inventory
# inventory_names = {}
# inventory_name_list = []
# to handle family: inventory["Family"] = ""
# to handle genus: inventory["Genus"] = ""
# to handle .sp: inventory["Species"] = ""
# to handle .sp: inventory_species_stats = {}

# automated family searching
# com_collection, sci_collection = init_collections(SUPERDIR_PATH + COMMON_PATH,
#                                                   SUPERDIR_PATH + SCI_PATH)
# com_name = com_collection.readline().strip('\n')
# sci_name = sci_collection.readline().strip('\n')
# while com_collection and sci_collection:
#     print(f'{com_name}:', search(com_name))
#     print(f'{sci_name}:', search(sci_name))
#     com_name = com_collection.readline().strip('\n')
#     sci_name = sci_collection.readline().strip('\n')

# inventory validation: use when an update happens, and need to improve reusability
# valid_count = 0
# invalid_count = 0
# for index in range(inventory_length):
#     # map the current common name with the scientific name
#     current_common_name = inventory_common_names[index]
#     # extract the family, the genus, and the species
#     if type(current_common_name) != float:
#         current_sci_name = all_name_collection[current_common_name]
#         current_genus = current_sci_name[:current_sci_name.index(" ")]
#         current_species = current_sci_name[current_sci_name.index(" ") + 1:]
#         if current_genus not in inventory_genus_stats:
#             inventory_genus_stats[current_genus] = 0
#         else:
#             inventory_genus_stats[current_genus] += 1
#         if current_species not in inventory_species_stats:
#             inventory_species_stats[current_species] = 0
#         else:
#             inventory_species_stats[current_species] += 1
#         inventory["Genus"][index] = current_genus
#         # genus validation is secured
#         inventory["Species"][index] = current_species
#         valid_count += 1
#     else:
#         invalid_count += 1

# print(tree_inventory[["Name_Commo", "Genus", "Species"]])
# print(valid_count, invalid_count)
# print(inventory_genus_stats)
# print(sum(list(inventory_genus_stats.values())))
# merge the Name_Commo and CommonName columns
# map a common name to family name
# add counts
#     if current_common_name not in inventory_name_dict:
#         inventory_name_dict[current_common_name] = 0
#         inventory_name_list.append(current_common_name)
#     else:
#         inventory_name_dict[current_common_name] += 1

# map the genus to family

# reuse anytime a new type comes available
# search_results = []
# for name in name_list:
#     for result in search(name, tld="com", lang="en", num=1, start=0, stop=1, pause=2.0):
#         search_results.append(result)
#
# reuse anytime an update happens
# with open("/Users/allen/Downloads/sci_names_list.txt", "w") as file:
#     for name in name_list:
#         file.write("%s\n" % name)

# family
# ------
# Fam1  ..%
# Fam2  ..%
# Fam3  ..%

# Genus
# ------
# Gen1  ..%
# Gen2  ..%
# Gen3  ..%

# Genus-species
# ------
# Gen-spe1  ..%
# Gen-spe2  ..%
# Gen-spe3  ..%
