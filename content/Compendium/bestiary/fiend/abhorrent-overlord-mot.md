---
title: Abhorrent Overlord
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- src/5e/mot
- monster/cr/9
- monster/size/large
- monster/type/fiend
statblock: inline
aliases: ["Abhorrent Overlord"]
---
# Abhorrent Overlord
*Source: Mythic Odysseys of Theros p. 219*  

![](Compendium/bestiary/fiend/img/abhorrent-overlord.webp#right|850)  
Abhorrent overlords are gaunt, bipedal creatures whose gray, leathery skin is in stark contrast to the gleaming jewelry made of Underworld gold that they adorn themselves with. Their appetite for pain and death is eclipsed only by their greed; these fiends delight in searching out treasure and slaughtering all who stand in their way.
```statblock
"name": "Abhorrent Overlord (MOT)"
"size": "Large"
"type": "fiend"
"alignment": "Lawful Evil"
"ac": !!int "16"
"ac_class": "natural armor"
"hp": !!int "136"
"hit_dice": "16d10 + 48"
"modifier": !!int "4"
"stats":
  - !!int "20"
  - !!int "18"
  - !!int "16"
  - !!int "15"
  - !!int "14"
  - !!int "16"
"speed": "30 ft., fly 60 ft."
"saves":
  - "constitution": !!int "7"
  - "charisma": !!int "7"
"skillsaves":
  - "name": "[[skills#Deception|Deception]]"
    "desc": "+7"
  - "name": "[[skills#Intimidation|Intimidation]]"
    "desc": "+7"
  - "name": "[[skills#Persuasion|Persuasion]]"
    "desc": "+7"
"damage_resistances": "cold, necrotic"
"damage_immunities": "poison"
"condition_immunities": "[[conditions#Poisoned|poisoned]]"
"senses": "[[senses#Darkvision|darkvision]] 120 ft., passive Perception\
  \ 12"
"languages": "Abyssal, Common, Infernal"
"cr": "9"
"traits":
  - "desc": "The abhorrent overlord's spellcasting ability is Charisma (spell save\
      \ DC 15). It can innately cast the following spells, requiring no material components:\n\
      \n**1/day each:** [[confusion-xphb|confusion]], [[crown-of-madness-xphb|crown of\
      \ madness]], [[suggestion-xphb|suggestion]]"
    "name": "Innate Spellcasting"
  - "desc": "The abhorrent overlord can sense the presence of gold within 1,000 feet\
      \ of itself. It can determine which location has the greatest amount of gold\
      \ and can sense the direction to that site. If the gold is being moved, it knows\
      \ the direction of the movement. It can't locate gold if any thickness of clay\
      \ or lead, even a thin sheet, blocks a direct path between it and the gold."
    "name": "Insatiable Greed"
  - "desc": "The abhorrent overlord has advantage on saving throws against spells\
      \ and other magical effects."
    "name": "Magic Resistance"
"actions":
  - "desc": "The abhorrent overlord makes two attacks with its claws."
    "name": "Multiattack"
  - "desc": "*Melee Weapon Attack:* +9 to hit, reach 5 ft., one target. *Hit:* 14\
      \ (2d8 + 5) slashing damage plus 14 (4d6) necrotic damage. The abhorrent\
      \ overlord regains hit points equal to half the amount of necrotic damage dealt\
      \ if the target is a creature."
    "name": "Claws"
  - "desc": "The abhorrent overlord conjures a swarm of spectral crows and harpies\
      \ in a 20-foot-radius sphere centered on a point the overlord can see within\
      \ 120 feet of it. The sphere remains for 1 minute or until the overlord loses\
      \ [[conditions#Concentration|concentration]] (as if [[conditions#Concentration|concentrating]]\
      \ on a spell), and its area is lightly obscured and difficult terrain.\n\nAny\
      \ creature that moves into the area for the first time on a turn or starts its\
      \ turn there must make a DC 15 Constitution saving throw. A creature takes 16\
      \ (3d10) slashing damage plus 16 (3d10) psychic damage on a failed save,\
      \ or half as much damage on a successful one."
    "name": "Storm of Crows (Recharge 6)"
"source":
  - "MOT"
"image": "Compendium/bestiary/fiend/token/abhorrent-overlord-mot.webp"
```
^statblock