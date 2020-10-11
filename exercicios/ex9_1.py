class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    
    def describe_restaurant(self):
        print(f'O nome do restaurante é: {self.restaurant_name}.')
        print(f'O tipo de cozinha é: {self.cuisine_type}.')
    
    def open_restaurant(self):
        print(f'O {self.restaurant_name} está aberto.')

restaurant = Restaurant('Corinthians', 'Brasileira')
restaurant.describe_restaurant()
restaurant.open_restaurant()