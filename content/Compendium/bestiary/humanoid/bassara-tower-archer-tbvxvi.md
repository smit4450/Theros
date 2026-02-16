---
title: Bassara Tower Archer
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- ttrpg-cli/compendium/src/5e/tbvxvi
- ttrpg-cli/monster/cr/2
- ttrpg-cli/monster/size/m
- ttrpg-cli/monster/type/humanoid
statblock: inline
aliases: ["Bassara Tower Archer"]
---
# Bassara Tower Archer
*Source: Theros Bestiary TBVXVI*  

<blockquote><small>Setessan warriors of Bassara Tower are known for their guerrilla tactics and skill with the bow. Interlopers into the Nessian Wood do not get far.</small></blockquote>

![Bassara Tower Archer](https://img.scryfall.com/cards/art_crop/front/9/5/95a1e5c2-7f5b-4ae4-83d9-06e334ba57ea.jpg?1593096148#right)  

```statblock
"name": "Bassara Tower Archer (TBVXVI)"
"size": "Medium"
"type": "humanoid"
"subtype": "human"
"alignment": "Any alignment"
"ac": !!int "13"
"ac_class": "leather"
"hp": !!int "5"
"hit_dice": "1d8 + 1"
"modifier": !!int "2"
"stats":
  - !!int "15"
  - !!int "15"
  - !!int "13"
  - !!int "11"
  - !!int "13"
  - !!int "11"
"speed": "30 ft."
"saves":
  - "constitution": !!int "4"
"skillsaves":
  - "name": "[[skills#Athletics|Athletics]]"
    "desc": "+5"
  - "name": "[[skills#Perception|Perception]]"
    "desc": "+4"
  - "name": "[[skills#Survival|Survival]]"
    "desc": "+4"
"senses": "passive Perception 10"
"languages": "Common, Any two languages"
"cr": "2"
"traits":
  - "desc": "The archer has [[advantage-xphb|Advantage]] on Dexterity (Stealth) checks made while in a wooded environment."
    "name": "Arbor Camouflage"
  - "desc": "The warrior has [[advantage-xphb|Advantage]] on initiative rolls."
    "name": "Battle Readiness"
  - "desc": "The warrior's attack rolls score a critical hit on a roll of 19 or 20 on the d20."
    "name": "Improved Critical"
"actions":
  - "desc": "The archer makes two longbow attacks."
    "name": "Extra Attack"
  - "desc": "_Ranged Weapon Attack:_ +4 to hit, range 150/600 ft., one target. _Hit:_ 6 (1d8 + 2) piercing damage."
    "name": "Longbow"
"reactions":
  - "desc": "The warrior imposes [[disadvantage-xphb|Disadvantage]] on the attack roll of a creature within 5 feet of it whose target isn't the warrior. The warrior must be able to see the attacker."
    "name": "Protection"
"source":
  - "TBVXVI"
"image": "Compendium/bestiary/humanoid/token/bassara-tower-archer-tbvxvi.webp"
```
^statblock