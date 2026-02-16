---
title: Bestial Spirit (Air)
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- ttrpg-cli/compendium/src/5e/xphb
- ttrpg-cli/monster/cr/
- ttrpg-cli/monster/size/small
- ttrpg-cli/monster/type/beast
statblock: inline
aliases: ["Bestial Spirit (Air)"]
---
# Bestial Spirit (Air)
*Source: Player's Handbook (2024) p. 323*  

```statblock
"name": "Bestial Spirit (Air) (XPHB)"
"size": "Small"
"type": "beast"
"alignment": "Neutral"
"ac_class": "11 + the spell's level"
"modifier": !!int "0"
"stats":
  - !!int "18"
  - !!int "11"
  - !!int "16"
  - !!int "4"
  - !!int "14"
  - !!int "5"
"speed": "30 ft., fly 60 ft."
"senses": "[[senses#Darkvision|Darkvision]] 60 ft., passive Perception\
  \ 12"
"languages": "understands the languages you know"
"traits":
  - "desc": "The spirit doesn't provoke [[actions#Opportunity%20Attack|Opportunity Attacks]]\
      \ when it flies out of an enemy's reach."
    "name": "Flyby"
"actions":
  - "desc": "The spirit makes a number of Rend attacks equal to half this spell's\
      \ level (round down)."
    "name": "Multiattack"
  - "desc": "*Melee Attack Roll:* Bonus equals your spell attack modifier, reach 5\
      \ ft. *Hit:* 1d8 + 4 + the spell's level Piercing damage."
    "name": "Rend"
"source":
  - "XPHB"
```
^statblock