---
obsidianUIMode: preview
cssclasses:
- json5e-monster
tags:
- compendium/src/5e/xmm
- monster/cr/1-2
- monster/environment/underwater
- monster/size/medium
- monster/type/beast
statblock: inline
statblock-link: "#^statblock"
aliases:
- "Reef Shark"
---
# Reef Shark
*Source: Monster Manual (2024) p. 368, Player's Handbook (2024) p. 356. Available in the <span title='Systems Reference Document (5.2)'>SRD</span> and the Free Rules (2024)*
![](/Compendium/bestiary/beast/img/reef-shark.webp#right)

## Animals

Use these stat blocks to represent the creatures they're named for or other similar creatures. For example, the [Panther](/Compendium/bestiary/beast/panther-xmm.md) stat block can also represent a mountain lion, while the [Giant Goat](/Compendium/bestiary/beast/giant-goat-xmm.md) stat block might represent a buffalo. Any of these stat blocks might also serve as fantastical animals with distinctive names and cosmetic details unique to your D&D adventures.

> [!gallery]
![A druid calls on animals of the hills and mountains to aid her cause](/Compendium/bestiary/beast/img/animals-hills-and-mountains.webp)
![Aquatic animals swim alongside a druid exploring the sea](/Compendium/bestiary/beast/img/animals-aquatic.webp)
![Inhabitants of the rain forest answer a druid's summons](/Compendium/bestiary/beast/img/animals-rainforest.webp)

```statblock
"name": "Reef Shark"
"size": "Medium"
"type": "beast"
"alignment": "Unaligned"
"ac": !!int "12"
"hp": !!int "22"
"hit_dice": "4d8 + 4"
"modifier": !!int "2"
"stats":
  - !!int "14"
  - !!int "15"
  - !!int "13"
  - !!int "1"
  - !!int "10"
  - !!int "4"
"speed": "5 ft., swim 30 ft."
"skillsaves":
  - "name": "[Perception](/Compendium/rules/skills.md#Perception)"
    "desc": "+2"
"senses": "[Blindsight](/Compendium/rules/senses.md#Blindsight) 30 ft., passive Perception\
  \ 12"
"languages": ""
"cr": "1/2"
"traits":
  - "desc": "The shark has [Advantage](/Compendium/rules/variant-rules/advantage-xphb.md)\
      \ on an attack roll against a creature if at least one of the shark's allies\
      \ is within 5 feet of the creature and the ally doesn't have the [Incapacitated](/Compendium/rules/conditions.md#Incapacitated)\
      \ condition."
    "name": "Pack Tactics"
  - "desc": "The shark can breathe only underwater."
    "name": "Water Breathing"
"actions":
  - "desc": "*Melee Attack Roll:* +4, reach 5 ft. *Hit:* 7 (2d4 + 2) Piercing damage."
    "name": "Bite"
"source":
  - "XMM"
  - "XPHB"
"image": "/Compendium/bestiary/beast/token/reef-shark-xmm.webp"
```
^statblock

## Environment

underwater