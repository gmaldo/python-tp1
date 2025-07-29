class Hand():
    """
    Represents a hand with a maximum weight capacity.
    
    Attributes:
        max_weight (float): Maximum weight the hand can hold in kg.
    """
    
    def __init__(self, max_weight: float) -> None:
        """
        Initialize a hand with a maximum weight capacity.
        
        Args:
            max_weight (float): Maximum weight the hand can hold in kg.
        """
        self.max_weight = max_weight

    def can_hold(self, item_weight: float) -> bool:
        """
        Check if the hand can hold an object of given weight.
        
        Args:
            item_weight (float): Weight of the object in kg.
            
        Returns:
            bool: True if the hand can hold the object, False otherwise.
        """
        return item_weight <= self.max_weight

class Person:
    """
    Represents a person with two hands and total lifting strength.
    
    Attributes:
        left_hand (Hand): The person's left hand.
        right_hand (Hand): The person's right hand.
        total_strength (float): Combined maximum weight capacity of both hands.
    """
    
    def __init__(self, left_hand: Hand, right_hand: Hand) -> None:
        """
        Initialize a person with two hands.
        
        Args:
            left_hand (Hand): The person's left hand.
            right_hand (Hand): The person's right hand.
        """
        self.left_hand = left_hand
        self.right_hand = right_hand
        self.total_strength = left_hand.max_weight + right_hand.max_weight
    
    def can_lift(self, item_weight: float) -> str:
        """
        Determine if the person can lift an object and how.
        
        Args:
            item_weight (float): Weight of the object in kg.
            
        Returns:
            str: Description of how the object can be lifted:
                - "With one hand" if either hand can hold it alone
                - "With both hands" if both hands are needed but total strength allows it
                - "Cannot lift it" if the object exceeds total strength
        """
        if self.left_hand.can_hold(item_weight) or self.right_hand.can_hold(item_weight):
            return "With one hand"
        elif item_weight <= self.total_strength:
            return "With both hands"
        else:
            return "Cannot lift it"
    
# Test cases
def main():
    # Create hands with different capacities
    left_hand = Hand(10)  # Can hold up to 10kg
    right_hand = Hand(15)    # Can hold up to 15kg
    
    # Create person
    person = Person(left_hand, right_hand)
    
    print(f"Person's total strength: {person.total_strength}kg")
    print()
    
    # Test cases
    objects = [5, 12, 20, 30]
    
    for weight in objects:
        result = person.can_lift(weight)
        print(f"Object of {weight}kg: {result}")

main()