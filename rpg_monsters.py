



class Goblin(object):
	def __init__(self):
		self.name = "goblin";
		self.max_health = 600;
		self.current_health = 600;
		self.power = 80;
		self.bonus_damage = 1.2;
	def alive(self):
		return self.current_health > 0;
	def take_damage(self, base_dmg_from_hero, bonus_from_hero):
		self.current_health -= (base_dmg_from_hero + bonus_from_hero);
	def attack(self, hero):
		print "%s attacks %s for %d points of damage" %(self.name, hero.name, (self.power * self.bonus_damage))
		hero.take_damage(self.power, self.bonus_damage)

class Troll(object):
	def __init__(self):
		self.name = "troll";
		self.max_health = 1200;
		self.current_health = 1200;
		self.power = 90;
		self.bonus_damage = 1.2;
	def alive(self):
		return self.current_health > 0;
	def take_damage(self, base_dmg_from_hero, bonus_from_hero):
		self.max_health -= (base_dmg_from_hero + bonus_from_hero);
	def attack(self, hero):
		print "%s attacks %s for %d points of damage" %(self.name, hero.name, (self.power * self.bonus_damage))
		hero.take_damage(self.power, self.bonus_damage)