from random import randint

def draw_hangman(x):
    hangman_list = ["  ____", " |    | ", " |    ", " |   ", " |    ", " |   ", "_|_"]
    if x == 1:
        hangman_list[2] = " |    o"
    elif x == 2:
        hangman_list[2] = " |    o"
        hangman_list[3] = " |    |"
        hangman_list[4] = " |    |"
    elif x == 3:
        hangman_list[2] = " |    o"
        hangman_list[3] = " |    |\\"
        hangman_list[4] = " |    |"
    elif x == 4:
        hangman_list[2] = " |    o"
        hangman_list[3] = " |   /|\\"
        hangman_list[4] = " |    |"
    elif x == 5:
        hangman_list[2] = " |    o"
        hangman_list[3] = " |   /|\\"
        hangman_list[4] = " |    |"
        hangman_list[5] = " |     \\"
    elif x == 6:
        hangman_list[2] = " |    o"
        hangman_list[3] = " |   /|\\"
        hangman_list[4] = " |    |"
        hangman_list[5] = " |   / \\"

    for item in hangman_list:
        print (item)

def pick_word(x):
    with open(x, "r") as f:
        lines = f.readlines()
    return (lines[randint(0, len(lines))].strip())

def guess_letters(word):
    print("Welcome to Hangman!")
    word = word.upper()
    print ("_ " * len(word))
    print ("")
    word_list = list(word)
    guess_list = []
    wrong_guess_list = []
    iteration_list = [i for i in range(0, (len(word_list)))]
    lenmin = int(len(word_list) - 1)
    counter = 0
    while True:
        countwin = 0
        while True:
            guess = str(input("Guess your letter: ")).upper()
            if guess in wrong_guess_list or guess in guess_list:
                print ("You have already guessed that item, please try again")
            else:
                break

        if guess in word:
            print("Correct!")
        else:
            print("Incorrect!")
            counter += 1
        print ("")

        if guess in word:
            guess_list.append(guess)
        else:
            wrong_guess_list.append(guess)

        for item in iteration_list:
            if word_list[item] in guess_list and item != lenmin:
                print(word_list[item], end = " ")
            elif word_list[item] not in guess_list and item != lenmin:
                print("_", end = " ")
            elif word_list[item] not in guess_list and item == lenmin:
                print("_")
            else:
                print(word_list[item])
        print("")

        for item in word_list:
            if item in guess_list:
                countwin += 1

        draw_hangman(counter)

        if countwin == len(word_list):
            print ("Congratulations you have won!")
            break

        if counter == 6:
            print ("You have lost, the word was: " + word)
            break

        if len(wrong_guess_list) >= 1:
            print("These are the letters you have already guessed wrong: " + ", ".join(wrong_guess_list))

guess_letters(pick_word("Dutchwords.txt"))
