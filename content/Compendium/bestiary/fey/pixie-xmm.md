---
obsidianUIMode: preview
cssclasses:
- json5e-monster
tags:
- compendium/src/5e/xmm
- monster/cr/1-4
- monster/environment/feywild
- monster/environment/forest
- monster/environment/planar
- monster/size/tiny
- monster/type/fey
statblock: inline
statblock-link: "#^statblock"
aliases:
- "Pixie"
---
# Pixie
*Source: Monster Manual (2024) p. 244*
![](/Compendium/books/monster-manual-2025/img/pixies.webp#right)

Pixies spend their days frolicking and exploring and avoid direct conflict when they can.

## Pixies

*Friends of the Forest*

- **Habitat.** Forest, Planar (Feywild)  
- **Treasure.** [Arcana](/Compendium/tables/random-magic-items-arcana.md)  

Barely a foot tall, pixies resemble diminutive elves with gossamer wings. They invisibly observe those who enter their wooded homes, revealing themselves to those with friendly intentions. Those who are unfriendly become the targets of pixies' pranks.

## Statblock

```statblock
"name": "Pixie"
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
  - "name": "[Perception](/Compendium/rules/skills.md#Perception)"
    "desc": "+4"
  - "name": "[Stealth](/Compendium/rules/skills.md#Stealth)"
    "desc": "+7"
"senses": "passive Perception 14"
"languages": "Sylvan"
"cr": "1/4"
"traits":
  - "desc": "The pixie has [Advantage](/Compendium/rules/variant-rules/advantage-xphb.md)\
      \ on saving throws against spells and other magical effects."
    "name": "Magic Resistance"
"actions":
  - "desc": "*Melee  or Ranged Attack Roll:* +4, reach 5 ft. or range 60 ft. *Hit:*\
      \ 1 Radiant damage, and the target has the [Charmed](/Compendium/rules/conditions.md#Charmed)\
      \ or [Poisoned](/Compendium/rules/conditions.md#Poisoned) condition (pixie's\
      \ choice) until the start of the pixie's next turn."
    "name": "Faerie Dust"
  - "desc": "The pixie casts one of the following spells, requiring no Material components\
      \ and using Charisma as the spellcasting ability (spell save DC 12):\n\n**At\
      \ will:** [Dancing Lights](/Compendium/spells/dancing-lights-xphb.md), [Druidcraft](/Compendium/spells/druidcraft-xphb.md),\
      \ [Invisibility](/Compendium/spells/invisibility-xphb.md) (self only)\n\n**1/day\
      \ each:** [Detect Thoughts](/Compendium/spells/detect-thoughts-xphb.md), [Fly](/Compendium/spells/fly-xphb.md),\
      \ [Sleep](/Compendium/spells/sleep-xphb.md)"
    "name": "Spellcasting"
"source":
  - "XMM"
"image": "/Compendium/bestiary/fey/token/pixie-xmm.webp"
```
^statblock

## Environment

forest, planar, feywild