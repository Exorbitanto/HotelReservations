from my_library import numeric_tools
from UsersService import UsersService




if action == 1: #trying to authorize user
    while try_again == "Y":
        login = input("Please enter your account login: ")
        password = input("Please enter your account password: ")
        authorized = UsersService.VerifyUserCredentials(login, password)
        if authorized == False:
            try_again = input("Access denied. Do you want to try again? (Y or N): ").upper()
        else:
            try_again = "N"
            print(f"You have been successfully authorized, welcome {login}")

elif action == 3: #trying to create a user
    login = input("Please enter your account login: ")
    password = input("Please enter your account password: ")
    secret_question = input("Please enter your secret question: ")
    answer_to_secret_question = input("Please enter your answer to the secret question: ")
    user_created = UsersService.CreateNewUser(login, password, secret_question, answer_to_secret_question)
    if user_created:
        print("The user has been created successfully.")