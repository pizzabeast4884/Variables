import random

def rollDice(sides):
    print(random.randint(1, sides))

sides = int(input("how many sides do you want your dice to have"))

rollDice(sides)