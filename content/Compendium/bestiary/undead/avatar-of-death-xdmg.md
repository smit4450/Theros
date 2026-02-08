---
title: Avatar of Death
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- ttrpg-cli/compendium/src/5e/xdmg
- ttrpg-cli/monster/cr/
- ttrpg-cli/monster/size/medium
- ttrpg-cli/monster/type/undead
statblock: inline
aliases: ["Avatar of Death"]
---
# Avatar of Death
*Source: Dungeon Master's Guide (2024) p. 252*  

```statblock
"name": "Avatar of Death (XDMG)"
"size": "Medium"
"type": "undead"
"alignment": "Neutral Evil"
"ac": !!int "20"
"modifier": !!int "3"
"stats":
  - !!int "16"
  - !!int "16"
  - !!int "16"
  - !!int "16"
  - !!int "16"
  - !!int "16"
"speed": "60 ft., fly 60 ft. (hover)"
"damage_immunities": "necrotic, poison"
"condition_immunities": "[charmed](Compendium/rules/conditions.md#Charmed), [exhaustion](Compendium/rules/conditions.md#Exhaustion),\
  \ [frightened](Compendium/rules/conditions.md#Frightened), [paralyzed](Compendium/rules/conditions.md#Paralyzed),\
  \ [petrified](Compendium/rules/conditions.md#Petrified), [poisoned](Compendium/rules/conditions.md#Poisoned),\
  \ [unconscious](Compendium/rules/conditions.md#Unconscious)"
"senses": "[Truesight](Compendium/rules/senses.md#Truesight) 60 ft., passive Perception\
  \ 13"
"languages": "all languages known to its summoner"
"traits":
  - "desc": "The avatar can move through other creatures and objects as if they were\
      \ Difficult Terrain. It takes 5 (1d10) Force damage if it ends its turn inside\
      \ an object."
    "name": "Incorporeal Movement"
"actions":
  - "desc": "The avatar makes a number of Reaping Scythe attacks equal to half the\
      \ summoner's Proficiency Bonus (rounded up)."
    "name": "Multiattack"
  - "desc": "*Melee Attack Roll:* Automatic hit, reach 5 ft. *Hit:* 7 (1d8 + 3)\
      \ Slashing damage plus 4 (1d8) Necrotic damage."
    "name": "Reaping Scythe"
"source":
  - "XDMG"
"image": "Compendium/bestiary/undead/token/avatar-of-death-xdmg.webp"
```
^statblock