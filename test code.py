def greet_user(name):
    print(f"Hello, {name}! Welcome to Exercise 6.")

def say_goodbye(name):
    print(f"Goodbye, {name}! Thanks for running the script.")

def main():
    user_name = input("Enter your name: ")
    greet_user(user_name)
    say_goodbye(user_name)

if __name__ == "__main__":
    main()
