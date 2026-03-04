import random

words = ["python", "java", "hangman", "coding", "program"]
word = random.choice(words)
guessed_letters = []
chances = 6

print("Welcome to Hangman Game!")
print("Guess the word, one letter at a time.")

while chances > 0:
    display_word = ""
    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "
    
    print("\nWord:", display_word)
    print("Chances left:", chances)

    if "_" not in display_word:
        print("Congratulations!! You guessed the word correctly.")
        break
    guess = input("Enter a letter: ").lower()
    if guess in guessed_letters:
        print("You already guessed that letter...")
        continue
    guessed_letters.append(guess)
    if guess not in word:
        chances -= 1
        print("Wrong guess!")
if chances == 0:
    print("\nGame Over!")
    print("The word was:", word)
