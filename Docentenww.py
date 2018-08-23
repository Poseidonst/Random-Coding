alphabet = [i for i in "abcdefghijklmnopqrstuvwxyz"]
wordslist = []

with open("Docentenwwfile.txt", "r") as f:
    line = f.readline()
    wordslist.append(line[0:4].lower())
    while line:
        line = f.readline()
        wordslist.append(line[0:4].lower())


def make_password():
    counter = 0
    for i in range(0, 26):
        first = i
        for i in range(0, 26):
            second = i
            for i in range(0, 26):
                third = i
                for i in range(0, 26):
                    fourth = i
                    word = "%s%s%s%s" %(alphabet[first], alphabet[second], alphabet[third], alphabet[fourth])
                    if word in wordslist:
                        print(word)
                        counter += 1
    print (counter)

make_password()

#456976 outcomes
