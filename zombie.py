# instead of console.log(something)
# in python we can use 
# print dir(something) to show local scope of an object
# print vars(something) will show local variables of an object


class Zombie(object):
	def __init__(self,speed,strength,hunger,weapon,health):
		self.speed = speed;
		self.strength = strength;
		self.hunger = hunger;
		self.weapon = weapon;
		self.health = health;
		self.type = "zombie";

