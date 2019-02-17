def product_lists(path: str, item: str, aisles: list):
    product_ids = []
    with open(path, 'r') as file:
        lis = [line.split(',') for line in file]
        for i, x in enumerate(lis):
            if find_item(x, item):
                if len(aisles) > 0:
                    for aisle in aisles:
                        if proper_aisle(x, aisle):
                            product_ids.append(x[0])
                else:
                    product_ids.append(x[0])

    return product_ids


def find_item(line: list, item: str):
    if item in line[1]:
        return True
    else:
        return False


def proper_aisle(line: list, aisle: str):
    if line[-2] == aisle:
        return True
    else:
        return False