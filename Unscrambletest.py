coded_text = "lwabw".upper()
print (coded_text +" could mean:")
alphabet_dictionary_number = {"A":1,"B":2,"C":3,"D":4,"E":5,"F":6,"G":7,"H":8,"I":9,"J":10,"K":11,"L":12,"M":13,"N":14,"O":15,"P":16,"Q":17,"R":18,"S":19,"T":20,"U":21,"V":22,"W":23,"X":24,"Y":25,"Z":26}
alphabet_dictionary_cipher = {1:"A",2:"B",3:"C",4:"D",5:"E",6:"F",7:"G",8:"H",9:"I",10:"J",11:"K",12:"L",13:"M",14:"N",15:"O",16:"P",17:"Q",18:"R",19:"S",20:"T",21:"U",22:"V",23:"W",24:"X",25:"Y",26:"Z"}

number_list = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
decoded_list = []
empty_list = []
letter_list = []
for x in coded_text:
    letter_list.append(x)

def code(letter_list):
    for letter in letter_list:
        for crypt in alphabet_dictionary_number:
            if letter == crypt:
                for number in number_list:
                    new = (alphabet_dictionary_number[letter] + number)
                    if new <= 26:
                        new = new
                    else:
                        new = new - 26
                    for crypt2 in alphabet_dictionary_cipher:
                        if crypt2 == new:
                            empty_list.append(alphabet_dictionary_cipher[crypt2])
    return empty_list

code(letter_list)

def list_organiser(list):
    other_list = []
    value = 0
    for item in list:
        other_list.append(item)
        value += 1
        if value % 26 == 0:
            print (" ".join(other_list[value-26:value]))



list_organiser(empty_list)
