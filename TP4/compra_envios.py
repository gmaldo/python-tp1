from functools import reduce
from abc import ABC, abstractmethod
import json
import os
from typing import List #menor a python 3.9


class Product:
    """
    Represents a product with a name and price.
    
    Attributes:
        name (str): The name of the product.
        price (float): The price of the product.
    """
    
    def __init__(self, name: str, price: float) -> None:
        """
        Initialize a product with name and price.
        
        Args:
            name (str): The name of the product.
            price (float): The price of the product.
        """
        self.name = name
        self.price = price


# Abstract class for shipping methods
class ShippingMethod(ABC):
    """
    Abstract base class for different shipping methods.
    
    This class defines the interface that all shipping methods must implement.
    """
    
    @abstractmethod
    def calculate_cost(self, distance_km: float) -> float:
        """
        Calculate the shipping cost based on distance.
        
        Args:
            distance_km (float): Distance in kilometers.
            
        Returns:
            float: The shipping cost.
        """
        pass

    @abstractmethod
    def delivery_time(self) -> str:
        """
        Get the estimated delivery time for this shipping method.
        
        Returns:
            str: A string describing the delivery time.
        """
        pass

class StandardShipping(ShippingMethod):
    """
    Standard shipping method with fixed cost and longer delivery time.
    
    This is the most economical shipping option with a fixed cost regardless of distance.
    """
    
    def calculate_cost(self, distance_km: float) -> float:
        """
        Calculate shipping cost for standard shipping.
        
        Args:
            distance_km (float): Distance in kilometers (not used for standard shipping).
            
        Returns:
            float: Fixed cost of 5000.
        """
        return 5000  # Fixed economic cost

    def delivery_time(self) -> str:
        """
        Get delivery time for standard shipping.
        
        Returns:
            str: Delivery time estimate.
        """
        return "5-7 business days"
    
    def __str__(self) -> str:
        return "Standard Shipping - Economic option with fixed cost of $5,000"


class ExpressShipping(ShippingMethod):
    """
    Express shipping method with higher fixed cost but faster delivery.
    
    This shipping option prioritizes speed over cost with guaranteed fast delivery.
    """
    
    def calculate_cost(self, distance_km: float) -> float:
        """
        Calculate shipping cost for express shipping.
        
        Args:
            distance_km (float): Distance in kilometers (not used for express shipping).
            
        Returns:
            float: Fixed cost of 15000.
        """
        return 15000  # Fixed higher cost

    def delivery_time(self) -> str:
        """
        Get delivery time for express shipping.
        
        Returns:
            str: Delivery time estimate.
        """
        return "1-2 business days"
    
    def __str__(self) -> str:
        return "Express Shipping - Fast delivery with fixed cost of $15,000"


class CustomShipping(ShippingMethod):
    """
    Custom shipping method with variable cost based on distance.
    
    This shipping option calculates cost using a base fee plus a rate per kilometer.
    """
    
    def calculate_cost(self, distance_km: float) -> float:
        """
        Calculate shipping cost based on distance.
        
        Args:
            distance_km (float): Distance in kilometers.
            
        Returns:
            float: Total shipping cost (base + distance rate).
        """
        base = 10000
        variable_rate = 500  # Rate per km
        return base + variable_rate * distance_km

    def delivery_time(self) -> str:
        """
        Get delivery time for custom shipping.
        
        Returns:
            str: Delivery time estimate that varies with distance.
        """
        return "2-4 business days, depending on distance"
    
    def __str__(self) -> str:
        return "Custom Shipping - Variable cost based on distance ($10,000 base + $500/km)"

class Order:
    """
    Represents an order containing products and shipping information.
    
    Attributes:
        products (List[Product]): List of products in the order.
        shipping_method (ShippingMethod): The chosen shipping method.
        distance_km (float): Distance for shipping calculation.
    """
    
    def __init__(self, products: List[Product], shipping_method: ShippingMethod, distance_km: float = 0) -> None:
        """
        Initialize an order with products and shipping details.
        
        Args:
            products (List[Product]): List of products to order.
            shipping_method (ShippingMethod): The shipping method to use.
            distance_km (float, optional): Distance in kilometers. Defaults to 0.
        """
        self.products = products
        self.shipping_method = shipping_method
        self.distance_km = distance_km
    
    def order_price(self) -> float:
        """
        Calculate the total price of all products in the order.
        
        Returns:
            float: Sum of all product prices.
        """
        return reduce(lambda acc, prod: acc + prod.price, self.products, 0)

    def shipping_cost(self) -> float:
        """
        Calculate the shipping cost using the selected shipping method.
        
        Returns:
            float: The shipping cost.
        """
        return self.shipping_method.calculate_cost(self.distance_km)

    def calculate_total_cost(self) -> float:
        """
        Calculate the total cost including products and shipping.
        
        Returns:
            float: Total order cost (products + shipping).
        """
        return self.order_price() + self.shipping_cost()

    def delivery_time(self) -> str:
        """
        Get the estimated delivery time from the shipping method.
        
        Returns:
            str: Estimated delivery time.
        """
        return self.shipping_method.delivery_time()
    
    def __str__(self) -> str:
        """
        String representation of the order with all details.
        
        Returns:
            str: Formatted order information.
        """
        products_str = ", ".join([f"{prod.name} (${prod.price})" for prod in self.products])
        return (f"Order: {products_str} | "
                f"Shipping: {str(self.shipping_method)} | "
                f"Products cost: ${self.order_price()} | "
                f"Shipping cost: ${self.shipping_cost()} | "
                f"Total: ${self.calculate_total_cost()} | "
                f"Estimated time: {self.delivery_time()}")
    
    @staticmethod
    def save_order_to_file(order: 'Order', filename: str = "orders.json") -> None:
        """
        Save an order to a JSON file.
        
        This method serializes the order data and appends it to a JSON file,
        creating the file if it doesn't exist.
        
        Args:
            order (Order): The order to save.
            filename (str, optional): The filename to save to. Defaults to "orders.json".
        """
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
def main() -> None:
    """
    Main function to demonstrate the purchase and shipping system.
    
    This function creates sample products, shipping methods, and orders
    to showcase the functionality of the system.
    """
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
    order2 = Order([keyboard], express, distance_km=5)
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
        """
        Drone shipping method for ultra-fast delivery.
        
        This shipping method uses drones for rapid delivery with tiered pricing
        based on distance.
        """
        
        def calculate_cost(self, distance_km: float) -> float:
            """
            Calculate drone shipping cost with tiered pricing.
            
            Args:
                distance_km (float): Distance in kilometers.
                
            Returns:
                float: Shipping cost (25000 for ≤10km, +5000/km after).
            """
            return 25000 if distance_km <= 10 else 25000 + (distance_km - 10) * 5000
        
        def delivery_time(self) -> str:
            """
            Get delivery time for drone shipping.
            
            Returns:
                str: Ultra-fast delivery time.
            """
            return "2-4 hours"
        
        def __str__(self) -> str:
            return "Drone Shipping - Ultra-fast delivery ($25000 up to 10km, +$5000/km after)"
    
    print("\n5. New method: Drone shipping")
    drone = DroneShipping()
    print(f"* {drone}")
    drone_order = Order([mouse], drone, distance_km=15)
    print(drone_order)
    Order.save_order_to_file(drone_order)
    print("> New method integrated without modifying existing code")

main()