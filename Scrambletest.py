clear_text = input("What do you need scrambled?: ").upper()

alphabet_dictionary_number = {"A":1,"B":2,"C":3,"D":4,"E":5,"F":6,"G":7,"H":8,"I":9,"J":10,"K":11,"L":12,"M":13,"N":14,"O":15,"P":16,"Q":17,"R":18,"S":19,"T":20,"U":21,"V":22,"W":23,"X":24,"Y":25,"Z":26}
alphabet_dictionary_cipher = {1:"A",2:"B",3:"C",4:"D",5:"E",6:"F",7:"G",8:"H",9:"I",10:"J",11:"K",12:"L",13:"M",14:"N",15:"O",16:"P",17:"Q",18:"R",19:"S",20:"T",21:"U",22:"V",23:"W",24:"X",25:"Y",26:"Z"}

letter_list = []

for x in clear_text:
    letter_list.append(x)

cipher_list = []
amount_displace = int(input("How many places displaced?: "))

if amount_displace not in range(1, 27):
    print ("That's not in range, it has to be between 1-26")
    amount_displace = int(input("How many places displaced?: "))

def find_letter(n):
    for alphabet in alphabet_dictionary_number:
        if n == alphabet:
            if int(alphabet_dictionary_number[n]) + int(amount_displace) <= 26:
                return int(alphabet_dictionary_number[n]) + int(amount_displace)
            else:
                return int(alphabet_dictionary_number[n]) + int(amount_displace) - 26

def cipher_letter(m):
    for number in alphabet_dictionary_cipher:
        if m == number:
            return alphabet_dictionary_cipher[m]

def total_outcome():
    for cipher in letter_list:
        cipher_list.append(cipher_letter(find_letter(cipher)))

total_outcome()

def make_loose():
    sent_str = ""
    for v in cipher_list:
        sent_str = sent_str + str(v)
    return sent_str

outcome = str(make_loose())

print ("After inserting "+clear_text+" and moving it "+str(amount_displace)+" spaces in the alphabet "+outcome+ " came out!"
)
