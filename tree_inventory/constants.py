import os
import pandas as pd

# to research: file closing
# to research: read lines in a .docx file without any conversion
# to research: browser = webdriver.Chrome("/Users/allen/Downloads/chromedriver")
# try to use debugger
# use colab? (no quite since not yet on the data-science/data-analytics level)
# handle the I/O since most of the office machines are Windows-based
# try to link this with thesis (the dataset of campus images)
# try to abstract each instance as an object

# 5/28/21 meeting agenda
# 1. code update - share GitHub
# 2. inventory update - know the periodicity, and set reminders (google calendar, and many other sources, want to
#    put them together)
# 3. 3D documentation - potential to learn, to discuss in the last meeting of this term
# 4. Environmental Club, tree trunk

# constants
# C:\\users\Joe\... on Windows
# abstract into a class Constants, if needed
# consider merging the dataframe of fam-gen and com-sci: would this be reasonable?

# 6/1/21 meeting agenda
# 1. set up tentative summer meeting schedule (done)
# 2. inventory update - calculation of statistics; if time, discuss abstraction (confirm features to use)
# 3. documentation update https://www.esri.com/en-us/arcgis/products/arcgis-3d-analyst/features
# - ArcGIS 3D Analyst? (able to discuss over the vacation)
# 4. Environmental Club
# - email out, wait for reply, and liaise with the other clubs once more before the term ends (follow up)

# features to use:
# common and scientific name
# diameter (DBH)
# overroador and against_ov
# season of pruning (notes)

# 6/4/21 meeting agenda (CSSA)
# 1. coverage of responsibilities: MUSE website maintenance (scope extension), database dev (course suggestions)
# 2. knowing the technical background of the member (Kenny)
# 3. year/term timeline distribution and expectations (ask the crew members if possible)
# 4. general chatting; thinking of Calvin

# 6/18/21 meeting agenda
# 1. project update: data manipulation (consult on feature augmentation),
#                    finalizing the map_fam_gen() method in constants.py
# 2. software: searching on the Web for 3D documentation, and trying to BootCamp for ArcGIS
# 3. committee update: another student (Paxton) joins, leader changes to Lex, adding more Facilities people
# 4. logistics: free on MWF and can do on TTh, depending on Joe's schedule
#               Commencement and summer intern
# i-Tree: source code
# augment the old dset to the new one (referred as Joe's experiments), with the help of i-Tree
# figure out the unit of the coordinates in the dset

# 6/29/21 meeting agenda
# 1. project update:
#    clean the code (#1),
#    finalize statistical module (constants.py, ...),
#    have a initial version of formatting.
#    should I replace the mapping given by Joe with the parsed one? be aware of timeline.
#    should I convert the constants.py module to a Python class?
# 2. extensive learning: aggregate Joe's resources
# 3. system logistics: BootCamp if needed, research the compatibility of ArcGIS software
# from the meeting
# 1. merge the datasets, and focus on the
# 2. research the dataset features: the system of the GPS coordinates (look at the phone screenshot)
# 3. differential correction wizard

# 7/13/21 meeting agenda
# 1. project update:
#    review the features of the new data table, and add them to the old one
#    finalize constants module: might want to consider .xlsx instead of .csv for the dataset
#    re-concatenate the DataFrames: review columns C&G, ask about sub-family in Wikipedia
#    update Wikipedia page with Magnolia, Robinia if needed (7/6/21)
#    complete the module to calculate the distributions of families
#    formalize the design of formatting


# bug record
# 5/4/21 UnicodeDecodeError: 'utf-8' codec can't decode byte 0xd4 in position 271: invalid continuation byte; resolved
# 5/8/21 requests.exceptions.HTTPError: 429 Client Error: Too Many Requests for url:
# (searching url); resolved (by switching a method to tackle)
# 6/21/21 TypeError: first argument must be an iterable of pandas objects, you passed an object of type "Series"


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


def map_com_sci(com_path, sci_path):
    """
    Get the mapping from common names of trees to their scientific names,
    and return the constructed mapping.
    :param com_path: the file path of the collection of common names.
    :param sci_path: the file path of the collection of scientific names.
    :return: the mapping from common names to scientific ones, in terms of
    their affiliation to trees.
    """
    com_sci_db = {}  # convert to DataFrame?
    com_collection, sci_collection = init_collections(com_path, sci_path)
    current_com_line = com_collection.readline().strip("\n")
    current_sci_line = sci_collection.readline().strip("\n")
    while current_com_line and current_sci_line:
        # handle the special cases in naming
        current_sci_line = modify(current_sci_line)
        com_sci_db.update({current_com_line: current_sci_line})
        current_com_line = com_collection.readline().strip("\n")
        current_sci_line = sci_collection.readline().strip("\n")
    com_collection.close()
    sci_collection.close()
    return com_sci_db


def modify(current_sci_line):
    """
    Modify the input of a line of scientific name,
    and return the modified results.
    # handle three special input of scientific names
    (move to Constants, as a helper of set_mapping())
    :param current_sci_line: the given line of scientific name.
    :return: the modified results.
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


def map_fam_gen(dsets):
    """
    Map the family with genus, given the constructed families and genera datasets.
    :param dsets: the datasets of the families and genera.
    :return: The database of family and genus, keyed by family primarily.
    """
    agg_data = []
    # if the file has not existed yet, generate one from given datasets
    agg_path = SUPERDIR_PATH + FAM_GEN_PATH
    if not os.path.exists(agg_path):
        # concatenate the family-genus dictionaries
        for name_dict in dsets:
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
        agg_data.to_csv(path_or_buf=agg_path)
    # map families and genera
    new_data = pd.read_csv(agg_path)
    families = new_data["Family"]
    genera = new_data["Genus"]
    fam_gen_db = pd.concat([families, genera], axis=1)
    return fam_gen_db


def get_name(com_or_sci):
    """
    Get the name of a tree, either common or scientific,
    and return the name on the other way around.
    :param com_or_sci: the common or scientific name of the tree.
    :return: the tree's scientific or common name.
    """
    if com_or_sci in COM_SCI_DB.keys():  # the passed name is a common name
        com_name = com_or_sci
        return COM_SCI_DB[com_name]
    else:  # the passed name is a scientific name
        sci_name = com_or_sci
        return {sci_name: com_name for (com_name, sci_name) in COM_SCI_DB.items()}[sci_name]


def get_family(genus):
    """
    Get the family of a genus of tree(s), given the genus.
    :param genus: the genus of the tree(s).
    :return: the family of such branch of tree(s).
    """
    return list(FAM_GEN_DB.iloc[FAM_GEN_DB.index[FAM_GEN_DB[GEN] == genus]][FAM])[0]


def get_fam_gen(species):
    """
    Get the family and genus of a species of tree(s), given the species.
    :param species: the species of the tree(s).
    :return: the family and genus of such branch of tree(s).
    """
    genus = species[:species.index(" ")]
    family = get_family(genus)
    return family, genus


SUPERDIR_PATH = "/Users/allenzhong/Downloads/tree_inventory/"  # need to change when runs on a different machine
COM_PATH = "Accurate Treelist Common 2.1.txt"
SCI_PATH = "Accurate Treelist Scientific 2.1.txt"
INVENTORY_PATH = "Tree_TableToExcel3.csv"
FAM_GEN_DICTS = ["genus (A-C).csv", "genus (D-K).csv", "genus (L-P).csv", "genus (Q-Z).csv"]
FAM_GEN_PATH = "genus (ALL).csv"
COM_NAME = "Name_Common"  # perform data cleansing in the dataset
CULTIVAR_REPR = ", var."
GEN_SPECIES_REPR = "sp."
MOD_SPECIES = "*species*"
CROSS_REPR = "X"  # consider modify the data structure
FAM = "Family"
GEN = "Genus"
COM_SCI_DB = map_com_sci(SUPERDIR_PATH + COM_PATH, SUPERDIR_PATH + SCI_PATH)
FAM_GEN_DB = map_fam_gen(FAM_GEN_DICTS)


# reference (try to have a sorting algorithm)
# http://www.simsgis.org/lite/
# https://medium.com/@soumyabrataroy/automate-the-google-search-using-python-b93e4621eb8b
# https://www.geeksforgeeks.org/performing-google-search-using-python-code/
# https://stackoverflow.com/questions/13962006/using-python-to-ask-a-web-page-to-run-a-search
# https://www.crummy.com/software/BeautifulSoup/bs4/doc/
# https://stackoverflow.com/questions/247770/how-to-retrieve-a-modules-path
# https://stackoverflow.com/questions/22786068/how-to-avoid-http-error-429-too-many-requests-python
# https://en.wikipedia.org/wiki/List_of_plant_genus_names_(A-C)
# https://en.wikipedia.org/wiki/List_of_plant_genus_names_(D-K)
# https://en.wikipedia.org/wiki/List_of_plant_genus_names_(L-P)
# https://en.wikipedia.org/wiki/List_of_plant_genus_names_(Q-Z)
# https://wikitable2csv.ggor.de/
# https://stackoverflow.com/questions/11346283/renaming-columns-in-pandas
