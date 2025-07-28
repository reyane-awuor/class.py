# Superhero Class Documentation

## Overview

This Python module implements a Superhero class and its subclass Sidekick to model superhero characters and their sidekicks in an object-oriented way. The classes provide methods to simulate superhero actions, health management, and identity handling.

## Classes

### Superhero

The main class representing a superhero character.

#### Attributes:
- name (str): The superhero's public name
- secret_identity (str): The superhero's secret identity (encapsulated)
- powers (list): List of the superhero's powers/abilities
- origin_story (str): The character's backstory
- health (int): Health points (default: 100)

#### Methods:
- __init__(name, secret_identity, powers, origin_story): Constructor
- use_power(): Returns a string describing power usage
- take_damage(damage): Reduces health and returns status
- reveal_identity(): Reveals the secret identity

### Sidekick

A subclass of Superhero representing a sidekick character.

#### Additional Attributes:
- mentor (str): The name of the sidekick's mentor/superhero

#### Methods (including overridden and new):
- __init__(name, secret_identity, powers, origin_story, mentor): Constructor
- call_for_help(): Unique method to call the mentor
- use_power(): Overrides parent method with sidekick-specific behavior

## Example Usage

python
hero = Superhero("Captain Thunder", "John Smith", 
                ["lightning bolts", "flight", "super strength"],
                "Struck by experimental energy beam")

sidekick = Sidekick("Thunder Boy", "Timmy Jones",
                  ["small lightning sparks", "gliding"],
                  "Trained by Captain Thunder",
                  "Captain Thunder")

print(hero.use_power())  # Output: Captain Thunder uses lightning bolts!
print(sidekick.use_power())  # Output: Thunder Boy tentatively tries small lightning sparks.
print(sidekick.call_for_help())  # Output: Thunder Boy calls Captain Thunder for backup!
print(hero.take_damage(30))  # Output: Captain Thunder has 70 health remaining.


## Key Features

- Object-oriented design with inheritance
- Encapsulation of secret identity
- Method overriding in subclass
- Default attribute values
- Interactive health management


