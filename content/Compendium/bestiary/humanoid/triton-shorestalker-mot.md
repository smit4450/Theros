---
title: Triton Shorestalker
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- src/5e/mot
- monster/cr/2
- monster/size/medium
- monster/type/humanoid/triton
statblock: inline
aliases: ["Triton Shorestalker"]
---
# Triton Shorestalker
*Source: Mythic Odysseys of Theros p. 244*  

![](Compendium/bestiary/humanoid/img/triton-shorestalker.webp#right|850)  
Some insults don't wash away with the tides. When surface dwellers threaten the safety of triton communities, impede upon Thassa's holiest depths, or steal the treasures of the deep, triton shorestalkers seek vengeance. Using speed and poison harvested from deadly sea beasts, these triton assassins slip into shallow waters and strike when least expected. Often, surface dwellers don't even realize they've been attacked by shorestalkers, chalking disappearances and deaths up to the innumerable dangers of the sea.

Clever, far-ranging people of the sea, tritons live rich lives unknown to most land-dwelling individuals. While the waves separate most tritons from land-dwellers, occasionally the inhabitants of the surface and the deep come into conflict. In such cases, tritons prove skilled at sabotaging ocean-going vessels, employing water-based magic, and otherwise whipping up the fury of the sea. Few dare insult tritons in their home environment, but those who do and survive often learn that the tritons' wrath doesn't end at the shore.
```statblock
"name": "Triton Shorestalker (MOT)"
"size": "Medium"
"type": "humanoid"
"subtype": "triton"
"alignment": "Neutral Evil"
"ac": !!int "13"
"hp": !!int "32"
"hit_dice": "5d8 + 10"
"modifier": !!int "3"
"stats":
  - !!int "11"
  - !!int "16"
  - !!int "14"
  - !!int "10"
  - !!int "15"
  - !!int "11"
"speed": "30 ft., swim 30 ft."
"skillsaves":
  - "name": "[[skills#Nature|Nature]]"
    "desc": "+4"
  - "name": "[[skills#Perception|Perception]]"
    "desc": "+4"
  - "name": "[[skills#Stealth|Stealth]]"
    "desc": "+5"
"damage_resistances": "cold"
"senses": "[[senses#Darkvision|darkvision]] 60 ft., passive Perception\
  \ 14"
"languages": "Common, Primordial"
"cr": "2"
"traits":
  - "desc": "The triton's spellcasting ability is Wisdom (spell save DC 12). It can\
      \ innately cast the following spells, requiring no material components:\n\n\
      **1/day each:** [[fog-cloud-xphb|fog cloud]], [[gust-of-wind-xphb|gust of wind]]"
    "name": "Innate Spellcasting"
  - "desc": "The triton can breathe air and water."
    "name": "Amphibious"
  - "desc": "The triton can take the Disengage or Hide actions as a bonus action on\
      \ each of its turns."
    "name": "Nimble Escape"
"actions":
  - "desc": "The triton makes two urchin-spine shortsword attacks."
    "name": "Multiattack"
  - "desc": "*Melee Weapon Attack:* +5 to hit, reach 5 ft., one target. *Hit:* 6\
      \ (1d6 + 3) piercing damage plus 10 (3d6) poison damage. If the damage reduces\
      \ a creature to 0 hit points, that creature is stable but [[conditions#Poisoned|poisoned]]\
      \ for 1 hour, even after regaining hit points, and is [[conditions#Paralyzed|paralyzed]]\
      \ while [[conditions#Poisoned|poisoned]] in this way."
    "name": "Urchin-Spine Shortsword"
  - "desc": "*Ranged Weapon Attack:* +5 to hit, range 30/60 ft., one target. *Hit:*\
      \ 5 (1d4 + 3) piercing damage plus 10 (3d6) poison damage."
    "name": "Poisoned Spine"
"source":
  - "MOT"
"image": "Compendium/bestiary/humanoid/token/triton-shorestalker-mot.webp"
```
^statblock