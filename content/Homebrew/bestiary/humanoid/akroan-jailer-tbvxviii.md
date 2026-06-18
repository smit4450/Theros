---
title: Akroan Jailer
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- src/5e/tbvxviii
- monster/cr/2
- monster/size/m
- monster/type/humanoid
statblock: inline
aliases: ["Akroan Jailer"]
---
# Akroan Jailer
*Source: Theros Bestiary TBVXVIII*  

The jailer carries a set of *manacles* and a ring of keys.

>He ensures escape attempts are just that-- attempts.

![Akroan Jailer](Homebrew/bestiary/humanoid/img/akroan-jailer.webp#right)  

```statblock
"name": "Akroan Jailer (TBVXVIII)"
"size": "Medium"
"type": "humanoid"
"subtype": "human"
"alignment": "Any alignment"
"ac": !!int "15"
"hp": !!int "5"
"hit_dice": "1d8 + 1"
"modifier": !!int "2"
"stats":
  - !!int "13"
  - !!int "14"
  - !!int "13"
  - !!int "12"
  - !!int "13"
  - !!int "14"
"speed": "30 ft."
"saves":
  - "charisma": !!int "4"
  - "strength": !!int "3"
  - "dexterity": !!int "4"
  - "constitution": !!int "3"
"skillsaves":
  - "name": "[[skills#Athletics|Athletics]]"
    "desc": "+3"
  - "name": "[[skills#Insight|Insight]]"
    "desc": "+3"
  - "name": "[[skills#Perception|Perception]]"
    "desc": "+3"
"senses": "passive Perception 10"
"languages": "Common"
"cr": "2"
"traits":
  - "desc": "The jailer has [[advantage-xphb|Advantage]] on initiative rolls."
    "name": "Battle Readiness"
  - "desc": "The jailer has [[advantage-xphb|Advantage]] on saving throws against being [[conditions#Charmed|charmed]], [[conditions#Frightened|frightened]], [[conditions#Grappled|grappled]], or [[conditions#Restrained|restrained]]."
    "name": "Resilient"
  - "desc": "The jailer has [[advantage-xphb|Advantage]] on skill checks made for pursuing, apprehension, retaining, and escorting hostile creatures."
    "name": "Retainer"
"actions":
  - "desc": "The jailer makes two unarmed strikes"
    "name": "Multiattack"
  - "desc": "_Melee Weapon Attack:_ +3 to hit, reach 5 ft., one target. _Hit:_ 3 (1d4 + 1) bludgeoning damage."
    "name": "Unarmed Strike"
"source":
  - "TBVXVIII"
"image": "Homebrew/bestiary/humanoid/token/akroan-jailer-tbvxviii.webp"
```
^statblock