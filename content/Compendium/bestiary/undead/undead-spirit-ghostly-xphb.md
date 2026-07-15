---
obsidianUIMode: preview
cssclasses:
- json5e-monster
tags:
- compendium/src/5e/xphb
- monster/cr/
- monster/size/medium
- monster/type/undead
statblock: inline
statblock-link: "#^statblock"
aliases:
- "Undead Spirit (Ghostly)"
---
# Undead Spirit (Ghostly)
*Source: Player's Handbook (2024) p. 328*

```statblock
"name": "Undead Spirit (Ghostly)"
"size": "Medium"
"type": "undead"
"alignment": "Neutral"
"ac_class": "11 + the spell's level"
"modifier": !!int "3"
"stats":
  - !!int "12"
  - !!int "16"
  - !!int "15"
  - !!int "4"
  - !!int "10"
  - !!int "9"
"speed": "30 ft., fly 40 ft. (hover)"
"damage_immunities": "necrotic, poison"
"condition_immunities": "[exhaustion](/Compendium/rules/conditions.md#Exhaustion),\
  \ [frightened](/Compendium/rules/conditions.md#Frightened), [paralyzed](/Compendium/rules/conditions.md#Paralyzed),\
  \ [poisoned](/Compendium/rules/conditions.md#Poisoned)"
"senses": "[Darkvision](/Compendium/rules/senses.md#Darkvision) 60 ft., passive Perception\
  \ 10"
"languages": "understands the languages you know"
"traits":
  - "desc": "The spirit can move through other creatures and objects as if they were\
      \ Difficult Terrain. If it ends its turn inside an object, it is shunted to\
      \ the nearest unoccupied space and takes 1d10 Force damage for every 5 feet\
      \ traveled."
    "name": "Incorporeal Passage"
"actions":
  - "desc": "The spirit makes a number of attacks equal to half this spell's level\
      \ (round down)."
    "name": "Multiattack"
  - "desc": "*Melee Attack Roll:* Bonus equals your spell attack modifier, reach 5\
      \ ft. *Hit:* 1d8 + 3 + the spell's level Necrotic damage, and the target has\
      \ the [Frightened](/Compendium/rules/conditions.md#Frightened) condition until\
      \ the end of its next turn."
    "name": "Deathly Touch"
"source":
  - "XPHB"
```
^statblock