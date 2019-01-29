def calculatedue(dict):
    totalDue = 0
    for data in dict["dues"]:
        totalDue += data[1]
    return totalDue

def generatepaymentstatement(dict):
    statement = ''
    for data in dict["payments"]:
        statement += " %s ($%.2f);" %(data[0], data[1])
    if calculatepayment(dict) > 0:
        return "[$%.2f]%s" % (calculatepayment(dict), statement)
    return ''

def calculatepayment(dict):
    totalPayment = 0
    for data in dict["payments"]:
        totalPayment += data[1]
    return totalPayment

def standardformat(phonenumber):
    return "(" + phonenumber[0:3] + ") " + phonenumber[3: 6] + " " + phonenumber[6: 10]

def main():
    familiesfile = open('families.txt', 'r')
    familieslist = []
    for line in familiesfile:
        line = line.strip('\n')
        familieslist.append(line.split(','))

    duesfile = open('dues.txt', 'r')
    dueslist = []
    for line in duesfile:
        line = line.strip('\n')
        dueslist.append(line.split(';'))

    paymentsfile = open('payments.txt', 'r')
    paymentslist = []
    for line in paymentsfile:
        line = line.strip('\n')
        paymentslist.append(line.split(';'))

    print(familieslist)
    print(dueslist)
    print(paymentslist)

    accountbook = []
    accountdict = {}
    accountbook.sort()
    for family in familieslist:
        number = family[0]
        accountbook.append(number)
        accountdict[number] = {'name': family[1], 'payments': [], 'dues': []}

    for due in dueslist:
        number = due[2]
        accountdict[number]['dues'].append([due[0], float(due[1])])

    for payment in paymentslist:
        number = payment[2]
        accountdict[number]['payments'].append([payment[0], float(payment[1])])

    print("+--------------+------------------+--------+-----+")
    print("| Phone Number | Name             | Due    | Int |")
    print("+--------------+------------------+--------+-----+")

    sumdue = 0
    sumint = 0
    for number in accountbook:
        totaldue = calculatedue(accountdict[number])
        totalpayment = calculatepayment(accountdict[number])
        sumdue += (totaldue - totalpayment)
        paymentstatement = generatepaymentstatement(accountdict[number])
        if totaldue - totalpayment >= 500:
            formatednumber = standardformat(number)
            print("|%s|%-18s|$%7.2f|$%4.2f|%s" %(formatednumber, '**' + accountdict[number]['name'], totaldue - totalpayment, (totaldue - totalpayment) * 0.01, paymentstatement))
        elif totaldue - totalpayment >= 100:
            formatednumber = standardformat(number)
            print("|%s|%-18s|$%7.2f|$%4.2f|%s" %(formatednumber, accountdict[number]['name'], totaldue - totalpayment, (totaldue - totalpayment) * 0.01, paymentstatement))
        elif totaldue - totalpayment > 0:
            formatednumber = standardformat(number)
            print("|%s|%-18s|$%7.2f|     |%s" %(formatednumber, accountdict[number]['name'], totaldue - totalpayment, paymentstatement))
        else:
            continue

    print("+--------------+------------------+--------+-----+")
    print("| Total Dues   |                $%10.2f|" %sumdue)
    print("+--------------+---------------------------+")
    print("| Total Interes|                  $%8.2f|" %sumint)
    print("+--------------+---------------------------+")


    summary = open('summary.txt', 'w')
    summary.write("")

main()