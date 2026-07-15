---
obsidianUIMode: preview
cssclasses:
- json5e-monster
tags:
- compendium/src/5e/xmm
- monster/cr/1-4
- monster/environment/forest
- monster/environment/grassland
- monster/environment/hill
- monster/size/medium
- monster/type/beast
statblock: inline
statblock-link: "#^statblock"
aliases:
- "Panther"
---
# Panther
*Source: Monster Manual (2024) p. 366, Player's Handbook (2024) p. 354. Available in the <span title='Systems Reference Document (5.2)'>SRD</span> and the Free Rules (2024)*
![A druid calls on animals of the hills and mountains to aid her cause](/Compendium/bestiary/beast/img/animals-hills-and-mountains.webp#right)

## Animals

Use these stat blocks to represent the creatures they're named for or other similar creatures. For example, the [Panther](/Compendium/bestiary/beast/panther-xmm.md) stat block can also represent a mountain lion, while the [Giant Goat](/Compendium/bestiary/beast/giant-goat-xmm.md) stat block might represent a buffalo. Any of these stat blocks might also serve as fantastical animals with distinctive names and cosmetic details unique to your D&D adventures.

> [!gallery]
![Aquatic animals swim alongside a druid exploring the sea](/Compendium/bestiary/beast/img/animals-aquatic.webp)
![Inhabitants of the rain forest answer a druid's summons](/Compendium/bestiary/beast/img/animals-rainforest.webp)

```statblock
"name": "Panther"
"size": "Medium"
"type": "beast"
"alignment": "Unaligned"
"ac": !!int "13"
"hp": !!int "13"
"hit_dice": "3d8"
"modifier": !!int "3"
"stats":
  - !!int "14"
  - !!int "16"
  - !!int "10"
  - !!int "3"
  - !!int "14"
  - !!int "7"
"speed": "50 ft., climb 40 ft."
"skillsaves":
  - "name": "[Perception](/Compendium/rules/skills.md#Perception)"
    "desc": "+4"
  - "name": "[Stealth](/Compendium/rules/skills.md#Stealth)"
    "desc": "+6"
"senses": "[Darkvision](/Compendium/rules/senses.md#Darkvision) 60 ft., passive Perception\
  \ 14"
"languages": ""
"cr": "1/4"
"actions":
  - "desc": "*Melee Attack Roll:* +5, reach 5 ft. *Hit:* 6 (1d6 + 3) Slashing damage."
    "name": "Rend"
"bonus_actions":
  - "desc": "The panther takes the [Disengage](/Compendium/rules/actions.md#Disengage)\
      \ or [Hide](/Compendium/rules/actions.md#Hide) action."
    "name": "Nimble Escape"
"source":
  - "XMM"
  - "XPHB"
"image": "/Compendium/bestiary/beast/token/panther-xmm.webp"
```
^statblock

## Environment

forest, grassland, hill