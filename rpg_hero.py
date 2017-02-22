



class Hero(object):
	# call the init method which is built into classes, pass it self as a paramter
	def __init__(self):
		# class properties (attached to self)
		self.name = "Merlin"
		self.max_health = 1000;
		self.current_health = 1000;
		self.power = 90;
		self.bonus_damage = 1.5
		# make a method that returns a boolean for whether or not the hero is alive or not
	def alive(self):
		return self.current_health > 0;
	def take_damage(self, base_dmg_enemy, bonus_from_enemy):
		self.current_health -= (base_dmg_enemy * bonus_from_enemy);
	def attack(self, enemy):
		# print "%s attacks %s" %(self.name, enemy.name)
		enemy.take_damage(self.power,self.bonus_damage)
		# time.sleep(1.5);
		print "%s has done %d damage to %s" % (self.name, (self.power * self.bonus_damage), enemy.name)

