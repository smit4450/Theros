---
title: Flurrying Minotaur
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- ttrpg-cli/compendium/src/5e/tbvxi
- ttrpg-cli/monster/cr/2
- ttrpg-cli/monster/size/m
- ttrpg-cli/monster/type/humanoid
statblock: inline
aliases: ["Flurrying Minotaur"]
---
# Flurrying Minotaur
*Source: Theros Bestiary TBVXI*  

<blockquote><small>A minotaur does not distinguish between human, satyr, and triton. They are all meat.</small></blockquote>

![Flurrying Minotaur](https://img.scryfall.com/cards/art_crop/front/5/d/5d2a3833-ab5b-4f84-b39c-d0eeb7b474d3.jpg?1561757242#right)  

```statblock
"name": "Flurrying Minotaur (TBVXI)"
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
  - !!int "12"
  - !!int "10"
"speed": "30 ft."
"saves":
  - "constitution": !!int "5"
"skillsaves":
  - "name": "[[skills#Athletics|Athletics]]"
    "desc": "+4"
  - "name": "[[skills#Perception|Perception]]"
    "desc": "+3"
  - "name": "[[skills#Survival|Survival]]"
    "desc": "+3"
  - "name": "[[skills#Intimidation|Intimidation]]"
    "desc": "+2"
"senses": "passive Perception 10"
"languages": "Common, Minotaur, any one language"
"cr": "2"
"traits":
  - "desc": "The minotaur has [[advantage-xphb|Advantage]] on initiative rolls."
    "name": "Battle Readiness"
  - "desc": "Immediately after the minotaur uses the Dash action on its turn and moves at least 20 feet, it can make one melee attack with its horns as a bonus action."
    "name": "Goring Rush"
  - "desc": "The minotaur's attack rolls score a critical hit on a roll of 19 or 20 on the d20."
    "name": "Improved Critical"
  - "desc": "The minotaur starves itself prior to battle. If it kills a creature and has not eaten, there is a 50% chance it will stop fighting to eat the corpse. If the minotaur eats, each hostile creature that can see it must succeed on a DC 11 Wisdom saving throw or be [[conditions#Frightened|frightened]] of the minotaur until the end of the minotaur's next turn. If a hungry minotaur does not eat after a kill, it gets a +1 bonus to damage rolls until it eats."
    "name": "Ragegore Hunger"
"actions":
  - "desc": "The minotaur makes two attacks."
    "name": "Multiattack"
  - "desc": "_Melee Weapon Attack:_ +6 to hit, reach 5 ft., one target. _Hit:_ 5 (1d6 + 2) piercing damage, and the minotaur can use a bonus action to attempt to shove that target with its horns. The target must be within 5 feet of the minotaur and no more than one size larger than it. Unless the target succeeds on a DC 12 Strength saving throw, the minotaur pushes it up to 10 feet away from the minotaur."
    "name": "Horns"
  - "desc": "_Melee Weapon Attack:_ +4 to hit, reach 5 ft., one target. _Hit:_ 5 (1d6 + 2) bludgeoning damage."
    "name": "Mace"
"source":
  - "TBVXI"
"image": "Compendium/bestiary/humanoid/token/flurrying-minotaur-tbvxi.webp"
```
^statblock