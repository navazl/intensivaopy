class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    
    def describe_restaurant(self):
        print(f'O nome do restaurante é: {self.restaurant_name}.')
        print(f'O tipo de cozinha é: {self.cuisine_type}.')
    
    def open_restaurant(self):
        print(f'O {self.restaurant_name} está aberto.')

restaurant1 = Restaurant('Corinthians', 'Brasileira')
restaurant2 = Restaurant("Mc Donald's", 'Americano')
restaurant3 = Restaurant("Bob's", 'Russo')
restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()

