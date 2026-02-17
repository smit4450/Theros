---
title: Leonin Snarecaster
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- src/5e/tbvxix
- monster/cr/1-4
- monster/size/m
- monster/type/humanoid
statblock: inline
aliases: ["Leonin Snarecaster"]
---
# Leonin Snarecaster
*Source: Theros Bestiary TBVXIX*  

<blockquote><small>Formerly oppressed by the polis of Meletis, leonin occasionally "mistake" their old enemies for game.</small></blockquote>

![Leonin Snarecaster](https://img.scryfall.com/cards/art_crop/front/a/d/ade9b739-122c-4659-b1b2-ea0510d96dbc.jpg?1562824726#right)  

```statblock
"name": "Leonin Snarecaster (TBVXIX)"
"size": "Medium"
"type": "humanoid"
"subtype": "leonin"
"alignment": "Any alignment"
"ac": !!int "11"
"ac_class": "padded"
"hp": !!int "12"
"hit_dice": "2d10 + 2"
"modifier": !!int "1"
"stats":
  - !!int "12"
  - !!int "13"
  - !!int "12"
  - !!int "10"
  - !!int "12"
  - !!int "10"
"speed": "35 ft."
"saves":
  - "strength": !!int "4"
  - "dexterity": !!int "4"
"skillsaves":
  - "name": "[[skills#Animal Handling|Animal Handling]]"
    "desc": "+4"
  - "name": "[[skills#Stealth|Stealth]]"
    "desc": "+4"
  - "name": "[[skills#Survival|Survival]]"
    "desc": "+4"
  - "name": "[[skills#Nature|Nature]]"
    "desc": "+3"
"senses": "[[senses#Darkvision|Darkvision]] 60 ft., passive Perception 10"
"languages": "Common, Leonin"
"cr": "1/4"
"traits":
  - "desc": "As a bonus action, the leonin can let out an especially menacing roar. Creatures of it chooses within 10 feet of itself that can hear it must succeed on a DC 11 Wisdom saving throw or become [[conditions#Frightened|frightened]] of it until the end of your next turn."
    "name": "Daunting Roar (Recharges after a Short or Long Rest)"
"actions":
  - "desc": "Ranged Weapon Attack: +5 to hit, range 30/60 ft., one target. Hit: 5 (1d8 + 1) piercing damage."
    "name": "Longbow"
  - "desc": "Melee Weapon Attack: +5 to hit, reach 5 ft., one target. Hit: 2 (1d4 + 0) slashing damage."
    "name": "Claws"
  - "desc": "Special Weapon Attack: +5 to hit, range 5/15 ft., one small or tiny target. The target is [[conditions#Restrained|restrained]] until freed. The net has no effect on creatures that are formless. A creature can use its action to make a DC 12 Strength check, freeing itself or another creature within its reach on a success. Dealing 5 slashing damage to the net (AC 10) also frees the creature without harming it, ending the effect and destroying the net."
    "name": "Cast Net"
"source":
  - "TBVXIX"
"image": "Compendium/bestiary/humanoid/token/leonin-snarecaster-tbvxix.webp"
```
^statblock