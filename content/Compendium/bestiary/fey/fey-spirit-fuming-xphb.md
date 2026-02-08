---
title: Fey Spirit (Fuming)
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- ttrpg-cli/compendium/src/5e/xphb
- ttrpg-cli/monster/cr/
- ttrpg-cli/monster/size/small
- ttrpg-cli/monster/type/fey
statblock: inline
aliases: ["Fey Spirit (Fuming)"]
---
# Fey Spirit (Fuming)
*Source: Player's Handbook (2024) p. 326*  

```statblock
"name": "Fey Spirit (Fuming) (XPHB)"
"size": "Small"
"type": "fey"
"alignment": "Neutral"
"ac_class": "12 + the spell's level"
"modifier": !!int "3"
"stats":
  - !!int "13"
  - !!int "16"
  - !!int "14"
  - !!int "14"
  - !!int "11"
  - !!int "16"
"speed": "30 ft., fly 30 ft."
"condition_immunities": "[charmed](Compendium/rules/conditions.md#Charmed)"
"senses": "[Darkvision](Compendium/rules/senses.md#Darkvision) 60 ft., passive Perception\
  \ 10"
"languages": "Sylvan, understands the languages you know"
"actions":
  - "desc": "The spirit makes a number of Fey Blade attacks equal to half this spell's\
      \ level (round down)."
    "name": "Multiattack"
  - "desc": "*Melee Attack Roll:* Bonus equals your spell attack modifier, reach 5\
      \ ft. *Hit:* 2d6 + 3 + the spell's level Force damage."
    "name": "Fey Blade"
"bonus_actions":
  - "desc": "The spirit magically teleports up to 30 feet to an unoccupied space it\
      \ can see. The spirit has Advantage on the next attack roll it makes before\
      \ the end of this turn."
    "name": "Fey Step"
"source":
  - "XPHB"
```
^statblock