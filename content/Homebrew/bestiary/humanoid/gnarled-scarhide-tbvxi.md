---
title: Gnarled Scarhide
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- src/5e/tbvxi
- monster/cr/1-8
- monster/size/m
- monster/type/humanoid
statblock: inline
aliases: ["Gnarled Scarhide"]
---
# Gnarled Scarhide
*Source: Theros Bestiary TBVXI*  



![Gnarled Scarhide](Homebrew/bestiary/humanoid/img/gnarled-scarhide.webp#right|850)  

```statblock
"name": "Gnarled Scarhide (TBVXI)"
"size": "Medium"
"type": "humanoid"
"subtype": "minotaur"
"alignment": "Any alignment"
"ac": !!int "10"
"hp": !!int "5"
"hit_dice": "1d8 + 1"
"modifier": !!int "0"
"stats":
  - !!int "14"
  - !!int "10"
  - !!int "12"
  - !!int "10"
  - !!int "10"
  - !!int "10"
"speed": "30 ft."
"skillsaves":
  - "name": "[[skills#Intimidation|Intimidation]]"
    "desc": "+2"
"senses": "passive Perception 10"
"languages": "Common, Minotaur"
"cr": "1/8"
"traits":
  - "desc": "The minotaur can't make opportunity attacks."
    "name": "Gnarled"
  - "desc": "The minotaur has [[advantage-xphb|Advantage]] on saving throws against spells and other magical effects."
    "name": "Magic Resistance"
  - "desc": "The minotaur's weapon attacks are magical."
    "name": "Magic Weapons"
  - "desc": "The minotaur glows with the soft light of the night sky, shedding dim light in a 15-foot radius."
    "name": "Starlight Form"
"actions":
  - "desc": "Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 2 (1d4) piercing damage."
    "name": "Unarmed Strike"
  - "desc": "Melee Weapon Attack: +4 to hit, reach 5 ft., one target. Hit: 3 (1d4 + 1) piercing damage, and it can use a bonus action to attempt to shove that target with its horn. The target must be within 5 feet of the minotaur and no more than one size larger than it. Unless the target succeeds on a DC 12 Strength saving throw, the minotaur pushes it up to 10 feet away from the minotaur."
    "name": "Horn"
"reactions":
  - "desc": "Immediately after the minotaur uses the Dash action on its turn and moves at least 20 feet, it can make one melee attack with its horn as a bonus action."
    "name": "Goring Rush"
"source":
  - "TBVXI"
"image": "Homebrew/bestiary/humanoid/token/gnarled-scarhide-tbvxi.webp"
```
^statblock