import random


print("H A N G M A N")
print()
word = random.choice(["python", "java", "kotlin", "javascript"])
clock = 0
display = ["-" for _ in word]
while clock < 8:
    print("".join(display))
    guess = input("Input a letter: ")
    if guess in set(word):
        clock2 = 0
        for n in word:
            if guess == n:
                display[clock2] = guess
            clock2 += 1
    else:
        print("That letter doesn't appear in the word")
    print()
    clock += 1
print("""
Thanks for playing!
We'll see how well you did in the next stage""")
