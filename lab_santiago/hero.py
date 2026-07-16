import random 
import ability
import armor
class Hero:
    def __init__(self, name, starting_health=100):
        self.name = name
        self.current_health = starting_health

    def battle(self, opponent):
        mylist = [self.name,opponent.name]
        print(random.choice(mylist))

    def add_ability(self, ability):
        self.ability = ability
        print(self.ability)

    def attack(self):
        total_damage = 0
        for ability in self.abilities:
            total_damage += ability.attack()
        return total_damage

    def add_armor(self, armor):
        self.armors.append(armor)

    def defend(self):
        total_block = 0
        for armor in self.armors:
            total_block += armor.block()
            print(total_block)
   return total_block    
 
 def take_damage(self, damage): 
    blocked = self.defend()
    actual_damage = max(damage - blocked,0 )
    self.current_health -= actual_damage
    return actual_damage
      
if __name__ == "__main__":
    myhero = Hero("Spider-Man", 150)
    print(myhero.name)
    print(myhero.current_health)
    my_opponet = Hero("Venom", 200)
    myhero.battle(my_opponet)
    my_hero.add_ability("Web Shooter", 25) 
    my_hero.add_ability("Spidey Senses", 10)
    my.hero.attack()
    my_hero.add_armor (Armor("Super Suit", 20)
    my_hero.add_armor (Armor("Helmet", 10)  
    my_hero.defend()  
    my_hero.take_damage(40)   
    print(my_hero.current_health)
    from ability import Ability
from weapon import Weapon
from armor import Armor
from hero import Hero
from team import Team

class Arena:
  def __init__(self):
    '''Instantiate properties
        team_one: None
        team_two: None
    '''



  def create_ability(self):
    '''Prompt for Ability information.
      return Ability with values from user Input
    '''
    name = input("What is the ability name?  ")
    max_damage = input(
      "What is the max damage of the ability?  ")

    return Ability(name, max_damage)

  def create_weapon(self):
    '''Prompt user for Weapon information
        return Weapon with values from user input.
   

  def create_armor(self):
    
 
      pass

  def create_hero(self):
    '''Prompt user for Hero information
      return Hero with values from user input.
    '''
    hero_name = input("Hero's name: ")
    hero = Hero(hero_name)
    add_item = None
    while add_item != "4":
      add_item = input("[1] Add ability\n[2] Add weapon\n[3] Add armor\n[4] Done adding items\n\nYour choice: ")
      if add_item == "1":
       
      elif add_item == "2":
       
      elif add_item == "3":
      
    return hero

  
  def build_team_one(self):
    '''Prompt the user to build team_one '''
   
    numOfTeamMembers = int(input("How many members would you like on Team One?\n"))
    for i in range(numOfTeamMembers):
      hero = self.create_hero()
      self.team_one.add_hero(hero)

  
  def build_team_two(self):
    '''Prompt the user to build team_two'''
    
    pass

  def team_battle(self):
    '''Battle team_one and team_two together.'''
    
    pass

  def show_stats(self):
    '''Prints team statistics to terminal.'''
    
  

    print("\n")
    print(self.team_one.name + " statistics: ")
    self.team_one.stats()
    print("\n")
    print(self.team_two.name + " statistics: ")
    self.team_two.stats()
    print("\n")

   
    team_kills = 0
    team_deaths = 0
    for hero in self.team_one.heroes:
        team_kills += hero.kills
        team_deaths += hero.deaths
    if team_deaths == 0:
        team_deaths = 1
    print(self.team_one.name + " average K/D was: " + str(team_kills/team_deaths))


    for hero in self.team_one.heroes:
        if hero.deaths == 0:
            print("survived from " + self.team_one.name + ": " + hero.name)

   

    game_is_running = True

   
    arena = Arena()


    arena.build_team_one()
    arena.build_team_two()

    while game_is_running:

        arena.team_battle()
        arena.show_stats()
        play_again = input("Play Again? Y or N: ")

       
        if play_again.lower() == "n":
            game_is_running = False

        else:
     
            arena.team_one.revive_heroes()
            arena.team_two.revive_heroes()




                                  