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
- "Kragma Butcher"
---
# Kragma Butcher
*Source: Theros Bestiary, Vol. XI*
![](/Compendium/bestiary/humanoid/img/kragma-butcher.webp#right)

Minotaurs go into battle hungry. The first sight of their enemies’ blood sends them into a flesh-eating rage.

```statblock
"name": "Kragma Butcher"
"size": "Medium"
"type": "humanoid"
"subtype": "minotaur"
"alignment": "Any alignment"
"ac": !!int "12"
"hp": !!int "21"
"hit_dice": "3d8 + 9"
"modifier": !!int "2"
"stats":
  - !!int "15"
  - !!int "14"
  - !!int "16"
  - !!int "10"
  - !!int "12"
  - !!int "10"
"speed": "30 ft."
"saves":
  - "constitution": !!int "6"
"skillsaves":
  - "name": "[Athletics](/Compendium/rules/skills.md#Athletics)"
    "desc": "+5"
  - "name": "[Perception](/Compendium/rules/skills.md#Perception)"
    "desc": "+4"
  - "name": "[Survival](/Compendium/rules/skills.md#Survival)"
    "desc": "+4"
  - "name": "[Intimidation](/Compendium/rules/skills.md#Intimidation)"
    "desc": "+3"
"senses": "passive Perception 10"
"languages": "Common, Minotaur, any one language"
"cr": "2"
"traits":
  - "desc": "The butcher has Advantage on initiative rolls."
    "name": "Battle Readiness"
  - "desc": "Immediately after the butcher uses the Dash action on its turn and moves\
      \ at least 20 feet, it can make one melee attack with its horns as a bonus action."
    "name": "Goring Rush"
  - "desc": "The butcher's attack rolls score a critical hit on a roll of 19 or 20\
      \ on the d20."
    "name": "Improved Critical"
  - "desc": "The butcher starves itself prior to battle. If it kills a creature, there\
      \ is a 50% chance it will stop fighting to eat the corpse. If the butcher eats,\
      \ each hostile creature that can see it must succeed on a DC 11 Wisdom saving\
      \ throw or be frightened of the butcher until the end of the butcher's next\
      \ turn. If a hungry butcher does not eat after a kill, it gets a +2 bonus to\
      \ damage rolls and Strength and Dexterity checks until the end of its next turn."
    "name": "Insatiable Ragegore Hunger"
"actions":
  - "desc": "The butcher can attack twice, instead of once, whenever it takes the\
      \ Attack action on its turn."
    "name": "Extra Attack"
  - "desc": "_Melee Weapon Attack:_ +7 to hit, reach 5 ft., one target. _Hit:_ 5 (1d6\
      \ + 2) piercing damage, and the butcher can use a bonus action to attempt to\
      \ shove that target with its horns. The target must be within 5 feet of the\
      \ butcher and no more than one size larger than it. Unless the target succeeds\
      \ on a DC 13 Strength saving throw, the butcher pushes it up to 10 feet away\
      \ from the butcher."
    "name": "Horns"
  - "desc": "_Melee Weapon Attack:_ +7 to hit, reach 10 ft., one target. _Hit:_ 6\
      \ (1d8 + 2) piercing damage, or 7 (1d10 + 2) piercing damage if used with two\
      \ hands to make a melee attack."
    "name": "War pick"
"source":
  - "TBVXI"
```
^statblock