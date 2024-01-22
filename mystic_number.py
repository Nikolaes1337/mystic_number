import random

mystic_number = random.randint(0, 100)

adventure_question = "Adventurer, are you sure you can guess the Oracle's mystic number? "
print(adventure_question)
adventure_question = input('YES or NO? ').upper()

if adventure_question == 'YES':
    print('You has chosen the path by yourself!')
elif adventure_question == 'NO':
    print("I didn't know you are that scared!")
    last_chance = "Are you sure? "
    print(last_chance)
    last_chance = input("YES or NO? ").upper()
    if last_chance == 'YES':
        raise SystemExit('Be more brave the next time!')
    elif last_chance == 'NO':
        print('You has chosen the path by yourself!')
    else:
        raise SystemExit('Only YES or NO acceptable!!!')

else:
    raise SystemExit('Only YES or NO acceptable!!!')

users_number = int(input("Tell me which number is the mystic one? "))
guess_counter = 0

while users_number != mystic_number:
    guess_counter += 1

    if users_number > mystic_number:
        if users_number - mystic_number < 3:
            users_number = int(input('↓↓↓ You are EXTREMELY close from the mystic number! ↓↓↓ '))
        elif users_number - mystic_number < 10:
            users_number = int(input('↓↓↓ You are UP away from the mystic number! ↓↓↓ '))
        elif users_number - mystic_number < 30:
            users_number = int(input('↓↓↓ You are UP far from the mystic number! ↓↓↓ '))
        else:
            users_number = int(input('↓↓↓ You are not born for these things! ↓↓↓ '))

    elif users_number < mystic_number:
        if mystic_number - users_number < 3:
            users_number = int(input('↑↑↑ You are DOWN away from the mystic number! ↑↑↑ '))
        elif mystic_number - users_number < 10:
            users_number = int(input('↑↑↑ You are DOWN away from the mystic number! ↑↑↑ '))
        elif mystic_number - users_number < 30:
            users_number = int(input('↑↑↑ You are DOWN far from the mystic number! ↑↑↑ '))
        else:
            users_number = int(input('↑↑↑ You are not born for these things! ↑↑↑ '))

if guess_counter == 1:
    print('YOU ARE THE CHOSEN ONE!')
elif guess_counter <= 3:
    print('You are doing GREAT, keep it UP!')
elif guess_counter <= 5:
    print('You have to train your skills but you are good!')
else:
    print('For homework: Do it more often!')

print('Congrats!')
