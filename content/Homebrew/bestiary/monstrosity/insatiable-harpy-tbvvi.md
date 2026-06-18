---
title: Insatiable Harpy
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- src/5e/tbvvi
- monster/cr/1-4
- monster/size/m
- monster/type/monstrosity
statblock: inline
aliases: ["Insatiable Harpy"]
---
# Insatiable Harpy
*Source: Theros Bestiary TBVVI*  

<small><blockquote>Gold coin, battered helmet, broken wrist bone-- all have the same value in the eyes of a harpy.</blockquote></small>

![Insatiable Harpy](Homebrew/bestiary/monstrosity/img/insatiable-harpy.webp#right)  

```statblock
"name": "Insatiable Harpy (TBVVI)"
"size": "Medium"
"type": "monstrosity"
"alignment": "Chaotic Evil"
"ac": !!int "10"
"hp": !!int "10"
"hit_dice": "2d8 + 2"
"modifier": !!int "1"
"stats":
  - !!int "12"
  - !!int "13"
  - !!int "12"
  - !!int "6"
  - !!int "11"
  - !!int "14"
"speed": "20 ft., fly 40 ft."
"skillsaves":
  - "name": "[[skills#Intimidation|Intimidation]]"
    "desc": "+4"
"senses": "passive Perception 10"
"languages": "Common"
"cr": "1/4"
"traits":
  - "desc": "The harpy has [[advantage-xphb|Advantage]] on saving throws against being [[conditions#Charmed|charmed]] or [[conditions#Frightened|frightened]]."
    "name": "Dark Devotion"
"actions":
  - "desc": "The harpy makes two melee attacks: one with its bite and one with its claws."
    "name": "Multiattack"
  - "desc": "Melee Weapon Attack: +3 to hit, reach 5 ft., one target. Hit: 3 (1d4 + 1) piercing damage. The harpy regains that many [[hit-points-xphb|Hit Points]]."
    "name": "Bite"
  - "desc": "Melee Weapon Attack: +3 to hit, reach 5 ft., one target. Hit: 3 (1d4 + 1) slashing damage."
    "name": "Claws"
"source":
  - "TBVVI"
"image": "Homebrew/bestiary/monstrosity/token/insatiable-harpy-tbvvi.webp"
```
^statblock