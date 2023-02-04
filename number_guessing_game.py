import random
print("HELLO")
top_of_range=input('Type a number: ' )
if top_of_range.isdigit():
    top_of_range = int(top_of_range)
    if top_of_range <= 0:
        print('pls type a number greater than 0')
        quit()
else:
    print('pls type a number next time')
    quit()

random_number = random.randint(0, top_of_range)
guesses=0

while True:
    guesses += 1
    user_guess= input("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    
    else:
        print('pls type a number next time')
        continue
    if user_guess==random_number:
        print("YOU GOT IT")
        break
    else:
        if user_guess>random_number:
            print('you were above the number')
        else:
            print('you were below the bumber')
print(guesses,'guesses')
    
    
