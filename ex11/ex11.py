import itertools


class Node:
    def __init__(self, data, pos=None, neg=None):
        self.data = data
        self.positive_child = pos
        self.negative_child = neg

    def get_data(self):
        return self.data

    def set_data(self, val):
        self.data = val


class Record:
    def __init__(self, illness, symptoms):
        self.illness = illness
        self.symptoms = symptoms

    def get_symptoms(self):
        return self.symptoms

    def get_illness(self):
        return self.illness


def parse_data(filepath):
    with open(filepath) as data_file:
        records = []
        for line in data_file:
            words = line.strip().split()
            records.append(Record(words[0], words[1:]))
        return records


class Diagnoser:
    def __init__(self, root):
        self.root = root

    def diagnose(self, symptoms):
        """this method gets a list of symptoms and diagnoses which illness
        fits the symptoms"""
        cur = self.root
        while cur.positive_child and cur.negative_child:  # Node has children
            if cur.get_data() in symptoms:
                cur = cur.positive_child  # go to positive child
            else:
                cur = cur.negative_child  # go to negative child
        return cur.get_data()  # means we got to a leaf (illness)

    def calculate_success_rate(self, records):
        """this method gets a list of type Record objects, and returns the
        ratio between num of diagnose successes of records (according to the
        tree), and num of records overall(assuming records list isn't empty)"""
        num_correct_illness = 0
        for r in records:
            if self.diagnose(r.get_symptoms()) == r.get_illness():
                num_correct_illness += 1  # was diagnosed successfully
        return num_correct_illness / len(records)  # the ratio

    def all_illnesses(self):
        """this method returns a sorted list (by frequency) of all illnesses
        in tree leaves"""
        all_illnesses_lst = []
        all_illnesses_dict = {}  # will check frequency of each illness
        cur = self.root
        self.all_illnesses_helper(cur, all_illnesses_dict)
        # this next line sorts the dictionary by its values from high to low
        sorted_ill = sorted(all_illnesses_dict.items(), key=lambda x: -x[1])
        for illness in sorted_ill:
            all_illnesses_lst.append(illness[0])  # add illnesses to list by
        #  its frequency
        return all_illnesses_lst

    def all_illnesses_helper(self, cur, all_illnesses_dict):
        """this helper method gets current Node, dictionary (of illness to
        number of appearances in tree) and updates the dictionary"""
        if cur.positive_child is None and cur.negative_child is None:
            if cur.get_data() not in all_illnesses_dict: # first time reaching
                #  this illness
                all_illnesses_dict[cur.get_data()] = 1
            else:  # not first time reaching this illness, add 1 to num
                #  of appearances
                all_illnesses_dict[cur.get_data()] += 1
            return
        self.all_illnesses_helper(cur.positive_child, all_illnesses_dict)
        self.all_illnesses_helper(cur.negative_child, all_illnesses_dict)

    def most_rare_illness(self, records):
        """this method gets list of type Record objects, traverses symptoms
        list in each record, and returns most rare illness(assuming records
        list isn't empty"""
        rareness_dict = {}
        for record in records:
            if self.diagnose(record.get_symptoms()) not in rareness_dict:
                rareness_dict[self.diagnose(record.get_symptoms())] = 1
            else:
                rareness_dict[self.diagnose(record.get_symptoms())] += 1
        min_val = list(rareness_dict.values())[0]  # meanwhile
        most_rare_illness = ""  # meanwhile
        for illness in rareness_dict:
            if rareness_dict[illness] <= min_val:  # found rarer illness
                min_val = rareness_dict[illness]
                most_rare_illness = illness
        # these next lines check if there is an illness in the tree that was
        #  diagnosed 0 times
        all_illnesses_lst = self.all_illnesses()
        for illness in all_illnesses_lst:
            if illness not in rareness_dict:
                most_rare_illness = illness
                break  # found illness that was not diagnosed
        return most_rare_illness

    def paths_to_illness(self, illness):
        """this method gets illness name(string type), and returns list of all
        paths in the tree that get to this illness"""
        lst_paths_lists = []  # will be updated with all paths in the
        #  tree to illness
        cur_path_lst = []
        cur = self.root
        self.paths_helper(cur, lst_paths_lists, cur_path_lst, illness)
        return lst_paths_lists

    def paths_helper(self, cur, lst_paths_lists, cur_path_lst, illness):
        """this helper method gets current Node, lst of paths(first time-
        empty), current path list, and illness. returns list of all paths
        in the tree that get to this illness"""
        if cur.positive_child is None and cur.negative_child is None:
            #  reached an illness
            if cur.get_data() == illness:  # reached required illness
                lst_paths_lists.append(cur_path_lst)  # update list of paths
            return
        # build the path to positive child
        self.paths_helper(cur.positive_child, lst_paths_lists,
                          cur_path_lst + [True], illness)

        # build the path to negative child
        self.paths_helper(cur.negative_child, lst_paths_lists,
                          cur_path_lst + [False], illness)


def build_tree(records, symptoms):
    """this function gets list of type Record objects, and list of
    symptoms(string). the function builds a tree according to list
    of symptoms, and returns its root"""
    tree = build_tree_helper(symptoms, 0)  # builds the tree, with empty
    #  string illnesses
    symptom_to_tf = {}
    fill_tree_illnesses(symptom_to_tf, records, tree)
    return tree


def build_tree_helper(symptoms, index):
    """this function builds tree without illnesses, and puts an empty string
    as illnesses (for the meantime)"""
    if index == len(symptoms):
        return Node("")
    return Node(symptoms[index],
                build_tree_helper(symptoms, index + 1),
                build_tree_helper(symptoms, index + 1))


def fill_tree_illnesses(symptom_to_tf, records, nd):
    """this function gets a path (dictionary of symptom to True\ False),
    list of Record type objects and a Node(that represents a tree
    or part of it), and fills the matching illness (to each path)"""
    if nd.positive_child is None and nd.negative_child is None:
        illness = find_illness(symptom_to_tf, records)
        nd.set_data(illness)  # fill this leaf with matching illness
        return
    symptom_to_tf[nd.get_data()] = True
    fill_tree_illnesses(symptom_to_tf, records, nd.positive_child)
    symptom_to_tf[nd.get_data()] = False
    fill_tree_illnesses(symptom_to_tf, records, nd.negative_child)


def find_illness(symptom_to_tf, records):
    """this function gets a path (dictionary of symptom to True\False),
    and list of Record type objects, and returns best matching illness"""
    illness_counter = {}  # matches illness to num of appearances
    for record in records:
        if does_path_match_record(record, symptom_to_tf):
            if record.get_illness() not in illness_counter:
                illness_counter[record.get_illness()] = 1
            else:
                illness_counter[record.get_illness()] += 1
    if illness_counter is None:  # symptom_to_tf path doesn't match any record
        return records[0].get_illness()  # dummy illness
    max_val = -1  # meanwhile
    matching_illness = None  # meanwhile
    for illness in illness_counter:
        if illness_counter[illness] > max_val:
            max_val = illness_counter[illness]
            matching_illness = illness
    return matching_illness


def does_path_match_record(record, symptom_to_tf):
    """"this helper function gets a Record type object, a path (dictionary of
    symptom to True\False), and checks if the path matches the record"""
    for sym in symptom_to_tf:
        sym_tf = symptom_to_tf[sym]
        if sym_tf is True and \
                sym not in record.get_symptoms():
            return False  # in path, not in record
        if sym_tf is False and \
                sym in record.get_symptoms():
            return False  # not in path, in record
    return True


def optimal_tree(records, symptoms, depth):
    """this function gets list of Record type objects, symptoms list,
    and depth. the function returns a root of a tree with depth "depth"
    with highest success rate"""
    best_ratio = -1  # meanwhile
    best_root = None  # meanwhile
    # iterate subgroups length depth of symptoms list
    for dep_sym in itertools.combinations(symptoms, depth):
        root = build_tree(records, dep_sym)
        diag = Diagnoser(root)
        # check success rate of this tree
        cur_ratio = diag.calculate_success_rate(records)
        if cur_ratio > best_ratio:
            best_ratio = cur_ratio
            best_root = root
    return best_root


if __name__ == "__main__":
    pass