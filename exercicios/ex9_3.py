class User():
    def __init__(self, first_name, last_name, age, gender):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender
    
    def describe_user(self):
        print(f'Name: {self.first_name} {self.last_name}')
        print(f'Age: {self.age}')
        print(f'Gender: {self.gender}')
        print('=' * 30)
    
    def greet_user(self):
        print(f'Welcome, {self.first_name}!')


user1 = User('Rodrigo', 'Navarro', 16, 'male')
user2 = User('Felipe', 'Holanda', 19, 'male')
user3 = User('Julia', 'Almeida', 15, 'female')
user4 = User('Mariana', 'Ferraz', 16, 'female')
User.describe_user(user1)
User.describe_user(user2)
User.describe_user(user3)
User.describe_user(user4)