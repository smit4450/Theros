---
title: Borderland Minotaur
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- ttrpg-cli/compendium/src/5e/tbvxi
- ttrpg-cli/monster/cr/3
- ttrpg-cli/monster/size/m
- ttrpg-cli/monster/type/humanoid
statblock: inline
aliases: ["Borderland Minotaur"]
---
# Borderland Minotaur
*Source: Theros Bestiary TBVXI*  

<blockquote><small>“You have led us to triumph over the forces of Mogis!” said Brygus the Brave, clapping the Champion on the back.

The Champion wiped the sweat and blood from her brow.

“I count eight graves,” she said. “Too many to call this a victory.”

—<i>The Theriad</i></small></blockquote>

![Borderland Minotaur](https://img.scryfall.com/cards/art_crop/front/9/c/9c7f6eb2-feae-4dc9-a009-0ad60f89a592.jpg?1562822251#right)  

```statblock
"name": "Borderland Minotaur (TBVXI)"
"size": "Medium"
"type": "humanoid"
"subtype": "minotaur"
"alignment": "Any alignment"
"ac": !!int "15"
"ac_class": "natural armor"
"hp": !!int "21"
"hit_dice": "3d8 + 9"
"modifier": !!int "2"
"stats":
  - !!int "18"
  - !!int "14"
  - !!int "16"
  - !!int "10"
  - !!int "12"
  - !!int "10"
"speed": "30 ft."
"saves":
  - "constitution": !!int "5"
"skillsaves":
  - "name": "[Athletics](Compendium/rules/skills.md#Athletics)"
    "desc": "+6"
  - "name": "[Perception](Compendium/rules/skills.md#Perception)"
    "desc": "+3"
  - "name": "[Survival](Compendium/rules/skills.md#Survival)"
    "desc": "+3"
  - "name": "[Intimidation](Compendium/rules/skills.md#Intimidation)"
    "desc": "+2"
"senses": "passive Perception 10"
"languages": "Common, Minotaur, any one language"
"cr": "3"
"traits":
  - "desc": "The warrior has advantage on initiative rolls."
    "name": "Battle Readiness"
  - "desc": "Immediately after the warrior uses the Dash action on its turn and moves at least 20 feet, it can make one melee attack with its horns as a bonus action."
    "name": "Goring Rush"
  - "desc": "The warrior's attack rolls score a critical hit on a roll of 19 or 20 on the d20."
    "name": "Improved Critical"
"actions":
  - "desc": "The warrior can attack twice, instead of once, whenever it takes the Attack action on its turn."
    "name": "Extra Attack"
  - "desc": "_Melee Weapon Attack:_ +9 to hit, reach 5 ft., one target. _Hit:_ 7 (1d6 + 4) piercing damage, and the warrior can use a bonus action to attempt to shove that target with its horns. The target must be within 5 feet of the warrior and no more than one size larger than it. Unless the target succeeds on a DC 15 Strength saving throw, the warrior pushes it up to 10 feet away from the warrior."
    "name": "Horns"
  - "desc": "_Melee Weapon Attack:_ +9 to hit, reach 5 ft., one target. _Hit:_ 7 (1d6 + 4) piercing damage."
    "name": "Shortsword"
"source":
  - "TBVXI"
"image": "Compendium/bestiary/humanoid/token/borderland-minotaur-tbvxi.webp"
```
^statblock