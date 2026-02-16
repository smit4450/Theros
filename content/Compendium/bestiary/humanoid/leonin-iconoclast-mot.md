---
title: Leonin Iconoclast
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- ttrpg-cli/compendium/src/5e/mot
- ttrpg-cli/monster/cr/5
- ttrpg-cli/monster/size/medium
- ttrpg-cli/monster/type/humanoid/leonin
statblock: inline
aliases: ["Leonin Iconoclast"]
---
# Leonin Iconoclast
*Source: Mythic Odysseys of Theros p. 232*  

![](Compendium/bestiary/humanoid/img/leonin-iconoclast.webp#right|850)  
While leonin don't deny the existence of the gods, most denounce them, believing the deities are more likely to spread doom than peace and bounty. Some leonin, known as iconoclasts, devote themselves to thwarting the gods by hunting down their followers and all things born of Nyx that impede on Oreskos and the safety of the leonin prides.

Prides of leonin roam the plains of Oreskos, protecting the land and its creatures from interlopers, both mortal and immortal. As many leonin suffered at the hands of archon tyrants in ages past, today their prides largely avoid contact with other peoples and spurn the gods that ignored their plight. Since then, the leonin have flourished, finding strength in their bonds with one another and the land. Only in recent times have some leonin started guardedly looking beyond their homeland and wondering what role they might take in the wider world.

Most leonin hunters are tribal warriors, but those who hunt the servants of the gods rather than game are known as leonin iconoclasts.
```statblock
"name": "Leonin Iconoclast (MOT)"
"size": "Medium"
"type": "humanoid"
"subtype": "leonin"
"alignment": "Any alignment"
"ac": !!int "17"
"ac_class": "Unarmored Defense"
"hp": !!int "67"
"hit_dice": "9d8 + 27"
"modifier": !!int "4"
"stats":
  - !!int "14"
  - !!int "18"
  - !!int "16"
  - !!int "13"
  - !!int "17"
  - !!int "10"
"speed": "40 ft."
"saves":
  - "dexterity": !!int "7"
  - "wisdom": !!int "6"
"skillsaves":
  - "name": "[[skills#Arcana|Arcana]]"
    "desc": "+4"
  - "name": "[[skills#Insight|Insight]]"
    "desc": "+6"
  - "name": "[[skills#Intimidation|Intimidation]]"
    "desc": "+3"
  - "name": "[[skills#Stealth|Stealth]]"
    "desc": "+7"
  - "name": "[[skills#Survival|Survival]]"
    "desc": "+6"
"senses": "[[senses#Darkvision|darkvision]] 60 ft., passive Perception\
  \ 13"
"languages": "Common, Leonin"
"cr": "5"
"traits":
  - "desc": "The leonin's spellcasting ability is Wisdom (spell save DC 14). It can\
      \ innately cast the following spells, requiring no material components:\n\n\
      **1/day each:** [[banishment-xphb|banishment]], [[detect-evil-and-good-xphb|detect\
      \ evil and good]]"
    "name": "Innate Spellcasting"
  - "desc": "If the leonin is subjected to an effect that allows it to make a Dexterity\
      \ saving throw to take only half damage, it instead takes no damage if it succeeds\
      \ on the saving throw, and only half damage if it fails. It can't use this trait\
      \ if it's [[conditions#Incapacitated|incapacitated]]."
    "name": "Evasion"
  - "desc": "While the leonin is wearing no armor and wielding no shield, its AC includes\
      \ its Wisdom modifier."
    "name": "Unarmored Defense"
"actions":
  - "desc": "The leonin makes three weapon attacks."
    "name": "Multiattack"
  - "desc": "*Melee Weapon Attack:* +7 to hit, reach 5 ft., one target. *Hit:* 11\
      \ (2d6 + 4) slashing damage plus 7 (2d6) force damage."
    "name": "Claws"
  - "desc": "*Ranged Weapon Attack:* +7 to hit, range 20/60 ft., one target. *Hit:*\
      \ 6 (1d4 + 4) piercing damage."
    "name": "Dart"
"source":
  - "MOT"
"image": "Compendium/bestiary/humanoid/token/leonin-iconoclast-mot.webp"
```
^statblock