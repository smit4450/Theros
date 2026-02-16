---
title: Minotaur Skullcleaver
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- ttrpg-cli/compendium/src/5e/tbvxi
- ttrpg-cli/monster/cr/1
- ttrpg-cli/monster/size/m
- ttrpg-cli/monster/type/humanoid
statblock: inline
aliases: ["Minotaur Skullcleaver"]
---
# Minotaur Skullcleaver
*Source: Theros Bestiary TBVXI*  

<blockquote><small>“Their only dreams are of full stomachs.”

—Kleon the Iron-Booted</small></blockquote>

![Minotaur Skullcleaver](Compendium/bestiary/humanoid/img/minotaur-skullcleaver.webp#right|850)  

```statblock
"name": "Minotaur Skullcleaver (TBVXI)"
"size": "Medium"
"type": "humanoid"
"subtype": "minotaur"
"alignment": "Any alignment Chaotic"
"ac": !!int "14"
"ac_class": "natural armor"
"hp": !!int "12"
"hit_dice": "2d8 + 4"
"modifier": !!int "1"
"stats":
  - !!int "15"
  - !!int "12"
  - !!int "15"
  - !!int "9"
  - !!int "11"
  - !!int "9"
"speed": "30 ft."
"skillsaves":
  - "name": "[[skills#Intimidation|Intimidation]]"
    "desc": "+3"
"senses": "passive Perception 10"
"languages": "Common, Minotaur"
"cr": "1"
"traits":
  - "desc": "Immediately after the skullcleaver uses the Dash action on its turn and moves at least 20 feet, it can make one melee attack with its horns as a bonus action."
    "name": "Goring Rush"
  - "desc": "Whenever the minotaur starts its turn with half its [[hit-points-xphb|Hit Points]] or fewer, roll a d6. On a 6, the raider goes berserk. On each of its turns while berserk, the minotaur attacks the nearest non-minotaur creature it can see. If no non-minotaur creature is near enough to move to and attack, the minotaur attacks an object, with preference for an object smaller than itself. Once the minotaur goes berserk, it continues to do so until it is destroyed or regains all its [[hit-points-xphb|Hit Points]].A creature within 60 feet of the berserk minotaur can try to calm it by speaking firmly and persuasively. The minotaur must be able to hear that creature, who must take an action to make a DC 20 Charisma (Persuasion) check. If the check succeeds, the minotaur ceases being berserk. If it takes damage while still at half [[hit-points-xphb|Hit Points]] or fewer, the minotaur might go berserk again."
    "name": "Rage of Mogis"
  - "desc": "The minotaur starves itself prior to battle. If it kills a creature and has not eaten, there is a 50% chance it will stop fighting to eat the corpse. If the minotaur eats, each hostile creature that can see it must succeed on a DC 11 Wisdom saving throw or be [[conditions#Frightened|frightened]] of the minotaur until the end of the minotaur's next turn. If a hungry minotaur does not eat after a kill, it gets a +1 bonus to damage rolls until it eats."
    "name": "Ragegore Hunger"
  - "desc": "If the skullcleaver surprises a creature and hits it with an attack during the first round of combat, the target takes an extra 7 (2d6) damage from the attack."
    "name": "Surprise Attack"
"actions":
  - "desc": "_Melee Weapon Attack:_ +6 to hit, reach 5 ft., one target. _Hit:_ 5 (1d6 + 2) piercing damage, and the skullcleaver can use a bonus action to attempt to shove that target with its horns. The target must be within 5 feet of the skullcleaver and Large or smaller. Unless the target succeeds on a DC 14 Strength saving throw, the skullcleaver pushes it up to 10 feet away from the skullcleaver."
    "name": "Horns"
  - "desc": "_Melee Weapon Attack:_ +6 to hit, reach 5 ft., one target. _Hit:_ 8 (1d12 + 2) slashing damage."
    "name": "Greataxe"
"source":
  - "TBVXI"
"image": "Compendium/bestiary/humanoid/token/minotaur-skullcleaver-tbvxi.webp"
```
^statblock