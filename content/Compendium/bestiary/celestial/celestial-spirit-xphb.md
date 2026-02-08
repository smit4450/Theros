---
title: Celestial Spirit
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- ttrpg-cli/compendium/src/5e/xphb
- ttrpg-cli/monster/cr/
- ttrpg-cli/monster/size/large
- ttrpg-cli/monster/type/celestial
statblock: inline
aliases: ["Celestial Spirit"]
---
# Celestial Spirit
*Source: Player's Handbook (2024) p. 323*  

![](Compendium/bestiary/celestial/img/celestial-spirit.webp#center)  
```statblock
"name": "Celestial Spirit (XPHB)"
"size": "Large"
"type": "celestial"
"alignment": "Neutral"
"ac_class": "11 + the spell's level + 2 (Defender only)"
"modifier": !!int "2"
"stats":
  - !!int "16"
  - !!int "14"
  - !!int "16"
  - !!int "10"
  - !!int "14"
  - !!int "16"
"speed": "30 ft., fly 40 ft."
"damage_resistances": "radiant"
"condition_immunities": "[charmed](Compendium/rules/conditions.md#Charmed), [frightened](Compendium/rules/conditions.md#Frightened)"
"senses": "[Darkvision](Compendium/rules/senses.md#Darkvision) 60 ft., passive Perception\
  \ 12"
"languages": "Celestial, understands the languages you know"
"actions":
  - "desc": "The spirit makes a number of attacks equal to half this spell's level\
      \ (round down)."
    "name": "Multiattack"
  - "desc": "*Ranged Attack Roll:* Bonus equals your spell attack modifier, range\
      \ 600 ft. *Hit:* 2d6 + 2 + the spell's level Radiant damage."
    "name": "Radiant Bow (Avenger Only)"
  - "desc": "*Melee Attack Roll:* Bonus equals your spell attack modifier, reach 5\
      \ ft. *Hit:* 1d10 + 3 + the spell's level Radiant damage, and the spirit can\
      \ choose itself or another creature it can see within 10 feet of the target.\
      \ The chosen creature gains 1d10 Temporary Hit Points."
    "name": "Radiant Mace (Defender Only)"
  - "desc": "The spirit touches another creature. The target regains Hit Points equal\
      \ to 2d8 + the spell's level."
    "name": "Healing Touch (1/Day)"
"source":
  - "XPHB"
"image": "Compendium/bestiary/celestial/token/celestial-spirit-xphb.webp"
```
^statblock