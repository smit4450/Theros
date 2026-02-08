---
title: Elemental Spirit (Earth)
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- ttrpg-cli/compendium/src/5e/xphb
- ttrpg-cli/monster/cr/
- ttrpg-cli/monster/size/medium
- ttrpg-cli/monster/type/elemental
statblock: inline
aliases: ["Elemental Spirit (Earth)"]
---
# Elemental Spirit (Earth)
*Source: Player's Handbook (2024) p. 325*  

```statblock
"name": "Elemental Spirit (Earth) (XPHB)"
"size": "Medium"
"type": "elemental"
"alignment": "Neutral"
"ac_class": "11 + the spell's level"
"modifier": !!int "2"
"stats":
  - !!int "18"
  - !!int "15"
  - !!int "17"
  - !!int "4"
  - !!int "10"
  - !!int "16"
"speed": "40 ft., burrow 40 ft."
"damage_resistances": "piercing, slashing"
"damage_immunities": "poison"
"condition_immunities": "[exhaustion](Compendium/rules/conditions.md#Exhaustion),\
  \ [paralyzed](Compendium/rules/conditions.md#Paralyzed), [petrified](Compendium/rules/conditions.md#Petrified),\
  \ [poisoned](Compendium/rules/conditions.md#Poisoned)"
"senses": "[Darkvision](Compendium/rules/senses.md#Darkvision) 60 ft., passive Perception\
  \ 10"
"languages": "Primordial, understands the languages you know"
"actions":
  - "desc": "The spirit makes a number of Slam attacks equal to half this spell's\
      \ level (round down)."
    "name": "Multiattack"
  - "desc": "*Melee Attack Roll:* Bonus equals your spell attack modifier, reach 5\
      \ ft.. *Hit:* 1d10 + 4 + the spell's level Bludgeoning damage."
    "name": "Slam"
"source":
  - "XPHB"
```
^statblock