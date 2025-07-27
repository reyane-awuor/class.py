class Superhero:
    """A class representing a superhero"""
    
    def _init_(self, name, secret_identity, powers, origin_story):
        """Constructor to initialize superhero attributes"""
        self.name = name
        self.secret_identity = secret_identity 
        self.powers = powers
        self.origin_story = origin_story
        self.health = 100  
        
    def use_power(self):
        """Method to use the superhero's power"""
        return f"{self.name} uses {self.powers[0]}!"
    
    def take_damage(self, damage):
        """Method to handle damage"""
        self.health -= damage
        if self.health <= 0:
            return f"{self.name} has been defeated!"
        return f"{self.name} has {self.health} health remaining."
    
    def reveal_identity(self):
        """Method to reveal secret identity"""
        return f"{self.name}'s secret identity is {self.secret_identity}."


class Sidekick(Superhero):
    """A class representing a sidekick, inheriting from Superhero"""
    
    def _init_(self, name, secret_identity, powers, origin_story, mentor):
        """Constructor for Sidekick with additional mentor attribute"""
        super()._init_(name, secret_identity, powers, origin_story)
        self.mentor = mentor
        self.health = 70 
        
    def call_for_help(self):
        """Unique method for sidekicks"""
        return f"{self.name} calls {self.mentor} for backup!"
    
    def use_power(self): 
        """Sidekicks use powers differently"""
        return f"{self.name} tentatively tries {self.powers[0]}."


if __name__ == "_main_":
    hero = Superhero("Captain Thunder", "John Smith", 
                    ["lightning bolts", "flight", "super strength"],
                    "Struck by experimental energy beam")
    
    sidekick = Sidekick("Thunder Boy", "Timmy Jones",
                      ["small lightning sparks", "gliding"],
                      "Trained by Captain Thunder",
                      "Captain Thunder")
    
    print(hero.use_power()) 
    print(sidekick.use_power())  
    print(sidekick.call_for_help())  
    print(hero.take_damage(30))  