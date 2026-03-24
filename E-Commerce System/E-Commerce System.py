class Product:
    def __init__(self,name,price):
        self.name = name
        self.price = price
    def __str__(self):
        return self.name

    def get_information(self):
        print( f"Product: {self.name}, Price: {self.price}")

class Client:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.cart = []  # Initializes an empty list for each new client

    def add_to_cart(self, product):
        """Adds a Product object to the client's shopping cart."""
        self.cart.append(product)

    def compute_total(self):
        """Calculates and returns the sum of all product prices in the cart."""
        total = 0
        for item in self.cart:
            total += item.price
        return total

class VIPClient(Client):
    def __init__(self, name, email, discount):
        # super() calls the constructor of the parent Client class
        super().__init__(name, email)
        self.discount = discount  # percentage (e.g., 20)

    # Polymorphism: Overriding the parent method
    def compute_total(self):
        standard_total = super().compute_total()
        # Applying the discount: Total * (1 - discount/100)
        discounted_total = standard_total * (1 - self.discount / 100)
        return discounted_total


p1 = Product("Laptop", 1200)
p2 = Product("Chair", 90)
p3 = Product("Scarf", 24)

alice = VIPClient("Alice", "alice@vip.com", 20)
alice.add_to_cart(p1)
alice.add_to_cart(p3)

paul = Client("Paul", "paul@example.com")
paul.add_to_cart(p2)
paul.add_to_cart(p3)

print(f"Customer (VIP): {alice.name}")
print(f"Total to pay: {alice.compute_total()}")

print(f"Customer: {paul.name}")
print(f"Total to pay: {paul.compute_total()}")