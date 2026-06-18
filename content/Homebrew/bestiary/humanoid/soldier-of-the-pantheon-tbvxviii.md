---
title: Soldier of the Pantheon
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- src/5e/tbvxviii
- monster/cr/2
- monster/size/m
- monster/type/humanoid
statblock: inline
aliases: ["Soldier of the Pantheon"]
---
# Soldier of the Pantheon
*Source: Theros Bestiary TBVXVIII*  

<small><blockquote>"I hear the gods' voices in my dreams each night, and I offer bloody trophies on their altars each day."</blockquote></small>

![Soldier of the Pantheon](Homebrew/bestiary/humanoid/img/soldier-of-the-pantheon.webp#right|850)  

```statblock
"name": "Soldier of the Pantheon (TBVXVIII)"
"size": "Medium"
"type": "humanoid"
"subtype": "human"
"alignment": "Unaligned"
"ac": !!int "18"
"ac_class": "chain mail, shield"
"hp": !!int "15"
"hit_dice": "3d8 + 3"
"modifier": !!int "1"
"stats":
  - !!int "14"
  - !!int "13"
  - !!int "13"
  - !!int "11"
  - !!int "12"
  - !!int "12"
"speed": "30 ft."
"skillsaves":
  - "name": "[[skills#Athletics|Athletics]]"
    "desc": "+4"
  - "name": "[[skills#Perception|Perception]]"
    "desc": "+3"
"damage_resistances": "damage from magical attacks"
"senses": "passive Perception 10"
"languages": "Common"
"cr": "2"
"traits":
  - "desc": "The soldier has [[advantage-xphb|Advantage]] on saving throws against being [[conditions#Charmed|charmed]], [[conditions#Frightened|frightened]], [[conditions#Grappled|grappled]], or [[conditions#Restrained|restrained]] while it is within 5 feet of at least one ally."
    "name": "Formation Tactics"
"actions":
  - "desc": "The soldier makes two melee attacks."
    "name": "Multiattack"
  - "desc": "Melee Weapon Attack: +3 to hit, reach 5 ft., one target. Hit: 6 (1d8 + 2) slashing damage, or 7 (1d10 + 2) slashing damage if used with two hands."
    "name": "Longsword"
"source":
  - "TBVXVIII"
"image": "Homebrew/bestiary/humanoid/token/soldier-of-the-pantheon-tbvxviii.webp"
```
^statblock