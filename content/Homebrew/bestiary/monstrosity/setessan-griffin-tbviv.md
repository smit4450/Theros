---
title: Setessan Griffin
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- src/5e/tbviv
- monster/cr/2
- monster/size/l
- monster/type/monstrosity
statblock: inline
aliases: ["Setessan Griffin"]
---
# Setessan Griffin
*Source: Theros Bestiary TBVIV*  

<small><blockquote>Most griffins must be caught and broken into the service of the polis. Not so in Setessa, where they volunteer.</blockquote></small>

![Setessan Griffin](Homebrew/bestiary/monstrosity/img/setessan-griffin.webp#right)  

```statblock
"name": "Setessan Griffin (TBVIV)"
"size": "Large"
"type": "monstrosity"
"alignment": "Unaligned"
"ac": !!int "12"
"hp": !!int "56"
"hit_dice": "7d10 + 21"
"modifier": !!int "2"
"stats":
  - !!int "20"
  - !!int "15"
  - !!int "16"
  - !!int "2"
  - !!int "13"
  - !!int "8"
"speed": "30 ft., fly 80 ft."
"skillsaves":
  - "name": "[[skills#Perception|Perception]]"
    "desc": "+3"
"senses": "[[senses#Darkvision|Darkvision]] 60 ft., passive Perception 10"
"languages": ""
"cr": "2"
"traits":
  - "desc": "The griffin has [[advantage-xphb|Advantage]] on Wisdom (Perception) checks that rely on sight."
    "name": "Keen Sight"
  - "desc": "At the beginning of every creature's turn that the griffin can see a Setessan creature, it gains 20 temporary [[hit-points-xphb|Hit Points]] for the duration of that turn and its attacks deal 50% more damage, rounded up."
    "name": "Eager Servitor"
"actions":
  - "desc": "The griffin makes two attacks: one with its beak and one with its claws."
    "name": "Multiattack"
  - "desc": "Melee Weapon Attack: +7 to hit, reach 5 ft., one target. Hit: 9 (1d8 + 5) piercing damage."
    "name": "Beak"
  - "desc": "Melee Weapon Attack: +7 to hit, reach 5 ft., one target. Hit: 12 (2d6 + 5) slashing damage."
    "name": "Claws"
"source":
  - "TBVIV"
"image": "Homebrew/bestiary/monstrosity/token/setessan-griffin-tbviv.webp"
```
^statblock