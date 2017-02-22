from rpg_hero import Hero;
from rpg_monsters import Goblin, Troll;
from dragon import Dragon;



dragon = Dragon();
hero = Hero();
enemies = [Goblin(),Troll()];



for enemy in enemies:
	# loop through all the enemies in the enemies list
	# while hero.health > 0 and enemy.health > 0:
	while hero.alive() and enemy.alive():
		# keep the loop going as long as both have health over 0
		print "What will you do?";
		print "1. FIGHT! %s" % enemy.name
		print "2. Run away!"
		print "3. Search the forest for more challenges"
		print "> ",
		input = int(raw_input());
		if input == 1:
			hero.attack(enemy);
			enemy.attack(hero);
			print "Your HEALTH is currently %d of %d, the ENEMY is at %d of %d" % (hero.current_health, hero.max_health, enemy.current_health, enemy.max_health);
		elif input == 2:
			break;
		elif input == 3:
			while hero.alive() and dragon.alive():
				print "                                                  .~))>>"
				print "                                                 .~)>>"
				print "                                             .~))>>"             
				print "                                           .~))>>)))>>      .-~))>>  "
				print "                                         .~)))))>>       .-~))>>)>"
				print "                                       .~)))>>))))>>  .-~)>>)>"
				print "                   )                 .~))>>))))>>  .-~)))))>>)>"
				print "                ( )@@*)             //)>))))))  .-~))))>>)>"
				print "              ).@(@@               //))>>))) .-~))>>)))))>>)>"
				print "          ))  )@@*.@@ )          //)>))) //))))))>>))))>>)>"
				print "       ((  ((@@@.@@             |/))))) //)))))>>)))>>)>"
				print "      )) @@*. )@@ )   (\_(\-\b  |))>)) //)))>>)))))))>>)>"
				print "    (( @@@(.@(@ .    _/`-`  ~|b |>))) //)>>)))))))>>)>"
				print "     )* @@@ )@*     (@) (@)  /\b|))) //))))))>>))))>>"
				print "   (( @. )@( @ .   _/       /  \b)) //))>>)))))>>>_._"
				print "    )@@ (@@*)@@.  (6,   6) / ^  \b)//))))))>>)))>>   ~~-."
				print " ( @jgs@@. @@@.*@_ ~^~^~, /\  ^  \b/)>>))))>>      _.     `,"
				print "  ((@@ @@@*.(@@ .   \^^^/' (  ^   \b)))>>        .'         `,"
				print "   ((@@).*@@ )@ )    `-'   ((   ^  ~)_          /             `,"
				print "     (@@. (@@ ).           (((   ^    `\        |               `."
				print "       (*.@*              / ((((        \        \      .         `."
				print "                         /   (((((  \    \    _.-~\     Y,         ;"
				print '                        /   / (((((( \    \.-~   _.`" _.-~`,       ;'
				print "                       /   /   `(((((()    )    (((((~      `,     ;"
				print '                     _/  _/      `"""/   /"                  ;     ;'
				print "                 _.-~_.-~           /  /'                _.-~   _.'"
				print "               ((((~~              / /'              _.-~ __.--~"
				print "                                  ((((          __.-~ _.-~"
				print "                                              .'   .~~"
				print "                                              :    ,'"
				print "                                              ~~~~~"

				print "You approach a large clearing in the forest, the trees are flattened and burned amidst a chaos of charred bodies. A massive cave entrance lies ahead, do you wish to proceed?"
				print "1. Take your chances"
				print "2. Run before the Dragon notices you"
				input = int(raw_input());
				if input == 1:
					hero.attack(dragon);
					dragon.attack(hero);
					print "Your HEALTH is currently %d of %d, the Dragon is at %d of %d" % (hero.current_health, hero.max_health, dragon.current_health, dragon.max_health);
				else:
					print "The %s chases you down but you barely escape!" % dragon.name
					break;
			print "You were Killed by the Massive %s" % dragon.name
		else:
			print "Invalid choice %r" %input
		if enemy.alive():
			hero.current_health -= enemy.power;
	if hero.alive():
		print "You won! The %s is defeated" % enemy.name
	else:
		print "You were Killed"
