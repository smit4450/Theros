---
title: Omenspeaker
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- ttrpg-cli/compendium/src/5e/tbvxx
- ttrpg-cli/monster/cr/3
- ttrpg-cli/monster/size/m
- ttrpg-cli/monster/type/humanoid
statblock: inline
aliases: ["Omenspeaker"]
---
# Omenspeaker
*Source: Theros Bestiary TBVXX*  

<small><blockquote>Her prophecies amaze her even as she speaks them.</blockquote></small>

![Omenspeaker](Compendium/bestiary/humanoid/img/omenspeaker.webp#right|850)  

```statblock
"name": "Omenspeaker (TBVXX)"
"size": "Medium"
"type": "humanoid"
"subtype": "human"
"alignment": "Any alignment"
"ac": !!int "15"
"ac_class": "blessings of the gods"
"hp": !!int "25"
"hit_dice": "5d8 + 5"
"modifier": !!int "1"
"stats":
  - !!int "11"
  - !!int "13"
  - !!int "12"
  - !!int "14"
  - !!int "17"
  - !!int "16"
"speed": "30 ft."
"saves":
  - "wisdom": !!int "5"
  - "charisma": !!int "5"
"skillsaves":
  - "name": "[Insight](Compendium/rules/skills.md#Insight)"
    "desc": "+5"
  - "name": "[Persuasion](Compendium/rules/skills.md#Persuasion)"
    "desc": "+5"
  - "name": "[Religion](Compendium/rules/skills.md#Religion)"
    "desc": "+5"
"senses": "passive Perception 10"
"languages": "Celestial, Common, any one language"
"cr": "3"
"traits":
  - "desc": "While the omenspeaker is wearing no armor and wielding no shield, its AC includes its Wisdom modifier. In addition, a creature that hits the omenspeaker with a melee attack while within 5 feet of it takes 9 (2d8) force damage."
    "name": "Blessings of the Gods"
  - "desc": "The omenspeaker's innate spellcasting ability is Wisdom (spell save DC 13, +5 to hit with spell attacks). It can innately cast the following spells, requiring no material components: At will: _light_, _true strike_ 3/day: _augury_, _detect thoughts_, _identify_ 1/day: _commune_, _divination_, _scrying_"
    "name": "Innate Spellcasting"
  - "desc": "Just the omenspeaker seeks insights from interpreting the divine, so too do the gods occasionally seek to manipulate the world through the omenspeaker. Sometimes the gods might speak directly, be it with dramatic manifestations or direct possession of the omenspeaker. Although the gods' words might be steeped in metaphors, should they wish to make their intentions clear, they often finds dramatic ways to make their thoughts known."
    "name": "Divine Influence"
  - "desc": "The omenspeaker possesses unparalleled experience in divining godly whims from cryptic visions and mundane forces."
    "name": "Interpreter of Signs"
"actions":
  - "desc": "Melee Spell Attack: +5 to hit, reach 5 ft., one target. Hit: 6 (1d6 + 1) force damage."
    "name": "Eldritch Touch"
"reactions":
  - "desc": "When the omenspeaker or a creature it can see makes an attack roll, a saving throw, or an ability check, the omenspeaker can cause the roll to be made with advantage or disadvantage."
    "name": "Divine Insight (3/Day)"
"source":
  - "TBVXX"
"image": "Compendium/bestiary/humanoid/token/omenspeaker-tbvxx.webp"
```
^statblock