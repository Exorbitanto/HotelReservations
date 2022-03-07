
class UserInterface:
    def __init__(self):
        pass

    def ShowAvailableActions(self):
        print("1. Log into the system.")
        print("2. Restore lost password.")
        print("3. Create a new account.")
        action = 0
        authorized = False
        try_again = "Y"
        while action < 1 or action > 3:
            action = numeric_tools.get_int_input("Welcome! What would you like to do next? (1-3): ")