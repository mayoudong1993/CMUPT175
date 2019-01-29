import operator
def read_data_from_file(filename, symbol):
    file = open(filename, 'r')
    flist = []
    for line in file:
        line = line.strip('\n')
        flist.append(line.split(symbol))
    return flist

class Customer:
    def __init__(self, name, phoneNumber):
        self.name = name
        self.phoneNumber = phoneNumber
        self.payments =[]
        self.dues = []

    def __gt__(self, other):
        return self.phoneNumber > other.phoneNumber

    def __str__(self):
        return "|%s|%-18s|$%7.2f|$%4.2f|%s" %("(***) *** ****", self.name, self.totalDues() - self.totalPayments(), (self.totalDues() - self.totalPayments()) * 0.01, self.paymentStatement())

    def addPayment(self, payment):
        self.payments.append(payment)
        return

    def addDue(self, payment):
        return

    def totalPayments(self):
        return 0

    def totalDues(self):
        return 100
    def interest(self):
        return

    def paymentStatement(self):
        return "HHH"

    def formatPhonenumber(self):
        return

    def realname(self):
        if (self.totalDues() - self.totalPayments()) > 500:
            self.name = "**" + self.name
            self.name = self.name[0:17]


def main():
    #读取 families
    families = read_data_from_file('families.txt', ',')
    #读取 dues
    dues = read_data_from_file('dues.txt', ';')
    #读取 payments
    payments = read_data_from_file('payments.txt', ';')
    print(families)
    customerList = []
    for [phonenumber, name, address] in families:
        customerList.append(Customer(name, phonenumber))
    #customerList.sort(key = operator.attrgetter('phoneNumber'))
    customerList.sort()
    for customer in customerList:
        print(customer)

main()