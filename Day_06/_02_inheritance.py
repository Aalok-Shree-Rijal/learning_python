# in simple words just copying the attributes of one 
# class to another without rewriting the code

from classes import chef, masterChef

# by doing this i am copying the attributes 
# of chef class to myChef
myChef = chef()
myChef.make_chowmein()

# by doing this i am copying the attributes 
# of masterChef class to seniorChef
seniorChef = masterChef()
seniorChef.make_special_dish()