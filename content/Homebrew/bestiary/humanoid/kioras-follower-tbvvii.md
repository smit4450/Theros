---
title: Kiora's Follower
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- src/5e/tbvvii
- monster/cr/0
- monster/size/m
- monster/type/humanoid
statblock: inline
aliases: ["Kiora's Follower"]
---
# Kiora's Follower
*Source: Theros Bestiary TBVVII*  

<blockquote><small>“She may call herself Kiora but I believe she is Thassa, the embodiment of the sea and empress of the depths.”</small></blockquote>

![Kiora's Follower](Homebrew/bestiary/humanoid/img/kioras-follower.webp#right|850)  

```statblock
"name": "Kiora's Follower (TBVVII)"
"size": "Medium"
"type": "humanoid"
"subtype": "triton"
"alignment": "Neutral"
"ac": !!int "10"
"hp": !!int "10"
"hit_dice": "2d8 + 2"
"modifier": !!int "0"
"stats":
  - !!int "12"
  - !!int "10"
  - !!int "12"
  - !!int "10"
  - !!int "11"
  - !!int "12"
"speed": "30 ft., swim 30 ft."
"skillsaves":
  - "name": "[[skills#Religion|Religion]]"
    "desc": "+2"
"damage_resistances": "cold"
"senses": "[[senses#Darkvision|Darkvision]] 60 ft., passive Perception 10"
"languages": "Common, Primordial"
"cr": "0"
"traits":
  - "desc": "The triton can breathe air and water."
    "name": "Amphibious"
  - "desc": "The triton can communicate simple ideas with beasts that can breathe water. They can understand its words, though it has no special ability to understand them in return."
    "name": "Emissary of the Sea"
  - "desc": "The kiora's follower's innate spellcasting ability is Charisma (spell save DC 11, +3 to hit with spell attacks). It can innately cast the following spells, requiring no material components: 3/day: [[fog-cloud-xphb|Fog Cloud]]"
    "name": "Innate Spellcasting"
"actions":
  - "desc": "The triton makes two trident attacks."
    "name": "Multiattack"
  - "desc": "_Melee or Ranged Weapon Attack:_ +3 to hit, reach 5 ft. or range 20/60 ft., one target. _Hit:_ 4 (1d6 + 1) piercing damage in melee."
    "name": "Trident"
  - "desc": "The triton bows down to any creature that it can see. It remains in this position until a different action is used. As long as the triton is bowing to that creature, that creature may make an additional attack as a bonus action on its turn."
    "name": "Bow"
"source":
  - "TBVVII"
"image": "Homebrew/bestiary/humanoid/token/kioras-follower-tbvvii.webp"
```
^statblock