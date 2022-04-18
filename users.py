class User:

    def __init__(self, first_name, last_name, username, email, location):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email
        self.location = location
        self.login_attempts = 0

    def describe_user(self):
        print(f"{self.first_name} {self.last_name}")
        print(f"Username: {self.username}")
        print(f"Email: {self.email}")
        print(f"Location: {self.location}")

    def greet_user(self):
        print(f"\nHi, welcome to my profile")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


john = User("john", "Smith", "jsmith", "jsmith@email.com", "Canada")
john.describe_user()
john.greet_user()

# deff = User("deff", "singh", "dsingh", "dsingh@email.com", "Australia")
# deff.describe_user()
# deff.greet_user()

print("\nMaking 3 login attempts...")
john.increment_login_attempts()
john.increment_login_attempts()
john.increment_login_attempts()
print(f"\nLogin attempts: {john.login_attempts}")

john.reset_login_attempts()
print(f"\nLogin attempts: {john.login_attempts}")