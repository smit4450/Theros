---
obsidianUIMode: preview
cssclasses:
- json5e-monster
tags:
- compendium/src/5e/xmm
- monster/cr/1-2
- monster/environment/forest
- monster/size/medium
- monster/type/beast
statblock: inline
statblock-link: "#^statblock"
aliases:
- "Black Bear"
---
# Black Bear
*Source: Monster Manual (2024) p. 349, Player's Handbook (2024) p. 346. Available in the <span title='Systems Reference Document (5.2)'>SRD</span> and the Free Rules (2024)*
![](/Compendium/bestiary/beast/img/black-bear.webp#right)

## Animals

Use these stat blocks to represent the creatures they're named for or other similar creatures. For example, the [Panther](/Compendium/bestiary/beast/panther-xmm.md) stat block can also represent a mountain lion, while the [Giant Goat](/Compendium/bestiary/beast/giant-goat-xmm.md) stat block might represent a buffalo. Any of these stat blocks might also serve as fantastical animals with distinctive names and cosmetic details unique to your D&D adventures.

> [!gallery]
![A druid calls on animals of the hills and mountains to aid her cause](/Compendium/bestiary/beast/img/animals-hills-and-mountains.webp)
![Aquatic animals swim alongside a druid exploring the sea](/Compendium/bestiary/beast/img/animals-aquatic.webp)
![Inhabitants of the rain forest answer a druid's summons](/Compendium/bestiary/beast/img/animals-rainforest.webp)

```statblock
"name": "Black Bear"
"size": "Medium"
"type": "beast"
"alignment": "Unaligned"
"ac": !!int "11"
"hp": !!int "19"
"hit_dice": "3d8 + 6"
"modifier": !!int "1"
"stats":
  - !!int "15"
  - !!int "12"
  - !!int "14"
  - !!int "2"
  - !!int "12"
  - !!int "7"
"speed": "30 ft., climb 30 ft., swim 30 ft."
"skillsaves":
  - "name": "[Perception](/Compendium/rules/skills.md#Perception)"
    "desc": "+5"
"senses": "[Darkvision](/Compendium/rules/senses.md#Darkvision) 60 ft., passive Perception\
  \ 15"
"languages": ""
"cr": "1/2"
"actions":
  - "desc": "The bear makes two Rend attacks."
    "name": "Multiattack"
  - "desc": "*Melee Attack Roll:* +4, reach 5 ft. *Hit:* 5 (1d6 + 2) Slashing damage."
    "name": "Rend"
"source":
  - "XMM"
  - "XPHB"
"image": "/Compendium/bestiary/beast/token/black-bear-xmm.webp"
```
^statblock

## Environment

forest