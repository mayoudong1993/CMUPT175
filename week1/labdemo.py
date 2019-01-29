infile = open('earthquake.txt', 'r')
alist = infile.read().splitlines()
blist = []
print(alist)
for item in alist:
    blist.append(item.split(" "))
print(blist)
adict ={}
for value in blist:
    location = value[-1]
    if location in adict.keys():
        adict[location].append([value[1], value[0]])
    else:
        adict[location] = [[value[1], value[0]]]
print(adict.keys())

output = []
for k in adict:
    list = [k]
    list.extend(adict[k])
    print(list)


print(adict)

#['ALASKA': ['2006/10/19', '2.8'], ['2006/10/18', '2.6'], ['2006/10/18', '2.7'], ['2006/10/18', '2.7'], ['2006/10/18', '2.8']]