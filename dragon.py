class Dragon(object):
	def __init__(self):
		self.name = "Dragon";
		self.max_health = 6000;
		self.current_health = 6000;
		self.power = 500;
		self.bonus_damage = 1.5;
	def alive(self):
		return self.current_health > 0;
	def take_damage(self, base_dmg_from_hero, bonus_from_hero):
		self.current_health -= (base_dmg_from_hero);
	def attack(self, hero):
		print "%s attacks %s for %d points of damage" % (self.name, hero.name, (self.power * self.bonus_damage))
		hero.take_damage(self.power, self.bonus_damage)