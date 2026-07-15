---
obsidianUIMode: preview
cssclasses:
- json5e-monster
tags:
- compendium/src/5e/xmm
- monster/cr/1-8
- monster/environment/coastal
- monster/environment/desert
- monster/environment/forest
- monster/environment/grassland
- monster/environment/hill
- monster/environment/swamp
- monster/size/tiny
- monster/type/beast
statblock: inline
statblock-link: "#^statblock"
aliases:
- "Venomous Snake"
---
# Venomous Snake
*Source: Monster Manual (2024) p. 372, Player's Handbook (2024) p. 358. Available in the <span title='Systems Reference Document (5.2)'>SRD</span> and the Free Rules (2024)*
![](/Compendium/bestiary/beast/img/swarm-of-venomous-snakes.webp#right)

## Animals

Use these stat blocks to represent the creatures they're named for or other similar creatures. For example, the [Panther](/Compendium/bestiary/beast/panther-xmm.md) stat block can also represent a mountain lion, while the [Giant Goat](/Compendium/bestiary/beast/giant-goat-xmm.md) stat block might represent a buffalo. Any of these stat blocks might also serve as fantastical animals with distinctive names and cosmetic details unique to your D&D adventures.

> [!gallery]
![A druid calls on animals of the hills and mountains to aid her cause](/Compendium/bestiary/beast/img/animals-hills-and-mountains.webp)
![Aquatic animals swim alongside a druid exploring the sea](/Compendium/bestiary/beast/img/animals-aquatic.webp)
![Inhabitants of the rain forest answer a druid's summons](/Compendium/bestiary/beast/img/animals-rainforest.webp)

```statblock
"name": "Venomous Snake"
"size": "Tiny"
"type": "beast"
"alignment": "Unaligned"
"ac": !!int "12"
"hp": !!int "5"
"hit_dice": "2d4"
"modifier": !!int "2"
"stats":
  - !!int "2"
  - !!int "15"
  - !!int "11"
  - !!int "1"
  - !!int "10"
  - !!int "3"
"speed": "30 ft., swim 30 ft."
"senses": "[Blindsight](/Compendium/rules/senses.md#Blindsight) 10 ft., passive Perception\
  \ 10"
"languages": ""
"cr": "1/8"
"actions":
  - "desc": "*Melee Attack Roll:* +4, reach 5 ft. *Hit:* 4 (1d4 + 2) Piercing damage\
      \ plus 3 (1d6) Poison damage."
    "name": "Bite"
"source":
  - "XMM"
  - "XPHB"
"image": "/Compendium/bestiary/beast/token/venomous-snake-xmm.webp"
```
^statblock

## Environment

coastal, desert, forest, grassland, hill, swamp