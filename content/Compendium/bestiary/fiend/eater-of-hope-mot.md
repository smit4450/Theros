---
title: Eater of Hope
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- src/5e/mot
- monster/cr/6
- monster/size/large
- monster/type/fiend
statblock: inline
aliases: ["Eater of Hope"]
---
# Eater of Hope
*Source: Mythic Odysseys of Theros p. 220*  

![](Compendium/bestiary/fiend/img/eater-of-hope.webp#right|850)  
An eater of hope is bitter to the core, resentful of all forms of life and joy. Although these demons can strike down most foes, they prefer to let terror and despair overtake their victims first, letting their victims marinate in fear before the fiend devours them.
```statblock
"name": "Eater of Hope (MOT)"
"size": "Large"
"type": "fiend"
"alignment": "Lawful Evil"
"ac": !!int "17"
"ac_class": "natural armor"
"hp": !!int "90"
"hit_dice": "12d10 + 24"
"modifier": !!int "3"
"stats":
  - !!int "19"
  - !!int "17"
  - !!int "14"
  - !!int "12"
  - !!int "11"
  - !!int "16"
"speed": "30 ft., fly 60 ft."
"saves":
  - "constitution": !!int "5"
  - "charisma": !!int "6"
"skillsaves":
  - "name": "[[skills#Deception|Deception]]"
    "desc": "+6"
  - "name": "[[skills#Intimidation|Intimidation]]"
    "desc": "+6"
  - "name": "[[skills#Persuasion|Persuasion]]"
    "desc": "+6"
"damage_resistances": "cold, necrotic"
"damage_immunities": "poison"
"condition_immunities": "[[conditions#Poisoned|poisoned]]"
"senses": "[[senses#Darkvision|darkvision]] 120 ft., passive Perception\
  \ 10"
"languages": "Abyssal, Common, Infernal"
"cr": "6"
"traits":
  - "desc": "The eater of hope can sense the presence of gold within 1,000 feet of\
      \ itself. It can determine which location has the greatest amount of gold and\
      \ can sense the direction to that site. If the gold is being moved, it knows\
      \ the direction of the movement. It can't locate gold if any thickness of clay\
      \ or lead, even a thin sheet, blocks a direct path between it and the gold."
    "name": "Insatiable Greed"
  - "desc": "The eater of hope has advantage on saving throws against spells and other\
      \ magical effects."
    "name": "Magic Resistance"
"actions":
  - "desc": "The eater of hope makes two attacks with its claws."
    "name": "Multiattack"
  - "desc": "*Melee Weapon Attack:* +7 to hit, reach 5 ft., one target. *Hit:* 8\
      \ (1d8 + 4) slashing damage plus 7 (2d6) necrotic damage."
    "name": "Claws"
  - "desc": "The eater of hope exhales a miasma of Underworld winds in a 30-foot cone.\
      \ Each creature in that area must make a DC 14 Charisma saving throw. On a failed\
      \ save, the target takes 26 (4d12) necrotic damage and is cursed for 1 minute.\
      \ While cursed in this way, the target takes an extra 6 (1d12) necrotic damage\
      \ whenever the eater of hope hits it with an attack. On a successful save, the\
      \ target takes half as much damage and isn't cursed."
    "name": "Breath of Hopelessness (Recharge 5-6)"
"source":
  - "MOT"
"image": "Compendium/bestiary/fiend/token/eater-of-hope-mot.webp"
```
^statblock