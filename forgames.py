# hangman
word = "python"
hidden = ["_"]*len(word)

for attempt in range(6):
    guess = input("Guess a letter: ")
    for i in range(len(word)):
        if word[i]==guess:  
            hidden[i]=guess
    print(" ".join(hidden))
    if "_" not in hidden:
        print("You Win!")
        break



