---
title: Aerie Worshiper
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- src/5e/tbvxiv
- monster/cr/0
- monster/size/m
- monster/type/humanoid
statblock: inline
aliases: ["Aerie Worshiper"]
---
# Aerie Worshiper
*Source: Theros Bestiary TBVXIV*  

<blockquote><small>They can conjure stars from a clear sky.</small></blockquote>

![Aerie Worshiper](Homebrew/bestiary/humanoid/img/aerie-worshiper.webp#right)  

```statblock
"name": "Aerie Worshiper (TBVXIV)"
"size": "Medium"
"type": "humanoid"
"subtype": "human"
"alignment": "Any alignment"
"ac": !!int "10"
"hp": !!int "35"
"hit_dice": "7d8 + 7"
"modifier": !!int "0"
"stats":
  - !!int "11"
  - !!int "11"
  - !!int "13"
  - !!int "14"
  - !!int "13"
  - !!int "14"
"speed": "30 ft."
"skillsaves":
  - "name": "[[skills#Medicine|Medicine]]"
    "desc": "+5"
  - "name": "[[skills#Persuasion|Persuasion]]"
    "desc": "+5"
  - "name": "[[skills#Religion|Religion]]"
    "desc": "+6"
"senses": "passive Perception 10"
"languages": "Common, any two languages"
"cr": "0"
"traits":
  - "desc": "At the beginning of the worshiper's turn, if a bird the worshiper bowed to at any point since the worshiper's last turn saw it doing so, that bird uses a bonus action to summons a **nyxborn eagle** that appears in an unoccupied space that the worshiper can see within 60 feet of itself. The summoned eagle acts as an ally to its summoner."
    "name": "Inspired"
"actions":
  - "desc": "_Melee Weapon Attack:_ +4 to hit, reach 5 ft., one target. _Hit:_ 3 (1d4+1) bludgeoning damage."
    "name": "Unarmed Strike"
  - "desc": "The worshiper bows down to any bird it can see that can see it. It remains in this position until a different action is used."
    "name": "Bow"
"source":
  - "TBVXIV"
"image": "Homebrew/bestiary/humanoid/token/aerie-worshiper-tbvxiv.webp"
```
^statblock