def main():
    alist = [1, 2, 3]
    blist = [4, 5, 6]
    clist = [7, 8, 9]
    atotal = 0
    for number in alist:
        atotal += number

    btotal = 0
    for number in blist:
        btotal += number

    ctotal = 0
    for number in clist:
        ctotal += number


    ctotal = sum(clist)
#作用：求所有数之和
#输入 A list of number
#输出 所有数之和
def sum(numberlist):

    #通常我们要初始化 我们的输出值
    total = 0
    for number in numberlist:
        total += number

    return total

main()