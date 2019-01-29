def unzip(tuplelist):
    alist = []
    blist = []
    for tuple in tuplelist:
        alist.append(tuple[0])
        blist.append(tuple[1])
    return alist, blist


def main():
    print(unzip([(1, 4), (2, 5), (3, 6)]))
    print(unzip([(1, 2)]))
    print(unzip([('A', 'B'), ('X', 'Y')]))
    print(unzip([]))

main()