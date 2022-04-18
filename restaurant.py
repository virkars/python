class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        msg = f"{self.restaurant_name} serves {self.cuisine_type}"
        print(f"{msg}")

    def open_restaurant(self):
        msg = f"{self.restaurant_name} is open. Please come in!"
        print(f"\n{msg}")

    def set_number_served(self, number_served):
        self.number_served = number_served

    def increment_number_served(self, update_number_served):
        self.number_served += update_number_served


restaurant = Restaurant("Royal India", "Indian")
restaurant.describe_restaurant()

print(f"\nNumber served: {restaurant.number_served}")

#restaurant.number_served = 10

restaurant.set_number_served(10)
print(f"Number served: {restaurant.number_served}")

restaurant.increment_number_served(30)
print(f"Number served: {restaurant.number_served}")

