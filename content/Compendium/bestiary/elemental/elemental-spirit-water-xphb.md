---
title: Elemental Spirit (Water)
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- src/5e/xphb
- monster/cr/
- monster/size/medium
- monster/type/elemental
statblock: inline
aliases: ["Elemental Spirit (Water)"]
---
# Elemental Spirit (Water)
*Source: Player's Handbook (2024) p. 325*  

```statblock
"name": "Elemental Spirit (Water) (XPHB)"
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
"speed": "40 ft., swim 40 ft."
"damage_resistances": "acid"
"damage_immunities": "poison"
"condition_immunities": "[[conditions#Exhaustion|exhaustion]],\
  \ [[conditions#Paralyzed|paralyzed]], [[conditions#Petrified|petrified]],\
  \ [[conditions#Poisoned|poisoned]]"
"senses": "[[senses#Darkvision|Darkvision]] 60 ft., passive Perception\
  \ 10"
"languages": "Primordial, understands the languages you know"
"traits":
  - "desc": "The spirit can move through a space as narrow as 1 inch wide without\
      \ it counting as Difficult Terrain."
    "name": "Amorphous Form"
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