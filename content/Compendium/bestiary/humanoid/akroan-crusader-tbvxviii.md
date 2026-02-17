---
title: Akroan Crusader
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- src/5e/tbvxviii
- monster/cr/4
- monster/size/m
- monster/type/humanoid
statblock: inline
aliases: ["Akroan Crusader"]
---
# Akroan Crusader
*Source: Theros Bestiary TBVXVIII*  

<blockquote><small>An Akroan soldier’s worth is measured by the number of swords raised by his battle cry.</small></blockquote>

![Akroan Crusader](Compendium/bestiary/humanoid/img/akroan-crusader.webp#right|850)  

```statblock
"name": "Akroan Crusader (TBVXVIII)"
"size": "Medium"
"type": "humanoid"
"subtype": "human"
"alignment": "Any alignment"
"ac": !!int "18"
"ac_class": "breastplate, shield"
"hp": !!int "6"
"hit_dice": "1d8 + 2"
"modifier": !!int "3"
"stats":
  - !!int "16"
  - !!int "16"
  - !!int "14"
  - !!int "11"
  - !!int "14"
  - !!int "13"
"speed": "30 ft."
"saves":
  - "strength": !!int "5"
  - "dexterity": !!int "5"
"senses": "passive Perception 10"
"languages": "Common"
"cr": "4"
"actions":
  - "desc": "The crusader makes three melee attacks."
    "name": "Multiattack"
  - "desc": "_Melee Weapon Attack:_ +5 to hit, reach 5 ft., one target. _Hit:_ 6 (1d6 + 3) piercing damage."
    "name": "Shortsword"
  - "desc": "Melee Weapon Attack: +5 to hit, reach 5 ft., one creature. Hit: 5 (1d4 + 3) bludgeoning damage. If the target is a Medium or smaller creature, it must succeed on a DC 13 Strength saving throw or be knocked [[conditions#Prone|prone]]."
    "name": "Shield Bash"
"reactions":
  - "desc": "Whenever a spell targets the crusader, that spell's caster chooses whether the following happens: - The crusader summons an **Akroan crusade soldier** that appears in an unoccupied space that the crusader can see within 60 feet of itself. The summoned soldier acts as an ally to its summoner and its allies."
    "name": "Heroic"
"source":
  - "TBVXVIII"
"image": "Compendium/bestiary/humanoid/token/akroan-crusader-tbvxviii.webp"
```
^statblock