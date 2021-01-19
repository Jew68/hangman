import random


print("H A N G M A N")
lives = 8
word = random.choice(["python", "java", "kotlin", "javascript"])
display = ["-" for _ in word]
record = []
while True:
    while True:
        print()
        print("".join(display))
        guess = input("Input a letter: ")
        if guess in record:
            print("You've already guessed this letter")
        elif len(guess) != 1:
            print("You should input a single letter")
        elif guess not in list("abcdefghijklmnopqrstuvwxyz"):
            print("Please enter a lowercase English letter")
        else:
            record.append(guess)
            break
    if guess in word:
        clock = 0
        for n in word:
            if guess == n:
                display[clock] = guess
            clock += 1
        if "".join(display) == word:
            print(f"You guessed the word {word}!")
            print("You survived!")
            break
    else:
        print("That letter doesn't appear in the word")
        lives -= 1
        if lives == 0:
            print("You lost!")
            break
        
        
