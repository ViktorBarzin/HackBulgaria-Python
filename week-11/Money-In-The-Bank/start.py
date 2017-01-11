import sql_manager as db_manager
from getpass import getpass


sql_manager = db_manager.Db_Manager()


def main_menu():
    global sql_manager
    print("Welcome to our bank service. You are not logged in. \nPlease register or login")
    while True:
        command = input("$$$>")

        if command == 'register':
            username = input("Enter your username: ")
            password = getpass("Enter your password: ")

            if sql_manager.register(username, password):
                print("Registration Successfull")
            else:
                print('Password does not meet requirements!')

        elif command == 'login':
            username = input("Enter your username: ")
            password = getpass("Enter your password: ")

            logged_user = sql_manager.login(username=username, password=password)

            if logged_user:
                logged_menu(logged_user)
            else:
                print("Login failed")

        elif command == 'help':
            print("login - for logging in!")
            print("register - for creating new account!")
            print("exit - for closing program!")

        elif command == 'exit':
            break
        else:
            print("Not a valid command")


def logged_menu(logged_user):
    global sql_manager
    print("Welcome you are logged in as: " + logged_user.get_username())
    while True:
        command = input("Logged>>")

        if command == 'info':
            print("You are: " + logged_user.get_username())
            print("Your id is: " + str(logged_user.get_id()))
            print("Your balance is:" + str(logged_user.get_balance()) + '$')

        elif command == 'changepass':
            new_pass = getpass("Enter your new password: ")
            sql_manager.change_pass(new_pass, logged_user)

        elif command == 'change-message':
            new_message = input("Enter your new message: ")
            sql_manager.change_message(new_message, logged_user)

        elif command == 'show-message':
            print(logged_user.get_message())

        elif command == 'help':
            print("info - for showing account info")
            print("changepass - for changing passowrd")
            print("change-message - for changing users message")
            print("show-message - for showing users message")


def main():
    # sql_manager.create_clients_table()
    main_menu()


if __name__ == '__main__':
    main()
