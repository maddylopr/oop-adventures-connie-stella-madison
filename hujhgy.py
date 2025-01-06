import random

# character class(?)
class Character:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def attack(self, opponent):
        damage = random.randint(7, 50)  # deals random damage between set numbers
        print(f"{self.name} attacks {opponent.name} and deals {damage} damage!")
        opponent.health -= damage

    def heal(self):
        heal_amount = random.randint(10, 50)
        self.health += heal_amount
        print(f"{self.name} heals for {heal_amount} health!")

    def magic(self, opponent):
        damage = random.randint(30, 40)
        print(f"{self.name} casts a spell on {opponent.name} and deals {damage} damage!")
        opponent.health -= damage

    def is_alive(self):
        return self.health > 0

# creates the playable loop for the game
def game():
    # creation of the characters
    hero = Character(input("Enter your hero's name: "), 100)
    villain = Character("evil kortnee", 150)

    print(f"\nWelcome, {hero.name}! You are about to face {villain.name}!")
    while hero.is_alive() and villain.is_alive():
        print(f"\n{hero.name}'s health: {hero.health} | {villain.name}'s health: {villain.health}\n")
        
        # start of players turn
        print("Choose your action:")
        print("1. Attack")
        print("2. Heal")
        print("3. Magic")
        choice = input("Enter the number of your choice: ")

        if choice == "1":
            hero.attack(villain)
        elif choice == "2":
            hero.heal()
        elif choice == "3":
            hero.magic(villain)
        else:
            print("someone had a typo!") 
        
        # ran to check if the villian is alive
        if villain.is_alive():
            villain.attack(hero)  # villian attacks hero

    # in order to decide who is the winner
    if hero.is_alive():
        print(f"\nCongratulations! {hero.name} defeated {villain.name}!")
    else:
        print(f"\n{villain.name} has defeated you. Better luck next time!")

    # replay
    if input("\nDo you want to play again? (yes/no): ").lower() == "yes":
        game()

# runs the game
game()
