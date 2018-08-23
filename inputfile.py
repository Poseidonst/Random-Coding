l = [i ** 2 for i in range(1,11)]

with open("text.txt", "w") as writefile:
    for item in l:
        writefile.write(str(item) + "\n")

with open("text.txt", "r") as readfile:
    print (readfile.read())
