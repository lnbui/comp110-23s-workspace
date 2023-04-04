"""EX06: Choose Your Own Adventure!"""

__author__ = "730398384"

from random import randint

# Outlining global variables
player: str = ""
life_points: int = 10
attack_points: int = 10
defense_points: int = 10
points: int = 10
enemy_health: int = 0

# Outlining the magic number emojis
HEART: str = "\U0001F49A"
FIST: str = "\U0001F44A"
SHIELD: str = "\U0001F6E1"
MONEY: str = "\U0001F4B2"

round_number: int = 0


def greet() -> None:
    """This introduces the player to the game."""
    global player
    global attack_points
    global defense_points
    global points
    global life_points
    print("Welcome to Gladiator of the Century, a game where you battle for as long as you have the life points.")
    player = input("But before we get to all of that, what's your name? ")
    print(f"{player}? That's a good, strong name. Let me give you the lowdown, Gladiator. While in the arena, you can choose the options of 1: Fight, 2: Upgrade or 3: Quit.")
    print("When choosing to Fight, you can 1: Attack or 2: Defend. Choosing Attack will allow you to damage your opponent while leaving yourself open to your opponent's own attacks, while defending allows you to leverage your defense to the fullest, but your attacks will be weaker.")
    print("Naturally, victory is its own reward. After every victory, you will have gained some points {MONEY} that you can use to upgrade your attack or defense. However--once your life points are all out, then that's the end of the game. You will begin with 10 attack, defense, life, and victory points to start.")


def main() -> None:
    """The main function that begins the game."""
    greet()
    # Calls global variables
    global round_number
    global life_points
    global attack_points
    global defense_points
    global points
    play_game: bool = True
    player_choice: int = 0
    # Ends game if no life points left
    if life_points <= 0:
        print("Sorry! You died.")
        play_game is False
    # Sets up a "Status Screen," giving players their current status"
    while play_game is True and life_points > 0:
        print(f"=I=====[Round {round_number}]=====I=")
        print(f"Current Attack Points: {attack_points} {FIST}")
        print(f"Current Defense Points: {defense_points} {SHIELD}")       
        print(f"Current Life Points: {life_points} {HEART}")
        print(f"Current Victory Points: {points} {MONEY}")
        # Sets up player choices
        player_choice = int(input("Input the number corresponding to the choice you're doing: 1: Fight, 2: Upgrade, or 3: Quit "))
        while player_choice < 3 or player_choice < 0:
            player_choice = int(input("Please input the number corresponding to the choice you're doing: 1: Fight, 2: Upgrade, or 3: Quit "))
        if player_choice == 1:
            fight()
        elif player_choice == 2:
            upgrade()
        elif player_choice == 3:
            play_game is False
        round_number += 1                
    # Gives an end player screen
    if play_game is False:
        print(f"Final Round: {round_number}")
        print(f"Final Attack Points: {attack_points} {FIST}")
        print(f"Final Defense Points: {defense_points} {SHIELD}")       
        print(f"Final Life Points: {life_points} {HEART}")
        print(f"Final Victory Points: {points} {MONEY}")
        print(f"Thanks for playing, {player}! Hope you had fun!") 


def fight() -> None:
    """The fight function, first of the three options."""
    global player
    global life_points
    global attack_points
    global defense_points
    global points
    global enemy_health
    global round_number
    # Establishes enemy values
    enemy_health = randint(1, 5 + round_number)
    # Gives player choice on what to do
    fight_choice: int = 0
    fight_choice = int(input("Input the number corresponding to the choice you would like to do: 1: Attack or 2: Defend! "))
    while fight_choice < 1 or fight_choice > 2:
        fight_choice = int(input("Please input the number corresponding to the choice you would like to do: 1: Attack or 2: Defend! "))
    if enemy_health <= 0:
        print(f"The {player} wins this round! They live to fight another day! They have gained some victory points!")
        points += (round_number + randint(1, 10))
    if fight_choice == 1:
        attack()
    if fight_choice == 2:
        defend()  


def attack() -> None:
    """Allows player to attack."""
    global life_points
    global attack_points
    global defense_points
    global enemy_health
    enemy_attack = defense_points + 1
    enemy_defense = randint(1, attack_points - 1)
    attack_damage: int = randint(1, attack_points)
    if attack_damage > enemy_defense:
        damage = attack_damage - enemy_defense
        enemy_health = enemy_health - damage
        print(f"You inflicted {damage} damage to the enemy! {FIST}") 
    elif attack_damage <= enemy_defense:
        remaining_enemy_defense = enemy_defense - attack_damage
        enemy_defense = remaining_enemy_defense
        print(f"You have struck a mighty blow! The enemy has {enemy_defense} defense left! {SHIELD}")
    if enemy_attack > (defense_points - 3):
        enemy_damage = enemy_attack - (defense_points - 3)
        life_points = life_points - enemy_damage
        print(f"The enemy inflicted {enemy_damage} damage to you! {FIST}") 
    elif enemy_attack <= (defense_points - 3):
        remaining_defense = defense_points - enemy_attack
        defense_points = remaining_defense
        print(f"The enemy struck a mighty blow! You have {defense_points} defense left! {SHIELD}")  


def defend() -> None:
    """Allows player to attack."""
    global life_points
    global attack_points
    global defense_points
    global enemy_health
    enemy_attack = defense_points + 1
    enemy_defense = randint(1, attack_points - 1)
    attack_damage: int = randint(1, attack_points)
    if (attack_damage - 3) > enemy_defense:
        damage = attack_damage - enemy_defense
        enemy_health = enemy_health - damage
        print(f"You inflicted {damage} damage to the enemy! {FIST}") 
    elif (attack_damage - 3) <= enemy_defense:
        remaining_enemy_defense = enemy_defense - attack_damage
        enemy_defense = remaining_enemy_defense
        print(f"You have struck a mighty blow! The enemy has {enemy_defense} defense left! {SHIELD}")
    if enemy_attack > (defense_points + 3):
        enemy_damage = enemy_attack - (defense_points - 3)
        life_points = life_points - enemy_damage
        print(f"The enemy inflicted {enemy_damage} damage to you! {FIST}") 
    elif enemy_attack <= (defense_points + 3):
        remaining_defense = defense_points - enemy_attack
        defense_points = remaining_defense
        print(f"The enemy struck a mighty blow! You have {defense_points} defense left! {SHIELD}")  


def upgrade() -> None:
    """Allows the player to upgrade their values."""
    global life_points
    global attack_points
    global defense_points
    global points
    shop_choice: int = 0
    while points > 0:
        print(f"Welcome! You have {points} left to spend! {MONEY}")
        shop_choice = int(input("Input the number corresponding to the choice you would like to do: 1: Upgrade Attack, 2: Upgrade Defense, or 3: Upgrade Life"))
        if shop_choice == 1:
            upgrade_attack = int(input("Input how many points you'd like to invest into attack!")) 
            if upgrade_attack <= points:
                attack_points += upgrade_attack
            else:
                upgrade_attack = int(input("Please input how many points you'd like to invest into attack!"))  
        elif shop_choice == 2:
            upgrade_defense = int(input("Input how many points you'd like to invest into defemse!")) 
            if upgrade_defense <= points:
                defense_points += upgrade_attack
            else:
                upgrade_defense = int(input("Please input how many points you'd like to invest into defense!")) 
        elif shop_choice == 3:
            upgrade_life = int(input("Input how many points you'd like to invest into life!")) 
            if upgrade_life <= points:
                life_points += upgrade_life
            else:  
                upgrade_life = int(input("Input how many points you'd like to invest into life!"))          


if __name__ == "__main__":
    main()
    """Begins the function."""