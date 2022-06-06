import random

with open('wordle.txt') as f:
    for line in f:
        lllibrary = line
        print(lllibrary)

f.close()



wordlist = []
wordlist.append(lllibrary)

for k in range(2315):
    wordright = random.choice(wordlist)

#Code doesn't work rn

p = 0
pp = 6

for bz in range(0,pp):
    guess = input("What is the word? ")
    if guess == wordright:
        print("You got it right")
        break
    for word in wordlist:
        if(guess == word):
            p = p+1
    if(p > 0):
        print("No.")
    else: 
        print("Not a word")
        pp = pp + 1
    p = 0
print("The word was " + wordright)
f.close()
