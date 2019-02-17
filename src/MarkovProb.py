import numpy as np
import random as rm


def twoStateWeights(cur_set: int, states: list):
    weights = [[0, 0], [0, 0]]
    cur_user = '0'
    cur_state: str
    aa = 0
    ab = 0
    ba = 0
    bb = 0
    total = 0
    for i, x in enumerate(cur_set):
        if x[1] != cur_user:
            cur_state = x[2]
            cur_user = x[1]
        else:
            if cur_state == states[0]:
                if x[2] == states[0]:
                    aa += 1
                else:
                    ab += 1
            else:
                if x[2] == states[0]:
                    ba += 1
                else:
                    bb += 1
            cur_state = x[2]
            total += 1
    pos = aa + ab
    neg = ba + bb
    weights[0][0] = "{0:.2f}".format(aa / pos)
    # print('aa: '+weights[0][0])
    weights[0][1] = "{0:.2f}".format(ab / pos)
    # print('ab: '+weights[0][1])
    weights[1][0] = "{0:.2f}".format(ba / neg)
    # print('ba: '+weights[1][0])
    weights[1][1] = "{0:.2f}".format(bb / neg)
    # print('bb: '+weights[1][1])
    return weights


def guessDays(cur_set: list, states: list, names: list, weights: list):
    cur_user = '0'
    cur_state: str
    tp = 0
    fp = 0
    fn = 0
    tn = 0
    right = 0
    total = 0
    for i, x in enumerate(cur_set):
        if x[1] != cur_user:
            cur_state = x[2]
            cur_user = x[1]
        else:
            if cur_state == states[0]:
                change = np.random.choice(names[0], p=weights[0])
                if change == names[0][0]:
                    if x[2] == states[0]:
                        tp +=1
                        right += 1
                    else:
                        fp += 1
                else:
                    if x[2] == states[0]:
                        fn += 1
                    else:
                        tn +=1
                        right += 1
            else:
                change = np.random.choice(names[1], p=weights[1])
                if change == names[1][0]:
                    if x[2] == states[0]:
                        tp += 1
                        right += 1
                    else:
                        fp += 1
                else:
                    if x[2] == states[0]:
                        fn += 1
                    else:
                        tn += 1
                        right += 1
            total += 1
            cur_state = x[2]
    result = right / total
    print(result)
    print("True Positive: " + str(tp))
    print("False Positive: " + str(fp))
    print("False Negative: " + str(fn))
    print("True Negative: " + str(tn))