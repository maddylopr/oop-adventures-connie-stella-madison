import random

# Character class
class Character:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def attack(self, opponent):
        damage = random.randint(10, 20)  # Random damage between 5 and 15
        print(f"{self.name} attacks {opponent.name} and deals {damage} damage!")
        opponent.health -= damage

    def heal(self):
        heal_amount = random.randint(5, 20)
        self.health += heal_amount
        print(f"{self.name} heals for {heal_amount} health!")

    def is_alive(self):
        return self.health > 0

# Playable game loop
def game():
    # Create characters
    hero = Character(input("Enter your hero's name: "), 100)
    villain = Character("evil kortnee", 150)

    print(f"\nWelcome, {hero.name}! You are about to face {villain.name}!")
    while hero.is_alive() and villain.is_alive():
        print(f"\n{hero.name}'s health: {hero.health} | {villain.name}'s health: {villain.health}\n")
        
        # Player's turn
        print("Choose your action:")
        print("1. Attack")
        print("2. Heal")
        choice = input("Enter the number of your choice: ")

        if choice == "1":
            hero.attack(villain)
        elif choice == "2":
            hero.heal()
        else:
            print("Invalid choice! You lose your turn.")
        
        # Check if villain is still alive
        if villain.is_alive():
            villain.attack(hero)  # Villain attacks hero

    # Decide the winner
    if hero.is_alive():
        print(f"\nCongratulations! {hero.name} defeated {villain.name}!")
    else:
        print(f"\n{villain.name} has defeated you. Better luck next time!")

    # Replay option
    if input("\nDo you want to play again? (yes/no): ").lower() == "yes":
        game()

# Start the game
game()
