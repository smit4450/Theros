---
title: Akroan Phalanx Hoplite
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- ttrpg-cli/compendium/src/5e/tbvxviii
- ttrpg-cli/monster/cr/3
- ttrpg-cli/monster/size/m
- ttrpg-cli/monster/type/humanoid
statblock: inline
aliases: ["Akroan Phalanx Hoplite"]
---
# Akroan Phalanx Hoplite
*Source: Theros Bestiary TBVXVIII*  

<blockquote><small>Shields up, spears out, heels set, hearts firm.</small></blockquote>

![Akroan Phalanx Hoplite](https://img.scryfall.com/cards/art_crop/front/f/e/fe23019a-e432-4a27-8acb-b17728a1e8b0.jpg?1578451516#right)  

```statblock
"name": "Akroan Phalanx Hoplite (TBVXVIII)"
"size": "Medium"
"type": "humanoid"
"subtype": "human"
"alignment": "Any alignment"
"ac": !!int "18"
"ac_class": "breastplate, shield"
"hp": !!int "56"
"hit_dice": "8d8 + 24"
"modifier": !!int "3"
"stats":
  - !!int "16"
  - !!int "16"
  - !!int "16"
  - !!int "11"
  - !!int "14"
  - !!int "13"
"speed": "30 ft."
"saves":
  - "strength": !!int "5"
  - "dexterity": !!int "5"
"damage_resistances": "bludgeoning, piercing, and slashing from nonmagical attacks"
"senses": "passive Perception 10"
"languages": "Common"
"cr": "3"
"traits":
  - "desc": "While the hoplite is holding a spear, other creatures provoke an opportunity attack from the hoplite when they move within 5 feet of it. When the hoplite hits a creature with an opportunity attack using its spear, the creature takes an extra 4 (1d8) piercing damage, and the creature’s speed becomes 0 for the rest of the turn."
    "name": "Hold the Line"
  - "desc": "The hoplite can't be surprised."
    "name": "Vigilant"
  - "desc": "The hoplite and all allied creatures forming a phalanx with it (an unbroken line without any five-foot or larger gaps) have a +1 damage roll bonus."
    "name": "Phalanx Tactics"
"actions":
  - "desc": "The hoplite makes three melee attacks or two ranged attacks."
    "name": "Multiattack"
  - "desc": "Melee or Ranged Weapon Attack: +5 to hit, reach 5 ft., or range 20/60 ft., one target. Hit: 6 (1d6 + 3) piercing damage, or 7 (1d8 + 3) piercing damage if used with two hands to make a melee attack."
    "name": "Spear"
  - "desc": "Melee Weapon Attack: +5 to hit, reach 5 ft., one creature. Hit: 5 (1d4 + 3) bludgeoning damage. If the target is a Medium or smaller creature, it must succeed on a DC 13 Strength saving throw or be knocked [[conditions#Prone|prone]]."
    "name": "Shield Bash"
"source":
  - "TBVXVIII"
"image": "Compendium/bestiary/humanoid/token/akroan-phalanx-hoplite-tbvxviii.webp"
```
^statblock