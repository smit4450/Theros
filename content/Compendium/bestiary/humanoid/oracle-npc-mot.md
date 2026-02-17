---
title: Oracle
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- src/5e/mot
- monster/cr/4
- monster/size/medium
- monster/type/humanoid
statblock: inline
aliases: ["Oracle"]
---
# Oracle
*Source: Mythic Odysseys of Theros p. 238*  

![](Compendium/bestiary/humanoid/img/oracle.webp#right|850)  
Oracles posses the ability to interpret the patterns and language of Nyx, divining from it the flow of fates and the will of the gods. Most of these gifted—or cursed—mortals communicate with a single god, interpreting their intentions for the wider world. Others aren't aligned with a god and observe the night sky, reading Nyx like a vast, cryptic scroll for insights.
```statblock
"name": "Oracle (MOT)"
"size": "Medium"
"type": "humanoid"
"alignment": "Any alignment"
"ac": !!int "15"
"ac_class": "Blessings Of The Gods"
"hp": !!int "44"
"hit_dice": "8d8 + 8"
"modifier": !!int "2"
"stats":
  - !!int "10"
  - !!int "14"
  - !!int "12"
  - !!int "13"
  - !!int "16"
  - !!int "15"
"speed": "30 ft."
"saves":
  - "wisdom": !!int "5"
  - "charisma": !!int "4"
"skillsaves":
  - "name": "[[skills#Insight|Insight]]"
    "desc": "+5"
  - "name": "[[skills#Persuasion|Persuasion]]"
    "desc": "+4"
  - "name": "[[skills#Religion|Religion]]"
    "desc": "+5"
"senses": "passive Perception 13"
"languages": "Celestial, Common"
"cr": "4"
"traits":
  - "desc": "The oracle's spellcasting ability is Wisdom (spell save DC 13, +5 to\
      \ hit with spell attacks). It can innately cast the following spells, requiring\
      \ no material components:\n\n**At will:** [[guidance-xphb|guidance]],\
      \ [[light-xphb|light]], [[thaumaturgy-xphb|thaumaturgy]]\n\
      \n**3/day each:** [[bless-xphb|bless]], [[guiding-bolt-xphb|guiding bolt]],\
      \ [[healing-word-xphb|healing word]], [[hold-person-xphb|hold person]]\n\
      \n**1/day each:** [[augury-xphb|augury]], [[scrying-xphb|scrying]]"
    "name": "Innate Spellcasting"
  - "desc": "While the oracle is wearing no armor and wielding no shield, its AC includes\
      \ its Wisdom modifier. In addition, a creature that hits the oracle with a melee\
      \ attack while within 5 feet of it takes 9 (2d8) force damage."
    "name": "Blessings of the Gods"
"actions":
  - "desc": "*Melee Spell Attack:* +5 to hit, reach 5 ft., one target. *Hit:* 6\
      \ (1d6 + 3) force damage."
    "name": "Eldritch Touch"
"reactions":
  - "desc": "When the oracle or a creature it can see makes an attack roll, a saving\
      \ throw, or an ability check, the oracle can cause the roll to be made with\
      \ advantage or disadvantage."
    "name": "Divine Insight (3/Day)"
"source":
  - "MOT"
"image": "Compendium/bestiary/humanoid/token/oracle-mot.webp"
```
^statblock