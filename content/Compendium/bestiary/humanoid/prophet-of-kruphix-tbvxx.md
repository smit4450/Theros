---
title: Prophet of Kruphix
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- src/5e/tbvxx
- monster/cr/4
- monster/size/m
- monster/type/humanoid
statblock: inline
aliases: ["Prophet of Kruphix"]
---
# Prophet of Kruphix
*Source: Theros Bestiary TBVXX*  

<blockquote><small>"Time is fluid as a dance, and truth as fleeting."</small></blockquote>

![Prophet of Kruphix](Compendium/bestiary/humanoid/img/prophet-of-kruphix.webp#right|850)  

```statblock
"name": "Prophet of Kruphix (TBVXX)"
"size": "Medium"
"type": "humanoid"
"subtype": "human"
"alignment": "Any alignment"
"ac": !!int "15"
"ac_class": "blessings of the gods"
"hp": !!int "40"
"hit_dice": "8d8 + 8"
"modifier": !!int "2"
"stats":
  - !!int "11"
  - !!int "15"
  - !!int "13"
  - !!int "14"
  - !!int "17"
  - !!int "16"
"speed": "30 ft."
"saves":
  - "wisdom": !!int "5"
  - "charisma": !!int "5"
"skillsaves":
  - "name": "[[skills#Insight|Insight]]"
    "desc": "+5"
  - "name": "[[skills#Persuasion|Persuasion]]"
    "desc": "+5"
  - "name": "[[skills#Religion|Religion]]"
    "desc": "+6"
  - "name": "[[skills#Perception|Perception]]"
    "desc": "+5"
"senses": "passive Perception 10"
"languages": "Celestial, Common, any one language"
"cr": "4"
"traits":
  - "desc": "While the prophet is wearing no armor and wielding no shield, its AC includes its Wisdom modifier. In addition, a creature that hits the prophet with a melee attack while within 5 feet of it takes 9 (2d8) force damage."
    "name": "Blessings of the Gods"
  - "desc": "Just the prophet seeks insights from interpreting the divine, so too does Kruphix occasionally seek to manipulate the world through the prophet. Sometimes Kruphix might speak directly, be it with dramatic manifestations or direct possession of the prophet. Although Kruphix’s words might be steeped in metaphors, should he wish to make his intentions clear, he often finds dramatic ways to make his thoughts known."
    "name": "Divine Influence"
  - "desc": "The prophet's innate spellcasting ability is Wisdom (spell save DC 13, +5 to hit with spell attacks). It can innately cast the following spells, requiring no material components: At will: _guidance_, [[light-xphb|Light]], [[thaumaturgy-xphb|Thaumaturgy]] 3/day: [[bless-xphb|Bless]], [[slow-xphb|Slow]], [[healing-word-xphb|Healing Word]], [[hold-person-xphb|Hold Person]] 1/day: [[augury-xphb|Augury]], [[scrying-xphb|Scrying]], [[time-stop-xphb|Time Stop]]"
    "name": "Innate Spellcasting"
  - "desc": "The prophet possesses unparalleled experience in divining Kruphix's whims from cryptic visions and mundane forces."
    "name": "Interpreter of Signs"
"actions":
  - "desc": "Melee Spell Attack: +5 to hit, reach 5 ft., one target. Hit: 6 (1d6 + 3) force damage."
    "name": "Eldritch Touch"
"reactions":
  - "desc": "When the oracle or a creature it can see makes an attack roll, a saving throw, or an ability check, the oracle can cause the roll to be made with [[advantage-xphb|Advantage]] or [[disadvantage-xphb|Disadvantage]]."
    "name": "Divine Insight (3/Day)"
"source":
  - "TBVXX"
"image": "Compendium/bestiary/humanoid/token/prophet-of-kruphix-tbvxx.webp"
```
^statblock