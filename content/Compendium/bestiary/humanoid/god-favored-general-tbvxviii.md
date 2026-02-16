---
title: God-Favored General
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- ttrpg-cli/compendium/src/5e/tbvxviii
- ttrpg-cli/monster/cr/2
- ttrpg-cli/monster/size/m
- ttrpg-cli/monster/type/humanoid
statblock: inline
aliases: ["God-Favored General"]
---
# God-Favored General
*Source: Theros Bestiary TBVXVIII*  

<small><blockquote>Someone has to be first to attack, but he was not alone for long</blockquote></small>

![God-Favored General](Compendium/bestiary/humanoid/img/god-favored-general.webp#right|850)  

```statblock
"name": "God-Favored General (TBVXVIII)"
"size": "Medium"
"type": "humanoid"
"subtype": "human"
"alignment": "Any alignment"
"ac": !!int "18"
"ac_class": "breastplate, shield"
"hp": !!int "40"
"hit_dice": "8d8 + 8"
"modifier": !!int "1"
"stats":
  - !!int "13"
  - !!int "13"
  - !!int "13"
  - !!int "11"
  - !!int "14"
  - !!int "13"
"speed": "30 ft."
"saves":
  - "strength": !!int "3"
  - "dexterity": !!int "3"
"skillsaves":
  - "name": "[[skills#Persuasion|Persuasion]]"
    "desc": "+3"
"senses": "passive Perception 10"
"languages": "Common"
"cr": "2"
"traits":
  - "desc": "At the beginning of the general's turn, if Heliod saw it bowing at any point since the general's last turn, Heliod uses a bonus action to summon two **nyxborn soldiers** that appear in unoccupied spaces that the general can see within 60 feet of itself. The summoned soldiers act as allies to their summoner and to each other."
    "name": "Inspired"
"actions":
  - "desc": "The phalanx leader makes three melee attacks or two ranged attacks."
    "name": "Multiattack"
  - "desc": "Melee or Ranged Weapon Attack: +3 to hit, reach 5 ft., or range 20/60 ft., one target. Hit: 4 (1d6 + 1) piercing damage."
    "name": "Spear"
  - "desc": "Melee Weapon Attack: +3 to hit, reach 5 ft., one creature. Hit: 3 (1d4 + 1) bludgeoning damage. If the target is a Medium or smaller creature, it must succeed on a DC 11 Strength saving throw or be knocked [[conditions#Prone|prone]]."
    "name": "Shield Bash"
  - "desc": "The general bows down to any manifestation or statue of Heliod that it can see."
    "name": "Bow"
"source":
  - "TBVXVIII"
"image": "Compendium/bestiary/humanoid/token/god-favored-general-tbvxviii.webp"
```
^statblock