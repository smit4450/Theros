---
title: Archer
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- ttrpg-cli/compendium/src/5e/vgm
- ttrpg-cli/monster/cr/3
- ttrpg-cli/monster/environment/forest
- ttrpg-cli/monster/environment/urban
- ttrpg-cli/monster/size/medium
- ttrpg-cli/monster/type/humanoid/any-race
statblock: inline
aliases: ["Archer"]
---
# Archer
*Source: Volo's Guide to Monsters p. 210, Mythic Odysseys of Theros*  

![](Compendium/bestiary/humanoid/img/archer.webp#right)  
Archers defend castles, hunt wild game on the fringes of civilization, serve as artillery in military units, and occasionally make good coin as brigands or caravan guards.
```statblock
"name": "Archer (VGM)"
"size": "Medium"
"type": "humanoid"
"subtype": "any race"
"alignment": "Any alignment"
"ac": !!int "16"
"ac_class": "[studded leather](Compendium/items/studded-leather-armor-xphb.md)"
"hp": !!int "75"
"hit_dice": "10d8 + 30"
"modifier": !!int "4"
"stats":
  - !!int "11"
  - !!int "18"
  - !!int "16"
  - !!int "11"
  - !!int "13"
  - !!int "10"
"speed": "30 ft."
"skillsaves":
  - "name": "[Acrobatics](Compendium/rules/skills.md#Acrobatics)"
    "desc": "+6"
  - "name": "[Perception](Compendium/rules/skills.md#Perception)"
    "desc": "+5"
"senses": "passive Perception 15"
"languages": "any one language (usually Common)"
"cr": "3"
"traits":
  - "desc": "As a bonus action, the archer can add 1d10 to its next attack or damage\
      \ roll with a longbow or shortbow."
    "name": "Archer's Eye (3/Day)"
"actions":
  - "desc": "The archer makes two attacks with its longbow."
    "name": "Multiattack"
  - "desc": "*Melee Weapon Attack:* +6 to hit, reach 5 ft., one target. *Hit:* 7\
      \ (1d6 + 4) piercing damage."
    "name": "Shortsword"
  - "desc": "*Ranged Weapon Attack:* +6 to hit, range 150/600 ft., one target. *Hit:*\
      \ 8 (1d8 + 4) piercing damage."
    "name": "Longbow"
"source":
  - "VGM"
  - "MOT"
"image": "Compendium/bestiary/humanoid/token/archer-vgm.webp"
```
^statblock