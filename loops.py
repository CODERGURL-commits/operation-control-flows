counter = 1
while counter <= 10:
    print(counter)
    counter += 1

# sometimes function is not needed in while loops.


def main_menu():
    user_choice = ""
    while user_choice.lower() != "quit":
        user_choice = input("Enter a command: ")
        print(f"Executing {user_choice}...")


# call the function main menu
main_menu()

# solved the bug in the code below, the condition is false so the loop will not execute.
num = 1
while num > 10:
    print(num)
    num = num + 2
