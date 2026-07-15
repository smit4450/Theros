---
obsidianUIMode: preview
cssclasses:
- json5e-monster
tags:
- compendium/src/5e/xmm
- monster/cr/0
- monster/environment/desert
- monster/environment/forest
- monster/environment/grassland
- monster/environment/urban
- monster/size/tiny
- monster/type/beast
statblock: inline
statblock-link: "#^statblock"
aliases:
- "Cat"
---
# Cat
*Source: Monster Manual (2024) p. 351, Player's Handbook (2024) p. 347. Available in the <span title='Systems Reference Document (5.2)'>SRD</span> and the Free Rules (2024)*
![](/Compendium/bestiary/beast/img/cat.webp#right)

## Animals

Use these stat blocks to represent the creatures they're named for or other similar creatures. For example, the [Panther](/Compendium/bestiary/beast/panther-xmm.md) stat block can also represent a mountain lion, while the [Giant Goat](/Compendium/bestiary/beast/giant-goat-xmm.md) stat block might represent a buffalo. Any of these stat blocks might also serve as fantastical animals with distinctive names and cosmetic details unique to your D&D adventures.

> [!gallery]
![A druid calls on animals of the hills and mountains to aid her cause](/Compendium/bestiary/beast/img/animals-hills-and-mountains.webp)
![Aquatic animals swim alongside a druid exploring the sea](/Compendium/bestiary/beast/img/animals-aquatic.webp)
![Inhabitants of the rain forest answer a druid's summons](/Compendium/bestiary/beast/img/animals-rainforest.webp)

```statblock
"name": "Cat"
"size": "Tiny"
"type": "beast"
"alignment": "Unaligned"
"ac": !!int "12"
"hp": !!int "2"
"hit_dice": "1d4"
"modifier": !!int "2"
"stats":
  - !!int "3"
  - !!int "15"
  - !!int "10"
  - !!int "3"
  - !!int "12"
  - !!int "7"
"speed": "40 ft., climb 40 ft."
"saves":
  - "dexterity": !!int "4"
"skillsaves":
  - "name": "[Perception](/Compendium/rules/skills.md#Perception)"
    "desc": "+3"
  - "name": "[Stealth](/Compendium/rules/skills.md#Stealth)"
    "desc": "+4"
"senses": "[Darkvision](/Compendium/rules/senses.md#Darkvision) 60 ft., passive Perception\
  \ 13"
"languages": ""
"cr": "0"
"traits":
  - "desc": "The cat's jump distance is determined using its Dexterity rather than\
      \ its Strength."
    "name": "Jumper"
"actions":
  - "desc": "*Melee Attack Roll:* +4, reach 5 ft. *Hit:* 1 Slashing damage."
    "name": "Scratch"
"source":
  - "XMM"
  - "XPHB"
"image": "/Compendium/bestiary/beast/token/cat-xmm.webp"
```
^statblock

## Environment

desert, forest, grassland, urban