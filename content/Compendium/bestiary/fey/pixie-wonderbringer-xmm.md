---
title: Pixie Wonderbringer
obsidianUIMode: preview
cssclasses: json5e-object
tags:
- ttrpg-cli/compendium/src/5e/xmm
- ttrpg-cli/monster/cr/5
- ttrpg-cli/monster/environment/feywild
- ttrpg-cli/monster/environment/forest
- ttrpg-cli/monster/environment/planar
- ttrpg-cli/monster/size/tiny
- ttrpg-cli/monster/type/fey
statblock: inline
aliases: ["Pixie Wonderbringer"]
---
# Pixie Wonderbringer
*Source: Monster Manual (2024) p. 244*  

![](Compendium/books/monster-manual-2025/img/pixies.webp#right)  
Energetic entertainers, wonderbringers use their magic in defense of the wilderness when they must.

## Pixies

*Friends of the Forest*

- **Habitat.** Forest, Planar (Feywild)  
- **Treasure.** [[random-magic-items-arcana|Arcana]]  

Barely a foot tall, pixies resemble diminutive elves with gossamer wings. They invisibly observe those who enter their wooded homes, revealing themselves to those with friendly intentions. Those who are unfriendly become the targets of pixies' pranks.
## Statblock

```statblock
"name": "Pixie Wonderbringer (XMM)"
"size": "Tiny"
"type": "fey"
"alignment": "Neutral Good"
"ac": !!int "15"
"hp": !!int "60"
"hit_dice": "24d4"
"modifier": !!int "5"
"stats":
  - !!int "2"
  - !!int "20"
  - !!int "10"
  - !!int "11"
  - !!int "14"
  - !!int "18"
"speed": "10 ft., fly 30 ft."
"skillsaves":
  - "name": "[[skills#Arcana|Arcana]]"
    "desc": "+3"
  - "name": "[[skills#Perception|Perception]]"
    "desc": "+5"
  - "name": "[[skills#Stealth|Stealth]]"
    "desc": "+8"
"senses": "passive Perception 15"
"languages": "Common, Elvish, Sylvan"
"cr": "5"
"traits":
  - "desc": "The pixie has [[advantage-xphb|Advantage]]\
      \ on saving throws against spells and other magical effects."
    "name": "Magic Resistance"
"actions":
  - "desc": "The pixie makes two Faerie Dust attacks."
    "name": "Multiattack"
  - "desc": "*Melee  or Ranged Attack Roll:* +7, reach 5 ft. or range 60 ft. *Hit:*\
      \ 15 (2d10 + 4) Radiant damage, and the target has the [[conditions#Charmed|Charmed]]\
      \ or [[conditions#Poisoned|Poisoned]] condition (pixie's\
      \ choice) until the start of the pixie's next turn."
    "name": "Faerie Dust"
  - "desc": "The pixie casts one of the following spells, requiring no Material components\
      \ and using Charisma as the spellcasting ability (spell save DC 15):\n\n**At\
      \ will:** [[dancing-lights-xphb|Dancing Lights]], [[druidcraft-xphb|Druidcraft]],\
      \ [[invisibility-xphb|Invisibility]] (self only)\n\n**1/day\
      \ each:** [[detect-thoughts-xphb|Detect Thoughts]], [[fly-xphb|Fly]],\
      \ [[major-image-xphb|Major Image]]"
    "name": "Spellcasting"
"bonus_actions":
  - "desc": "The pixie casts [[entangle-xphb|Entangle]], [[polymorph-xphb|Polymorph]],\
      \ or [[tashas-hideous-laughter-xphb|Tasha's Hideous Laughter]],\
      \ requiring no Material components and using the same spellcasting ability as\
      \ Spellcasting.\n"
    "name": "Burst of Wonder (Recharge 5-6)"
"source":
  - "XMM"
"image": "Compendium/bestiary/fey/token/pixie-wonderbringer-xmm.webp"
```
^statblock