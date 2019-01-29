def decode(key, ciphertext):
    str = ''
    charstring = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for char in ciphertext:
        index = charstring.find(char)
        index -= key
        str += charstring[index]
        #str += chr((ord(char) - 65 - key) % 26 + 65)
    return str

def main():
    print("[evaluate codebreaker]")
    inputfile = input("Enter the input filename: ")
    infile = open(inputfile, 'r')
    for line in infile:
        line = line.strip('\n')
        data = line.split(" ")
        if len(data) == 2:
            print(decode(int(data[0]), data[1]))
        else:
            print("Missing text!")

main()