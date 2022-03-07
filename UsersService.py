from Users import Users
import json
import hashlib

class UsersService(Users):

    def __init__(self):
        pass

    def __str__(self):
        pass

    @staticmethod
    def CreateNewUser(login, password, secret_question, answer_to_secret_question):
        # try:

            new_user={
                "login" : login,
                "password" : hashlib.md5(password.encode('utf-8')).hexdigest(),
                "secret_question" : secret_question,
                "answer_to_secret_question" : answer_to_secret_question
            }
            existing_users = UsersService._get_users_list()
            existing_users.append(new_user)
            file = open("C:\\Users\\Eugen\\PycharmProjects\\HotelReservations\\Database\\UserCredentials.json", "w+")
            file.write(json.dumps(existing_users))
            file.close()
            return True
        # except Exception:
        #     return False

    @staticmethod
    def RestorePassword(login, answer_to_secret_question):
        pass

    @staticmethod
    def VerifyUserCredentials(login, password):
        users_list = UsersService._get_users_list()
        if len(users_list) > 0:
            for user in users_list:
                if user["login"] == login and user["password"] == hashlib.md5(password.encode('utf-8')).hexdigest():
                    return True
                else:
                    return False
        else:
            return False

    @staticmethod
    def _get_users_list():
        file = open("C:\\Users\\Eugen\\PycharmProjects\\HotelReservations\\Database\\UserCredentials.json", "r")
        data = file.read()
        file.close()
        if data:
            users_list = json.loads(data)
        else:
            users_list = list()
        return users_list
