from functools import reduce
from abc import ABC, abstractmethod
import json
import os


class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price


# Abstract class for shipping methos
class ShippingMethod(ABC):
    @abstractmethod
    def calculate_cost(self, distance_km):
        pass

    @abstractmethod
    def delivery_time(self):
        pass

class StandardShipping(ShippingMethod):
    def calculate_cost(self, distance_km):
        return 5000  # Fixed economic cost

    def delivery_time(self):
        return "5-7 business days"
    
    def __str__(self):
        return "Standard Shipping - Economic option with fixed cost of $5,000"


class ExpressShipping(ShippingMethod):
    def calculate_cost(self, distance_km):
        return 15000  # Fixed higher cost

    def delivery_time(self):
        return "1-2 business days"
    
    def __str__(self):
        return "Express Shipping - Fast delivery with fixed cost of $15,000"


class CustomShipping(ShippingMethod):
    def calculate_cost(self, distance_km):
        base = 10000
        variable_rate = 500  # Rate per km
        return base + variable_rate * distance_km

    def delivery_time(self):
        return "2-4 business days, depending on distance"
    
    def __str__(self):
        return "Custom Shipping - Variable cost based on distance ($10,000 base + $500/km)"

class Order:
    def __init__(self, products, shipping_method, distance_km=0):
        self.products = products if isinstance(products, list) else [products]
        self.shipping_method = shipping_method
        self.distance_km = distance_km
    
    def order_price(self):
        return reduce(lambda acc, prod: acc + prod.price, self.products, 0)

    def shipping_cost(self):
        return self.shipping_method.calculate_cost(self.distance_km)

    def calculate_total_cost(self):
        return self.order_price() + self.shipping_cost()

    def delivery_time(self):
        return self.shipping_method.delivery_time()
    
    def __str__(self):
        products_str = ", ".join([f"{prod.name} (${prod.price})" for prod in self.products])
        return (f"Order: {products_str} | "
                f"Shipping: {str(self.shipping_method)} | "
                f"Products cost: ${self.order_price()} | "
                f"Shipping cost: ${self.shipping_cost()} | "
                f"Total: ${self.calculate_total_cost()} | "
                f"Estimated time: {self.delivery_time()}")
    
    @staticmethod
    def save_order_to_file(order, filename="orders.json"):
        """Saves the order to a JSON file"""
        order_data = {
            "products": [{"name": prod.name, "price": prod.price} for prod in order.products],
            "shipping_method": str(order.shipping_method),
            "distance_km": order.distance_km,
            "products_cost": order.order_price(),
            "shipping_cost": order.shipping_cost(),
            "total_cost": order.calculate_total_cost(),
            "delivery_time": order.delivery_time()
        }
        
        # Read existing orders or create empty list
        if os.path.exists(filename):
            try:
                with open(filename, 'r', encoding='utf-8') as file:
                    orders = json.load(file)
            except (json.JSONDecodeError, FileNotFoundError):
                orders = []
        else:
            orders = []
        
        # Add new order
        orders.append(order_data)
        
        # Save all orders
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(orders, file, indent=2, ensure_ascii=False)




# Test cases
def main():
    # Create products
    laptop = Product("Gamer Laptop", 2500000)
    mouse = Product("Mouse gamer", 35000)
    keyboard = Product("Mechanical Keyboard", 85000)
    
    # Create shipping methods
    standard = StandardShipping()
    express = ExpressShipping()
    custom = CustomShipping()
    
    print("=== PURCHASE AND SHIPPING SYSTEM ===\n")
    
    # Case 1: Order with standard shipping
    print("1. Order with standard shipping:")
    order1 = Order([laptop, mouse], standard, distance_km=10)
    print(order1)
    Order.save_order_to_file(order1)
    print("> Order saved to file\n")
    
    # Case 2: Order with express shipping
    print("2. Order with express shipping:")
    order2 = Order(keyboard, express, distance_km=5)
    print(order2)
    Order.save_order_to_file(order2)
    print("> Order saved to file\n")
    
    # Case 3: Order with custom shipping (variable distance)
    print("3. Order with custom shipping (50km):")
    order3 = Order([laptop, keyboard, mouse], custom, distance_km=50)
    print(order3)
    Order.save_order_to_file(order3)
    print("> Order saved to file\n")
    
    # Case 4: Cost comparison for the same order
    print("4. Shipping method comparison for the same order:")
    test_products = [laptop, mouse]
    test_distance = 25
    
    for name, method in [("Standard", standard), ("Express", express), ("Custom", custom)]:
        temp_order = Order(test_products, method, test_distance)
        print(f"   {name}: Total ${temp_order.calculate_total_cost()} - {temp_order.delivery_time()}")
    
    print("\n=== SYSTEM EXTENSIBILITY ===")
    print("To add a new shipping method, simply:")
    print("1. Create a new class that inherits from ShippingMethod")
    print("2. Implement calculate_cost() and delivery_time()")
    print("3. The rest of the code works without modifications")
    
    # Example of new shipping class
    class DroneShipping(ShippingMethod):
        def calculate_cost(self, distance_km):
            return 25000 if distance_km <= 10 else 25000 + (distance_km - 10) * 5000
        
        def delivery_time(self):
            return "2-4 hours"
        
        def __str__(self):
            return "Drone Shipping - Ultra-fast delivery ($25000 up to 10km, +$5000/km after)"
    
    print("\n5. New method: Drone shipping")
    drone = DroneShipping()
    print(f"* {drone}")
    drone_order = Order(mouse, drone, distance_km=15)
    print(drone_order)
    Order.save_order_to_file(drone_order)
    print("> New method integrated without modifying existing code")

main()