import json


def users_and_products(orders: str, purchases: str, products: list, product: str):
    user_ids = []
    time_stamps = [0,0,0,0,0,0,0,0,0,0,0,0]
    cur_user = 1
    bought = False
    with open(purchases) as p:
        pur = json.load(p)
    print("pur made")
    with open(orders) as o:
        order = o.readlines()
    print("order made")
    n_order = []
    for i, line in enumerate(order):
        x = line.split(',')
        if int(x[1]) != cur_user:
            if bought:
                user_ids.append(cur_user)
            cur_user = int(x[1])
            bought = False
        for prod in pur[x[0]]:
            if prod in products:
                x[2] = "true"
                bought = True
                break
            x[2] = "false"
        if x[5] == '00' or x[5] == '01':
            x[5] = '0-1'
            time_stamps[0] += 1
        elif x[5] == '02' or x[5] == '03':
            x[5] = '2-3'
            time_stamps[1] += 1
        elif x[5] == '04' or x[5] == '05':
            x[5] = '4-5'
            time_stamps[2] += 1
        elif x[5] == '06' or x[5] == '07':
            x[5] = '6-7'
            time_stamps[3] += 1
        elif x[5] == '08' or x[5] == '09':
            x[5] = '8-9'
            time_stamps[4] += 1
        elif x[5] == '10' or x[5] == '11':
            x[5] = '10-11'
            time_stamps[5] += 1
        elif x[5] == '12' or x[5] == '13':
            x[5] = '12-13'
            time_stamps[6] += 1
        elif x[5] == '14' or x[5] == '15':
            x[5] = '14-15'
            time_stamps[7] += 1
        elif x[5] == '16' or x[5] == '17':
            x[5] = '16-17'
            time_stamps[8] += 1
        elif x[5] == '18' or x[5] == '19':
            x[5] = '18-19'
            time_stamps[9] += 1
        elif x[5] == '20' or x[5] == '21':
            x[5] = '20-21'
            time_stamps[10] += 1
        elif x[5] == '22' or x[5] == '23':
            x[5] = '22-23'
            time_stamps[11] += 1
        if i%10000 == 0:
            print(i)
        line = ",".join(x)
        n_order.append(line)
    if bought:
        user_ids.append(cur_user)
    n_path = orders.split('.')[0] + "_" + product + ".csv"
    with open(n_path, 'w') as n:
        n.writelines(n_order)
    print('whole')
    b_order = []
    for i, line in enumerate(n_order):
        x = line.split(',')
        if int(x[1]) in user_ids:
            b_order.append(line)
        if i%10000 == 0:
            print(i)
    b_path = orders.split('.')[0] + "_" + product + "_bought.csv"
    with open(b_path, 'w') as b:
        b.writelines(b_order)
    print('bought')