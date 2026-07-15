---
obsidianUIMode: preview
cssclasses:
- json5e-monster
tags:
- compendium/src/5e/tbvxi
- monster/cr/1
- monster/size/medium
- monster/type/humanoid/minotaur
statblock: inline
statblock-link: "#^statblock"
aliases:
- "Pensive Minotaur"
---
# Pensive Minotaur
*Source: Theros Bestiary, Vol. XI*
![](/Compendium/bestiary/humanoid/img/pensive-minotaur.webp#right)

The Champion and her companions marched through the night, but the battle was over before they arrived. In the middle of the carnage sat a solitary minotaur, lost in what seemed to the Champion to be thought.

—The Theriad

```statblock
"name": "Pensive Minotaur"
"size": "Medium"
"type": "humanoid"
"subtype": "minotaur"
"alignment": "Chaotic Evil"
"ac": !!int "15"
"ac_class": "natural armor"
"hp": !!int "21"
"hit_dice": "3d8 + 9"
"modifier": !!int "2"
"stats":
  - !!int "15"
  - !!int "14"
  - !!int "16"
  - !!int "10"
  - !!int "10"
  - !!int "10"
"speed": "30 ft."
"saves":
  - "constitution": !!int "5"
"skillsaves":
  - "name": "[Athletics](/Compendium/rules/skills.md#Athletics)"
    "desc": "+4"
  - "name": "[Survival](/Compendium/rules/skills.md#Survival)"
    "desc": "+2"
  - "name": "[Intimidation](/Compendium/rules/skills.md#Intimidation)"
    "desc": "+2"
"senses": "passive Perception 10"
"languages": "Common, Minotaur, any one language"
"cr": "1"
"traits":
  - "desc": "Immediately after the minotaur uses the Dash action on its turn and moves\
      \ at least 20 feet, it can make one melee attack with its horns as a bonus action."
    "name": "Goring Rush"
"actions":
  - "desc": "The minotaur makes two attacks."
    "name": "Multiattack"
  - "desc": "_Melee Weapon Attack:_ +4 to hit, reach 5 ft., one target. _Hit:_ 5 (1d6\
      \ + 2) piercing damage, and the minotaur can use a bonus action to attempt to\
      \ shove that target with its horns. The target must be within 5 feet of the\
      \ minotaur and no more than one size larger than it. Unless the target succeeds\
      \ on a DC 12 Strength saving throw, the minotaur pushes it up to 10 feet away\
      \ from the minotaur."
    "name": "Horns"
  - "desc": "_Melee or Ranged Weapon Attack:_ +4 to hit, reach 5 ft. or range 20/60\
      \ ft., one target. _Hit:_ 4 (1d4 + 2) piercing damage."
    "name": "Claws"
"source":
  - "TBVXI"
```
^statblock