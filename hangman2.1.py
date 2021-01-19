import random
import string


def legal(y):
    if len(y) != 1:
        print("You should input a single letter")
        return False
    elif y not in string.ascii_lowercase:
        print("Please enter a lowercase English letter")
        return False
    else:
        return True

print("H A N G M A N")
word = random.choice(["python", "java", "kotlin", "javascript"])
lives = 8
display = ["-" for _ in word]
victory = False
while lives > 0:
    print()
    print("".join(display))
    guess = False
    first = True
    while True:
        guess = input("Input a letter: ")
        if legal(guess):
            break
    if guess in set(word):
        if guess in display:
            print("No improvements")
        else:
            clock = 0
            for n in word:
                if guess == n:
                    display[clock] = guess
                clock += 1
            if "-" not in display:
                victory = True
                break
    else:
        print("That letter doesn't appear in the word")
        lives -= 1
if victory == False:
    print("You lost!")
else:
    print("""You guessed the word!
You survived!""")
