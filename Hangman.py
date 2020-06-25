lives = 6

def guess(word,lyst):
    global lives
    known_letters = lyst
    check = 0
    word = word.lower()
    guesses = input("Enter a letter to guess: ")
    if guesses in known_letters:
        print("You already guessed that!")
    elif guesses in word:
        print(f'Correct!')
        for x in word:
            if x == guesses:
                print(guesses,end='')
            elif x in known_letters:
                print(x,end='')
            else:
                print('#',end='')
        print('\n')
        known_letters.append(guesses)
    else:
        print("Incorrect")
        lives -= 1
        if lives == 0:
            print("You died")
            quit()
        else:
            print(f'You have {lives} lives left')
                 
    for letter in word:
        if letter in known_letters:
            check +=  1
    if check == len(word):
        print("You win!")
    else:  
        guess(word,known_letters)
            
def main():
    print("Welcome to Hangman! Guess the word, but don't let the man die! You have six lives")
    word = input("Enter a word to guess: ")
    for _ in range(100):
        print('------------------------')
    guess(word,[])
  
    
if __name__ == "__main__":    
    main()

