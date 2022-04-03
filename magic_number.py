import random

game_title = "MAGIC NUMBER GAME"
try_count = 3
print("-"*50, game_title, "-"*50)
print("There is a number between 1 and 10. Can you guess it?")
print(f"You have {try_count} tries.")

# cast int to string
magic_number = str(random.randint(1, 10))

# remove this from final code
# print(f"MAGIC NUMBER: {magic_number}")

user_guess = input("Your guess?")
while user_guess != magic_number:
    try_count -= 1

    # check try_count == 0
    if try_count == 0:
        break
        # game over

    print(f"Wrong guess :( You have {try_count} tries left.")
    user_guess = input("Your guess?")

# check win condition
if user_guess == magic_number:
    print("You win!")
else:
    print("You lost. Maybe next time.")

print("-" * (102 + len(game_title)) )