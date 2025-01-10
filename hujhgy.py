import random

# character class(?)
class Character:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def attack(self, opponent):
        damage = random.randint(7, 50)  # deals random damage between set numbers
        print(f"{self.name} swings their sword at {opponent.name} and deals {damage} damage!")
        opponent.health -= damage

    def heal(self):
        heal_amount = random.randint(10, 43)
        self.health += heal_amount
        print(f"{self.name} pops a medkit and heals {heal_amount} health!")

    def magic(self, opponent):
        damage = random.randint(30, 35)
        print(f"{self.name} hurls a powerful spell torwards {opponent.name} and deals {damage} damage!")
        opponent.health -= damage

    def is_alive(self):
        return self.health > 0

# creates the playable loop for the game
def game():
    # creation of the characters
    hero = Character(input("Enter your hero's name: "), 100)
    villain = Character("evil kortnee", 150)

    print(f"\n hey loser! your up against {villain.name}!")
    while hero.is_alive() and villain.is_alive():
        print(f"\n{hero.name}'s health: {hero.health} | {villain.name}'s health: {villain.health}\n")
        
        # start of players turn
        print("Choose your action:")
        print("1. Attack")
        print("2. Heal")
        print("3. Magic")
        choice = input("enter the number of your choice: ")

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
        print(f"\hey! {hero.name} defeated {villain.name}. you just spammed heals though, didnt you?")
    else:
        print(f"\n{villain.name} cooked you.. i would NOT let that slide")

    # replay
    if input("\nwant to rematch? or are you scared? (yes/no): ").lower() == "yes":
        game()

# runs the game
game()
