# =======================================#
# Imports                                #
# =======================================#
# Python Import
import json
import csv


# =======================================#
# Public Methods                         #
# =======================================#

def reorganize_orders(path_from: str, path_prior: str, path_test: str):
    p_to = []
    p_from = []
    with open(path_from, 'r') as file:
        lines = file.readlines()
        for i in range(0, len(lines)):
            line = lines[i]
            split_line = line.split(',')
            if i == (len(lines) - 1):
                if split_line[2] == 'train':
                    p_to.append(line)
            else:
                if split_line[2] == 'train':
                    p_to.append(line)
                elif split_line[2] == 'prior':
                    if lines[i + 1].split(',')[2] == 'test':
                        split_line[2] = 'train'
                        new_line = ''
                        for part in range(0, len(split_line)):
                            if part != (len(split_line) - 1):
                                new_line = new_line + split_line[part] + ','
                            else:
                                new_line = new_line + split_line[part]
                        p_to.append(new_line)
                    else:
                        p_from.append(line)
    file_test = open(path_test, 'w')
    file_test.writelines(p_to)
    file_test.close()
    file_prior = open(path_prior, 'w')
    file_prior.writelines(p_from)
    file_prior.close()


def markov_orders(path_from: str, path_chain: str):
    p_to = []
    with open(path_from, 'r') as file:
        lines = file.readlines()
        for i in range(0, len(lines)):
            line = lines[i]
            split_line = line.split(',')
            if i == (len(lines) - 1):
                if split_line[2] == 'train':
                    p_to.append(line)
            else:
                if split_line[2] == 'train':
                    p_to.append(line)
                elif split_line[2] == 'prior':
                    if lines[i + 1].split(',')[2] == 'test':
                        split_line[2] = 'train'
                        new_line = ''
                        for part in range(0, len(split_line)):
                            if part != (len(split_line) - 1):
                                new_line = new_line + split_line[part] + ','
                            else:
                                new_line = new_line + split_line[part]
                        p_to.append(new_line)
                    elif lines[i + 1].split(',')[2] == 'train' or lines[i + 2].split(',')[2] == 'test':
                        p_to.append(line)
    with open(path_chain, 'w') as c:
        c.writelines(p_to)


def reorganize_products(prev_test_path: str, prev_prior_path: str, new_test_path: str, new_prior_path: str,
                        orders_path: str):
    test_dict = {}
    prior_dict = {}
    with open(prev_test_path, 'r') as ptp:
        ptp_purchases = ptp.readlines()
    prev_order = '0'
    full_order = []
    for i, line in enumerate(ptp_purchases):
        x = line.split(',')
        if x[0] != prev_order:
            test_dict[prev_order] = full_order
            prev_order = x[0]
            full_order = [x[1]]
        else:
            full_order.append(x[1])
        if i % 10000 == 0:
            print(i)
    test_dict[prev_order] = full_order
    prev_order = '0'
    full_order = []
    print("test")
    with open(orders_path, 'r') as organize:
        test_order = []
        for line in organize.readlines():
            test_order.append(line.split(',')[0])
    with open(prev_prior_path, 'r') as ppp:
        pppr = ppp.readlines()
    print("ready")
    for i, line in enumerate(pppr):
        x = line.split(",")[:2]
        if x[0] != prev_order:
            if prev_order in test_order:
                test_dict[prev_order] = full_order
            else:
                prior_dict[prev_order] = full_order
            prev_order = x[0]
            full_order = [x[1]]
        else:
            full_order.append(x[1])
        if i % 10000 == 0:
            print(i)
    if prev_order in test_order:
        test_dict[prev_order] = full_order
    else:
        prior_dict[prev_order] = full_order
    print("done")
    with open(new_test_path, 'w') as ntp:
        json.dump(test_dict, ntp)
    with open(new_prior_path, 'w') as npp:
        json.dump(prior_dict, npp)


def rechain_products(prev_test_path: str, prev_prior_path: str, new_test_path: str, orders_path: str):
    test_dict = {}
    with open(prev_test_path, 'r') as ptp:
        ptp_purchases = ptp.readlines()
    prev_order = '0'
    full_order = []
    for i, line in enumerate(ptp_purchases):
        x = line.split(',')
        if x[0] != prev_order:
            test_dict[prev_order] = full_order
            prev_order = x[0]
            full_order = [x[1]]
        else:
            full_order.append(x[1])
        if i % 10000 == 0:
            print(i)
    test_dict[prev_order] = full_order
    prev_order = '0'
    full_order = []
    print("test")
    with open(orders_path, 'r') as organize:
        test_order = []
        for line in organize.readlines():
            test_order.append(line.split(',')[0])
    with open(prev_prior_path, 'r') as ppp:
        pppr = ppp.readlines()
    print("ready")
    for i, line in enumerate(pppr):
        x = line.split(",")[:2]
        if x[0] != prev_order:
            if prev_order in test_order:
                test_dict[prev_order] = full_order
            prev_order = x[0]
            full_order = [x[1]]
        else:
            full_order.append(x[1])
        if i % 10000 == 0:
            print(i)
    if prev_order in test_order:
        test_dict[prev_order] = full_order
    print("done")
    with open(new_test_path, 'w') as ntp:
        json.dump(test_dict, ntp)


def parse_run_csv(path: str):
    with open(path, 'r') as file:
        data = list(csv.reader(file))
    return data
