game_title = "MAGIC NUMBER GAME"
print("-"*50, game_title, "-"*50)
print("There is a number between 1 and 10. Can you guess it?")

magic_number = 5

user_guess = input("Your guess?")
while user_guess != magic_number:
    print("Wrong guess :( Try again.")
    user_guess = input("Your guess?")


print("-" * (102 + len(game_title)) )