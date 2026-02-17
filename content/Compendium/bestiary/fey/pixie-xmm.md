---
title: Pixie
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- src/5e/xmm
- monster/cr/1-4
- monster/environment/feywild
- monster/environment/forest
- monster/environment/planar
- monster/size/tiny
- monster/type/fey
statblock: inline
aliases: ["Pixie"]
---
# Pixie
*Source: Monster Manual (2024) p. 244, FRHoF*  

![](Compendium/books/monster-manual-2025/img/pixies.webp#right)  
Pixies spend their days frolicking and exploring and avoid direct conflict when they can.

## Pixies

*Friends of the Forest*

- **Habitat.** Forest, Planar (Feywild)  
- **Treasure.** [[random-magic-items-arcana|Arcana]]  

Barely a foot tall, pixies resemble diminutive elves with gossamer wings. They invisibly observe those who enter their wooded homes, revealing themselves to those with friendly intentions. Those who are unfriendly become the targets of pixies' pranks.
## Statblock

```statblock
"name": "Pixie (XMM)"
"size": "Tiny"
"type": "fey"
"alignment": "Neutral Good"
"ac": !!int "15"
"hp": !!int "9"
"hit_dice": "6d4 - 6"
"modifier": !!int "5"
"stats":
  - !!int "2"
  - !!int "20"
  - !!int "8"
  - !!int "10"
  - !!int "14"
  - !!int "15"
"speed": "10 ft., fly 30 ft."
"skillsaves":
  - "name": "[[skills#Perception|Perception]]"
    "desc": "+4"
  - "name": "[[skills#Stealth|Stealth]]"
    "desc": "+7"
"senses": "passive Perception 14"
"languages": "Sylvan"
"cr": "1/4"
"traits":
  - "desc": "The pixie has [[advantage-xphb|Advantage]]\
      \ on saving throws against spells and other magical effects."
    "name": "Magic Resistance"
"actions":
  - "desc": "*Melee  or Ranged Attack Roll:* +4, reach 5 ft. or range 60 ft. *Hit:*\
      \ 1 Radiant damage, and the target has the [[conditions#Charmed|Charmed]]\
      \ or [[conditions#Poisoned|Poisoned]] condition (pixie's\
      \ choice) until the start of the pixie's next turn."
    "name": "Faerie Dust"
  - "desc": "The pixie casts one of the following spells, requiring no Material components\
      \ and using Charisma as the spellcasting ability (spell save DC 12):\n\n**At\
      \ will:** [[dancing-lights-xphb|Dancing Lights]], [[druidcraft-xphb|Druidcraft]],\
      \ [[invisibility-xphb|Invisibility]] (self only)\n\n**1/day\
      \ each:** [[detect-thoughts-xphb|Detect Thoughts]], [[fly-xphb|Fly]],\
      \ [[sleep-xphb|Sleep]]"
    "name": "Spellcasting"
"source":
  - "XMM"
  - "FRHoF"
"image": "Compendium/bestiary/fey/token/pixie-xmm.webp"
```
^statblock