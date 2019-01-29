infile = open('earthquake.txt', 'r')
alist = infile.read().splitlines()
blist = []
for list in alist:
    blist.append(list.split(' '))
print(blist)
adict = {}
for value in blist:
    if value[-1] in adict.keys():
        adict[value[-1]].append([value[1], value[0]])
    else:
        adict[value[-1]] = [[value[1], value[0]]]
print(adict)
output = []
for k in adict:
    list = [k]
    list.extend(adict[k])
    print(list)
