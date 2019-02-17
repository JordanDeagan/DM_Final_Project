# splits the data on a given attribute
from typing import List, Any


def split(cur_set, attribute: int):
    sub_sets = {}
    split_values = []
    for point in cur_set:
        if point[attribute] not in split_values:
            split_values.append(point[attribute])
    for feature in split_values:
        temp_set = []
        for point in cur_set:
            if point[attribute] == feature:
                temp_point = point[:]
                temp_point[attribute] = -1
                temp_set.append(temp_point)
        key = str(str(attribute)+", '"+feature+"'")
        sub_sets[key] = temp_set[:]
    return sub_sets


# a = [[1, 3, 6, 't'], [4, 5, 2, 't'], [1, 4, 3, 't'], [1, 4, 2, 't'], [1, 5, 2, 't'], [4, 4, 6, 'f'], [1, 3, 2, 't'],
#      [4, 4, 2, 'f'], [4, 5, 6, 'f'], [1, 3, 3, 't']]
# new_a = split(a,3)
# print(new_a[1])