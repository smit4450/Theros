---
title: Akroan Conscriptor
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- src/5e/tbvxvi
- monster/cr/2
- monster/size/m
- monster/type/humanoid
statblock: inline
aliases: ["Akroan Conscriptor"]
---
# Akroan Conscriptor
*Source: Theros Bestiary TBVXVI*  

<blockquote><small>“The time to serve is now.”</small></blockquote>

![Akroan Conscriptor](Homebrew/bestiary/humanoid/img/akroan-conscriptor.webp#right|850)  

```statblock
"name": "Akroan Conscriptor (TBVXVI)"
"size": "Medium"
"type": "humanoid"
"subtype": "human"
"alignment": "Lawful Evil"
"ac": !!int "16"
"ac_class": "mage armor"
"hp": !!int "12"
"hit_dice": "2d8 + 4"
"modifier": !!int "2"
"stats":
  - !!int "16"
  - !!int "14"
  - !!int "14"
  - !!int "16"
  - !!int "12"
  - !!int "11"
"speed": "30 ft."
"saves":
  - "intelligence": !!int "5"
  - "wisdom": !!int "3"
"skillsaves":
  - "name": "[[skills#Arcana|Arcana]]"
    "desc": "+5"
  - "name": "[[skills#History|History]]"
    "desc": "+5"
  - "name": "[[skills#Persuasion|Persuasion]]"
    "desc": "+2"
  - "name": "[[skills#Deception|Deception]]"
    "desc": "+2"
"condition_immunities": "[[conditions#Charmed|charmed]]"
"senses": "passive Perception 10"
"languages": "Common, Any three languages"
"cr": "2"
"actions":
  - "desc": "_Melee Weapon Attack:_ +5 to hit, reach 10 ft., one target. _Hit:_ 12 (2d8 + 3) slashing damage."
    "name": "Whip"
"reactions":
  - "desc": "Whenever the conscriptor becomes targeted by a spell, that spell's caster chooses whether the following happens: - The conscriptor's red crystal ball becomes wreathed with electricity, and it chooses a creature it can see. Until the end of the conscriptor's next turn, that creature becomes [[conditions#Charmed|charmed]] and has a +2 initiative bonus. This effect ends prematurely if the conscriptor loses contact with its ball."
    "name": "Heroic"
"source":
  - "TBVXVI"
"image": "Homebrew/bestiary/humanoid/token/akroan-conscriptor-tbvxvi.webp"
```
^statblock