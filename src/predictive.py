import json
import random


def predict(point: list, predictor: dict, fav, unfav):
    result: str
    for feature in range(0, len(point)):
        checker = str(feature) + ", '" + point[feature] + "'"
        if checker in predictor:
            if type(predictor[checker]) == dict:
                result = predict(point, predictor[checker], fav, unfav)
            else:
                if not predictor[checker][0].isdigit():
                    result = predictor[checker]
                else:
                    perc = float(predictor[checker][0:5])
                    if random.random() <= perc:
                        result = fav
                    else:
                        result = unfav
        else:
            result = unfav
    return result


def tester(test: list, predictor: dict, value: int, fav, unfav):
    total = 0
    right = 0
    tp = 0
    fp = 0
    fn = 0
    tn = 0
    for line in test:
        check = predict(line, predictor, fav, unfav)
        if check == fav:
            if line[value] == fav:
                tp += 1
                right += 1
            else:
                fp += 1
        else:
            if line[value] == unfav:
                tn += 1
                right += 1
            else:
                fn += 1
        total += 1
    result = right / total
    print(result)
    print("True Positive: " + str(tp))
    print("False Positive: " + str(fp))
    print("False Negative: " + str(fn))
    print("True Negative: " + str(tn))
