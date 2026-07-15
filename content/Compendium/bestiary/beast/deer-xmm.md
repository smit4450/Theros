---
obsidianUIMode: preview
cssclasses:
- json5e-monster
tags:
- compendium/src/5e/xmm
- monster/cr/0
- monster/environment/forest
- monster/environment/grassland
- monster/size/medium
- monster/type/beast
statblock: inline
statblock-link: "#^statblock"
aliases:
- "Deer"
---
# Deer
*Source: Monster Manual (2024) p. 352. Available in the <span title='Systems Reference Document (5.2)'>SRD</span> and the Free Rules (2024)*
![](/Compendium/bestiary/beast/img/deer.webp#right)

## Animals

Use these stat blocks to represent the creatures they're named for or other similar creatures. For example, the [Panther](/Compendium/bestiary/beast/panther-xmm.md) stat block can also represent a mountain lion, while the [Giant Goat](/Compendium/bestiary/beast/giant-goat-xmm.md) stat block might represent a buffalo. Any of these stat blocks might also serve as fantastical animals with distinctive names and cosmetic details unique to your D&D adventures.

> [!gallery]
![A druid calls on animals of the hills and mountains to aid her cause](/Compendium/bestiary/beast/img/animals-hills-and-mountains.webp)
![Aquatic animals swim alongside a druid exploring the sea](/Compendium/bestiary/beast/img/animals-aquatic.webp)
![Inhabitants of the rain forest answer a druid's summons](/Compendium/bestiary/beast/img/animals-rainforest.webp)

```statblock
"name": "Deer"
"size": "Medium"
"type": "beast"
"alignment": "Unaligned"
"ac": !!int "13"
"hp": !!int "4"
"hit_dice": "1d8"
"modifier": !!int "3"
"stats":
  - !!int "11"
  - !!int "16"
  - !!int "11"
  - !!int "2"
  - !!int "14"
  - !!int "5"
"speed": "50 ft."
"skillsaves":
  - "name": "[Perception](/Compendium/rules/skills.md#Perception)"
    "desc": "+4"
"senses": "[Darkvision](/Compendium/rules/senses.md#Darkvision) 60 ft., passive Perception\
  \ 14"
"languages": ""
"cr": "0"
"traits":
  - "desc": "The deer doesn't provoke an Opportunity Attack when it moves out of an\
      \ enemy's reach."
    "name": "Agile"
"actions":
  - "desc": "*Melee Attack Roll:* +2, reach 5 ft. *Hit:* 2 (1d4) Bludgeoning damage."
    "name": "Ram"
"source":
  - "XMM"
"image": "/Compendium/bestiary/beast/token/deer-xmm.webp"
```
^statblock

## Environment

forest, grassland