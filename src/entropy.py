# calculates individual entropy in a list of
# lists using the attribute in location value,
# differentiating between the favorable and
# unfavorable outcomes using the contents of
# parameters fav and unfav


import math


def ind_entropy(cur_set: list, value: int, fav, unfav):
    fav_count = 0
    unfav_count = 0
    size = 0
    for point in cur_set:
        if (point[value] == fav):
            fav_count += 1
        elif (point[value] == unfav):
            unfav_count += 1
        size += 1
    per_fav = fav_count / size
    per_unfav = unfav_count / size
    if fav_count > 0:
        log_fav = math.log(per_fav, 2)
    else:
        log_fav = 0
    if unfav_count > 0:
        log_unfav = math.log(per_unfav, 2)
    else:
        log_unfav = 0
    entropy = -(per_fav * log_fav) - (per_unfav * log_unfav)
    return entropy


# calclate the collective entropy of a new subset
# after splitting on parameter attribute


def col_entropy(cur_set: list, value: int, attribute: int, fav, unfav):
    split_values = []
    max_size = 0
    for point in cur_set:
        if point[attribute] not in split_values:
            split_values.append(point[attribute])
        max_size += 1
    sub_set = []
    sub_sizes = []
    for feature in split_values:
        temp = []
        size = 0
        for point in cur_set:
            if point[attribute] == feature:
                temp.append(point)
                size += 1
        sub_set.append(temp[:])
        sub_sizes.append(size)
    sub_entropy = []
    for sub in sub_set:
        sub_entropy.append(ind_entropy(sub, value, fav, unfav))
    entropy = 0
    for i in range(0, len(sub_set)):
        entropy += ((sub_sizes[i] / max_size) * sub_entropy[i])
    return entropy


# compare all possible sub_sets and determine which feature
# best purifies the data


def compare_attributes(cur_set, value: int, fav, unfav, splits: list):
    single = ind_entropy(cur_set, value, fav, unfav)
    print("Parent entropy: " + str(single))
    sub_sets = {}
    entropy_inc = {}
    for i in range(0, len(cur_set[0])):
        if i != value and i not in splits:
            sub_sets[i] = (col_entropy(cur_set, value, i, fav, unfav))
            entropy_inc[i] = (single - sub_sets[i])
            print("Feature " + str(i) + " entropy: " + str(sub_sets[i]))
            print("Feature " + str(i) + " entropy increase: " + str(entropy_inc[i]))
    checked = {}
    for feature in entropy_inc:
        if len(checked) == 0:
            biggest_inc = feature
        elif entropy_inc[feature] > entropy_inc[biggest_inc]:
            biggest_inc = feature
        checked[feature] = entropy_inc[feature]
    return biggest_inc


# a = [[1, 3, 6, 't'], [4, 5, 2, 't'], [1, 4, 3, 't'], [1, 4, 2, 't'], [1, 5, 2, 't'], [4, 4, 6, 'f'], [1, 3, 2, 't'],
#      [4, 4, 2, 'f'], [4, 5, 6, 'f'], [1, 3, 3, 't']]
# feature = compare_attributes(a, 0, 1, 4)
# print(feature)
