---
title: Undead Spirit (Skeletal)
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- ttrpg-cli/compendium/src/5e/xphb
- ttrpg-cli/monster/cr/
- ttrpg-cli/monster/size/medium
- ttrpg-cli/monster/type/undead
statblock: inline
aliases: ["Undead Spirit (Skeletal)"]
---
# Undead Spirit (Skeletal)
*Source: Player's Handbook (2024) p. 328*  

```statblock
"name": "Undead Spirit (Skeletal) (XPHB)"
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
"speed": "30 ft."
"damage_immunities": "necrotic, poison"
"condition_immunities": "[[conditions#Exhaustion|exhaustion]],\
  \ [[conditions#Frightened|frightened]], [[conditions#Paralyzed|paralyzed]],\
  \ [[conditions#Poisoned|poisoned]]"
"senses": "[[senses#Darkvision|Darkvision]] 60 ft., passive Perception\
  \ 10"
"languages": "understands the languages you know"
"actions":
  - "desc": "The spirit makes a number of attacks equal to half this spell's level\
      \ (round down)."
    "name": "Multiattack"
  - "desc": "*Ranged Attack Roll:* Bonus equals your spell attack modifier, range\
      \ 150 ft. *Hit:* 2d4 + 3 + the spell's level Necrotic damage."
    "name": "Grave Bolt"
"source":
  - "XPHB"
```
^statblock