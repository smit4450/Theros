---
title: Disciple of Phenax
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- src/5e/tbvxxv
- monster/cr/1-2
- monster/size/m
- monster/type/humanoid
statblock: inline
aliases: ["Disciple of Phenax"]
---
# Disciple of Phenax
*Source: Theros Bestiary TBVXXV*  

Disciples of Phenax perform a ritual in which the name of a hated person is written on a piece of paper and a dagger is driven into it. This is accompanied by a prayer that that person die.

![Disciple of Phenax](Homebrew/bestiary/humanoid/img/disciple-of-phenax.webp#right)  

```statblock
"name": "Disciple of Phenax (TBVXXV)"
"size": "Medium"
"type": "humanoid"
"subtype": "human"
"alignment": "Lawful Evil"
"ac": !!int "10"
"hp": !!int "8"
"hit_dice": "2d8 + 0"
"modifier": !!int "0"
"stats":
  - !!int "11"
  - !!int "11"
  - !!int "11"
  - !!int "11"
  - !!int "15"
  - !!int "12"
"speed": "30 ft."
"saves":
  - "dexterity": !!int "2"
"skillsaves":
  - "name": "[[skills#Deception|Deception]]"
    "desc": "+3"
  - "name": "[[skills#Religion|Religion]]"
    "desc": "+2"
  - "name": "[[skills#Stealth|Stealth]]"
    "desc": "+2"
"senses": "passive Perception 10"
"languages": "Common, Any one language"
"cr": "1/2"
"traits":
  - "desc": "The disciple's innate spellcasting ability is Wisdom (spell save DC 12, +4 to hit with spell attacks). It can innately cast the following spells, requiring no material components: At will: [[light-xphb|Light]], [[sacred-flame-xphb|Sacred Flame]] 3/day: [[bless-xphb|Bless]], [[cure-wounds-xphb|Cure Wounds]], [[sanctuary-xphb|Sanctuary]]"
    "name": "Innate Spellcasting"
"actions":
  - "desc": "_Melee or Ranged Weapon Attack:_ +6 to hit, reach 5 ft. or range 20/60 ft., one target. _Hit:_ 4 (1d4 + 2) piercing damage."
    "name": "Dagger"
  - "desc": "The disciple writes the name of a person on a piece of paper, then drives a dagger through it, pinning it to a stone altar or temple belonging to Phenax. That person must succeed on a DC 5 Charisma saving throw or be killed instantly. A person whose name has been used in the last 24 hours is immune to this ritual."
    "name": "Ritual of Vengeance"
"source":
  - "TBVXXV"
"image": "Homebrew/bestiary/humanoid/token/disciple-of-phenax-tbvxxv.webp"
```
^statblock