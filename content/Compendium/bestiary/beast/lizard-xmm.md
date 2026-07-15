---
obsidianUIMode: preview
cssclasses:
- json5e-monster
tags:
- compendium/src/5e/xmm
- monster/cr/0
- monster/environment/coastal
- monster/environment/desert
- monster/environment/forest
- monster/environment/swamp
- monster/environment/underdark
- monster/size/tiny
- monster/type/beast
statblock: inline
statblock-link: "#^statblock"
aliases:
- "Lizard"
---
# Lizard
*Source: Monster Manual (2024) p. 364, Player's Handbook (2024) p. 353. Available in the <span title='Systems Reference Document (5.2)'>SRD</span> and the Free Rules (2024)*
![](/Compendium/bestiary/beast/img/lizard.webp#right)

## Animals

Use these stat blocks to represent the creatures they're named for or other similar creatures. For example, the [Panther](/Compendium/bestiary/beast/panther-xmm.md) stat block can also represent a mountain lion, while the [Giant Goat](/Compendium/bestiary/beast/giant-goat-xmm.md) stat block might represent a buffalo. Any of these stat blocks might also serve as fantastical animals with distinctive names and cosmetic details unique to your D&D adventures.

> [!gallery]
![A druid calls on animals of the hills and mountains to aid her cause](/Compendium/bestiary/beast/img/animals-hills-and-mountains.webp)
![Aquatic animals swim alongside a druid exploring the sea](/Compendium/bestiary/beast/img/animals-aquatic.webp)
![Inhabitants of the rain forest answer a druid's summons](/Compendium/bestiary/beast/img/animals-rainforest.webp)

```statblock
"name": "Lizard"
"size": "Tiny"
"type": "beast"
"alignment": "Unaligned"
"ac": !!int "10"
"hp": !!int "2"
"hit_dice": "1d4"
"modifier": !!int "0"
"stats":
  - !!int "2"
  - !!int "11"
  - !!int "10"
  - !!int "1"
  - !!int "8"
  - !!int "3"
"speed": "20 ft., climb 20 ft."
"senses": "[Darkvision](/Compendium/rules/senses.md#Darkvision) 30 ft., passive Perception\
  \ 9"
"languages": ""
"cr": "0"
"traits":
  - "desc": "The lizard can climb difficult surfaces, including along ceilings, without\
      \ needing to make an ability check."
    "name": "Spider Climb"
"actions":
  - "desc": "*Melee Attack Roll:* +2, reach 5 ft. *Hit:* 1 Piercing damage."
    "name": "Bite"
"source":
  - "XMM"
  - "XPHB"
"image": "/Compendium/bestiary/beast/token/lizard-xmm.webp"
```
^statblock

## Environment

coastal, desert, forest, swamp, underdark