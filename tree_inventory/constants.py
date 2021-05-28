# constants
# C:\\users\Joe\... on Windows
# ["", ""]
# abstract into a class Constants

import pandas as pd


# 5/28/21 meeting agenda
# 1. code update - share GitHub
# 2. inventory update - know the periodicity, and set reminders
# 3. 3D documentation - potential to learn, to discuss in the last meeting of this term
# 4. Environmental Club, tree trunk


def init_collection(path):
    """
    Initialize a collection of botanical names, either common or scientific.
    :param path: the file path where the collection of names lies in.
    :return: the collection as a file.
    """
    return open(path, 'r', encoding="utf-8", errors='ignore')


def init_collections(com_path, sci_path):
    """
    Initialize two collections, one of common names and one of scientific names,
    both about trees.
    :param com_path: the file path of the collection of cmmon names.
    :param sci_path: the file path of the collection of scientific names.
    :return: the processed collections.
    """
    com_collection = init_collection(com_path)
    sci_collection = init_collection(sci_path)
    return com_collection, sci_collection


def set_mapping(com_path, sci_path):
    """
    Get the mapping (move to Constants)
    :param com_path: the file path of the collection of common names.
    :param sci_path: the file path of the collection of scientific names.
    """

    gen_com_sci

    mapping = {}
    com_collection, sci_collection = self.init_collections(com_path, sci_path)
    current_com_line = com_collection.readline().strip("\n")
    current_sci_line = sci_collection.readline().strip("\n")
    while current_com_line and current_sci_line:
        current_sci_line = self.modify(current_sci_line)
        mapping.update({current_com_line: current_sci_line})
        current_com_line = com_collection.readline().strip("\n")
        current_sci_line = sci_collection.readline().strip("\n")
    com_collection.close()
    sci_collection.close()
    self.mapping = mapping


def modify(current_sci_line):
    """
    # handle three special input of scientific names
    (move to Constants, as a helper of set_mapping())
    :param current_sci_line:
    :return:
    """
    cultivar_index = current_sci_line.find(CULTIVAR_REPR)
    gen_species_index = current_sci_line.find(GEN_SPECIES_REPR)
    cross_index = current_sci_line.find(CROSS_REPR)
    if cultivar_index != -1:  # ..., var. ...
        current_sci_line = current_sci_line[0:cultivar_index]
    if gen_species_index != -1:  # ... sp. ...
        current_sci_line = current_sci_line[0:gen_species_index] + MOD_SPECIES  # + " species"
        # self.set_gen_s_count(self.get_gen_s_count() + 1)
    if cross_index != -1:  # ... X ...
        current_sci_line = current_sci_line[0:cross_index - 1] + current_sci_line[cross_index + 1:]
    return current_sci_line


def map_fam_gen():
    """
    Map the family with genus, given the
    :return:
    """
    agg_data = []
    # concatenate the family-genus dictionaries
    for name_dict in DICTS:
        dict_path = SUPERDIR_PATH + name_dict
        data = pd.read_csv(dict_path)
        # reformat the column names
        new_columns = [col[:col.find("[")] if col.find("[") != -1 else col for col in data.columns]
        data.columns = new_columns
        agg_data.append(data)
    agg_data = pd.concat(agg_data)
    # reformat the concatenated dictionary's indices
    new_indices = pd.Int64Index(range(len(agg_data.index)))
    agg_data.index = new_indices
    # send back as a CSV file
    data_file = agg_data.to_csv(path_or_buf=SUPERDIR_PATH + "genus (ALL).csv")
    # print(agg_data[["Genus", "Family"]])
    return pd.read_csv(data_file)


SUPERDIR_PATH = "/Users/allenzhong/Downloads/tree_inventory/"  # need to change when runs on a different machine
COM_PATH = "Accurate Treelist Common 2.1.txt"
SCI_PATH = "Accurate Treelist Scientific 2.1.txt"
INVENTORY_PATH = "Tree_TableToExcel3.xlsx"
DICTS = ["genus (A-C).csv", "genus (D-K).csv", "genus (L-P).csv", "genus (Q-Z).csv"]
COM_NAME = "Name_Common"  # perform data cleansing
CULTIVAR_REPR = ", var."
GEN_SPECIES_REPR = "sp."
MOD_SPECIES = "*species*"
CROSS_REPR = "X"
FAM_NAME = "scientific family name of"  # see if still necessary to remain
COM_SCI_DICT = {}  # or DF
FAM_GEN_DICT = map_fam_gen()

# to research: file closing
# to research: read lines in a .docx file without any conversion
# to research: browser = webdriver.Chrome("/Users/allen/Downloads/chromedriver")
