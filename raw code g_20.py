def prepare(filename : str):
    print('Reading file {}'.format(filename))

    with open(filename) as fr:
        L = []
        for k in fr:
            L.append(k.split(','))

    return L


def stock_stats(stock : str):
    print('Searching min, max, and mean price of stock : {}'.format(stock))
    maxprice = 0
    minprice = 100000
    avgc = 0
    avgs = 0
    meanprice = 0.0
    for k in data:
        if k[0] == stock:
            if int(k[2]) > maxprice:
                maxprice = int(k[2])
            if minprice > int(k[2]):
                minprice = int(k[2])
            avgc += 1
            avgs += int(k[2])
    meanprice = avgs / avgc

    print("Min-price : {}, Mean-Price : {}, Max-Price : {} for stock : {}".format(minprice, meanprice, maxprice, stock))

    # NOTE: please return these value with the following order: min, mean, max
    return minprice, meanprice, maxprice