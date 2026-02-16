---
title: Kragma Warcaller
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- ttrpg-cli/compendium/src/5e/tbvxi
- ttrpg-cli/monster/cr/2
- ttrpg-cli/monster/size/m
- ttrpg-cli/monster/type/humanoid
statblock: inline
aliases: ["Kragma Warcaller"]
---
# Kragma Warcaller
*Source: Theros Bestiary TBVXI*  

<blockquote><small>A warcaller merely brings the herd together. After that, the meat-hunger is all the encouragement they need.</small></blockquote>

![Kragma Warcaller](https://img.scryfall.com/cards/art_crop/front/7/8/78791fc6-054f-45eb-b8b0-28f2512d72b6.jpg?1562820128#right)  

```statblock
"name": "Kragma Warcaller (TBVXI)"
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
  - !!int "15"
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
    "desc": "+4"
  - "name": "[Perception](Compendium/rules/skills.md#Perception)"
    "desc": "+3"
  - "name": "[Survival](Compendium/rules/skills.md#Survival)"
    "desc": "+3"
  - "name": "[Persuasion](Compendium/rules/skills.md#Persuasion)"
    "desc": "+2"
"senses": "passive Perception 10"
"languages": "Common, Minotaur, any one language"
"cr": "2"
"traits":
  - "desc": "The warrior has [Advantage](Compendium/rules/variant-rules/advantage-xphb.md) on initiative rolls."
    "name": "Battle Readiness"
  - "desc": "Immediately after the warrior uses the Dash action on its turn and moves at least 20 feet, it can make one melee attack with its horns as a bonus action."
    "name": "Goring Rush"
  - "desc": "The warrior's attack rolls score a critical hit on a roll of 19 or 20 on the d20."
    "name": "Improved Critical"
  - "desc": "The minotaur starves itself prior to battle. If it kills a creature and has not eaten, there is a 50% chance it will stop fighting to eat the corpse. If the minotaur eats, each hostile creature that can see it must succeed on a DC 11 Wisdom saving throw or be [frightened](Compendium/rules/conditions.md#Frightened) of the minotaur until the end of the minotaur's next turn. If a hungry minotaur does not eat after a kill, it gets a +1 bonus to damage rolls until it eats."
    "name": "Ragegore Hunger"
  - "desc": "Other minotaur creatures within 30 feet of the warcaller that can see or hear it have [Advantage](Compendium/rules/variant-rules/advantage-xphb.md) on initiative rolls and have a +2 bonus on damage rolls and Strength and Dexterity checks."
    "name": "Rallying War Cry"
"actions":
  - "desc": "The warrior can attack twice, instead of once, whenever it takes the Attack action on its turn."
    "name": "Extra Attack"
  - "desc": "_Melee Weapon Attack:_ +7 to hit, reach 5 ft., one target. _Hit:_ 5 (1d6 + 2) piercing damage, and the warrior can use a bonus action to attempt to shove that target with its horns. The target must be within 5 feet of the warrior and no more than one size larger than it. Unless the target succeeds on a DC 13 Strength saving throw, the warrior pushes it up to 10 feet away from the warrior."
    "name": "Horns"
  - "desc": "_Melee Weapon Attack:_ +7 to hit, reach 10 ft., one target. _Hit:_ 6 (1d8 + 2) piercing damage, or 7 (1d10 + 2) piercing damage if used with two hands to make a melee attack."
    "name": "War pick"
"source":
  - "TBVXI"
"image": "Compendium/bestiary/humanoid/token/kragma-warcaller-tbvxi.webp"
```
^statblock