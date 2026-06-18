---
title: Dakra Mystic
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- src/5e/tbvxx
- monster/cr/1
- monster/size/m
- monster/type/humanoid
statblock: inline
aliases: ["Dakra Mystic"]
---
# Dakra Mystic
*Source: Theros Bestiary TBVXX*  

<blockquote><small>Choices are rarely as simple as they seem.</small></blockquote>

![Dakra Mystic](Homebrew/bestiary/humanoid/img/dakra-mystic.webp#right)  

```statblock
"name": "Dakra Mystic (TBVXX)"
"size": "Medium"
"type": "humanoid"
"subtype": "triton"
"alignment": "Neutral"
"ac": !!int "15"
"ac_class": "blessings of the gods"
"hp": !!int "40"
"hit_dice": "8d8 + 8"
"modifier": !!int "2"
"stats":
  - !!int "11"
  - !!int "14"
  - !!int "13"
  - !!int "13"
  - !!int "16"
  - !!int "13"
"speed": "30 ft., swim 30 ft."
"saves":
  - "wisdom": !!int "5"
  - "charisma": !!int "3"
"skillsaves":
  - "name": "[[skills#Insight|Insight]]"
    "desc": "+5"
  - "name": "[[skills#Persuasion|Persuasion]]"
    "desc": "+3"
  - "name": "[[skills#Religion|Religion]]"
    "desc": "+5"
"damage_resistances": "cold"
"senses": "[[senses#Darkvision|Darkvision]] 60 ft., passive Perception 10"
"languages": "Celestial, Common, Primordial"
"cr": "1"
"traits":
  - "desc": "The mystic can breathe air and water."
    "name": "Amphibious"
  - "desc": "While the mystic is wearing no armor and wielding no shield, its AC includes its Wisdom modifier. In addition, a creature that hits the mystic with a melee attack while within 5 feet of it takes 9 (2d8) force damage."
    "name": "Blessings of the Gods"
  - "desc": "Just the mystic seeks insights from interpreting the divine, so too does Thassa occasionally seek to manipulate the world through the mystic . Sometimes Thassa might speak directly, be it with dramatic manifestations or direct possession of the mystic. Although Thassa's words might be steeped in metaphors, should she wish to make her intentions clear, she often finds dramatic ways to make her thoughts known."
    "name": "Divine Influence"
  - "desc": "The mystic can communicate simple ideas with beasts that can breathe water. They can understand its words, though it has no special ability to understand them in return."
    "name": "Emissary of the Sea"
  - "desc": "The mystic's innate spellcasting ability is Charisma (spell save DC 11, +3 to hit with spell attacks). It can innately cast the following spells, requiring no material components: 1/day: [[fog-cloud-xphb|Fog Cloud]], [[gust-of-wind-xphb|Gust Of Wind]], _wall of water_"
    "name": "Innate Spellcasting"
  - "desc": "The mystic possesses unparalleled experience in divining godly whims from cryptic visions and mundane forces."
    "name": "Interpreter of Signs"
  - "desc": "As an oracle of Thassa, the mystic is able to carry out negotiations between her clients and the goddess of the sea. Thassa is often willing to adjust her plans, provided the mystic collects payment in advance."
    "name": "Negotiate with Thassa"
"actions":
  - "desc": "Melee Spell Attack: +3 to hit, reach 5 ft., one target. Hit: 4 (1d6 + 1) force damage."
    "name": "Eldritch Touch"
"reactions":
  - "desc": "When the mystic or a creature it can see makes an attack roll, a saving throw, or an ability check, the mystic can cause the roll to be made with [[advantage-xphb|Advantage]] or [[disadvantage-xphb|Disadvantage]]."
    "name": "Divine Insight (3/Day)"
"source":
  - "TBVXX"
"image": "Homebrew/bestiary/humanoid/token/dakra-mystic-tbvxx.webp"
```
^statblock