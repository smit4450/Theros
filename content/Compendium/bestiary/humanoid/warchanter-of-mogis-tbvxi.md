---
obsidianUIMode: preview
cssclasses:
- json5e-monster
tags:
- compendium/src/5e/tbvxi
- monster/cr/2
- monster/size/medium
- monster/type/humanoid/minotaur
statblock: inline
statblock-link: "#^statblock"
aliases:
- "Warchanter of Mogis"
---
# Warchanter of Mogis
*Source: Theros Bestiary, Vol. XI*
![](/Compendium/bestiary/humanoid/img/warchanter-of-mogis.webp#center)

```statblock
"name": "Warchanter of Mogis"
"size": "Medium"
"type": "humanoid"
"subtype": "minotaur"
"alignment": "Lawful Evil"
"ac": !!int "13"
"ac_class": "natural armor"
"hp": !!int "21"
"hit_dice": "3d8 + 9"
"modifier": !!int "0"
"stats":
  - !!int "17"
  - !!int "10"
  - !!int "16"
  - !!int "11"
  - !!int "17"
  - !!int "13"
"speed": "30 ft."
"saves":
  - "constitution": !!int "5"
  - "wisdom": !!int "5"
"skillsaves":
  - "name": "[Intimidation](/Compendium/rules/skills.md#Intimidation)"
    "desc": "+3"
  - "name": "[Religion](/Compendium/rules/skills.md#Religion)"
    "desc": "+2"
  - "name": "[Persuasion](/Compendium/rules/skills.md#Persuasion)"
    "desc": "+3"
"senses": "passive Perception 10"
"languages": "Common, Minotaur, Any one language"
"cr": "2"
"traits":
  - "desc": "Immediately after the warchanter uses the Dash action on its turn and\
      \ moves at least 20 feet, it can make one melee attack with its horns as a bonus\
      \ action."
    "name": "Goring Rush"
  - "desc": "At the beginning of the warchanter's turn, if Mogis heard it chanting\
      \ to him at any point since the warchanter's last turn, the a creature of the\
      \ warchanter's choice gains the following ability until the beginning of the\
      \ warchanter's next turn: _**Fear Aura.**_ Any hostile target to the creature\
      \ that starts its turn within 20 feet of the creature must make a Wisdom saving\
      \ throw (DC = 8 + proficiency bonus + Charisma modifier), unless the creature\
      \ is incapacitated. On a failed save, the target is frightened until the start\
      \ of its next turn. If the target's saving throw is successful, the target is\
      \ immune to the creature's Fear Aura for the next 24 hours."
    "name": "Inspired"
  - "desc": "The minotaur starves itself prior to battle. If it kills a creature and\
      \ has not eaten, there is a 50% chance it will stop fighting to eat the corpse.\
      \ If the minotaur eats, each hostile creature that can see it must succeed on\
      \ a DC 11 Wisdom saving throw or be frightened of the minotaur until the end\
      \ of the minotaur's next turn. If a hungry minotaur does not eat after a kill,\
      \ it gets a +1 bonus to damage rolls until it eats."
    "name": "Ragegore Hunger"
"actions":
  - "desc": "The warchanter makes two melee attacks."
    "name": "Multiattack"
  - "desc": "_Melee Weapon Attack:_ +5 to hit, reach 5 ft., one target. _Hit:_ 6 (1d6\
      \ + 3) piercing damage, and the warchanter can use a bonus action to attempt\
      \ to shove that target with its horns. The target must be within 5 feet of the\
      \ warchanter and no more than one size larger than it. Unless the target succeeds\
      \ on a DC 13 Strength saving throw, the warchanter pushes it up to 10 feet away\
      \ from the warchanter."
    "name": "Horns"
  - "desc": "_Melee Weapon Attack:_ +5 to hit, reach 5 ft., one creature. _Hit:_ 10\
      \ (2d6 + 3) bludgeoning damage."
    "name": "Maul"
  - "desc": "The warchanter recites an incantation to Mogis. It continues to do so\
      \ until it takes a different action."
    "name": "Chant"
"source":
  - "TBVXI"
```
^statblock