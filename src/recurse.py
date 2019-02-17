# recursively goes through a set to find the most
# identifiable feature, splits on it, then repeates
# for all non pure branches

from src.entropy import *
from src.split import *


def build_tree(cur_set: list, value: int, fav, unfav, splits: list):
    best = compare_attributes(cur_set, value, fav, unfav, splits)
    cur_splits = splits + [best]
    eob = len(cur_set[0])==(len(cur_splits)+1)
    formed_dict = split(cur_set, best)
    for feature in formed_dict.keys():
        if ind_entropy(formed_dict[feature], value, fav, unfav) != 0.0:
            if (len(formed_dict[feature]) >= 20) and not eob:
                formed_dict[feature] = build_tree(formed_dict[feature], value, fav, unfav, cur_splits)
            else:
                formed_dict[feature] = average_result(formed_dict[feature], value, fav)
        else:
            formed_dict[feature] = formed_dict[feature][0][value]
    return formed_dict


def average_result(basket, value: int, fav):
    fav_value = 0
    total = 0
    for point in basket:
        if point[value] == fav:
            fav_value += 1
        total += 1
    perc = (fav_value / total)*100
    return str("{:05.2f}".format(perc)) + "% " + fav
