---
obsidianUIMode: preview
cssclasses:
- json5e-monster
tags:
- compendium/src/5e/xmm
- monster/cr/1-4
- monster/environment/coastal
- monster/environment/desert
- monster/environment/forest
- monster/environment/grassland
- monster/environment/hill
- monster/environment/swamp
- monster/size/medium
- monster/type/beast
statblock: inline
statblock-link: "#^statblock"
aliases:
- "Giant Venomous Snake"
---
# Giant Venomous Snake
*Source: Monster Manual (2024) p. 361. Available in the <span title='Systems Reference Document (5.2)'>SRD</span> and the Free Rules (2024)*
![](/Compendium/bestiary/beast/img/swarm-of-venomous-snakes.webp#right)

## Animals

Use these stat blocks to represent the creatures they're named for or other similar creatures. For example, the [Panther](/Compendium/bestiary/beast/panther-xmm.md) stat block can also represent a mountain lion, while the [Giant Goat](/Compendium/bestiary/beast/giant-goat-xmm.md) stat block might represent a buffalo. Any of these stat blocks might also serve as fantastical animals with distinctive names and cosmetic details unique to your D&D adventures.

> [!gallery]
![A druid calls on animals of the hills and mountains to aid her cause](/Compendium/bestiary/beast/img/animals-hills-and-mountains.webp)
![Aquatic animals swim alongside a druid exploring the sea](/Compendium/bestiary/beast/img/animals-aquatic.webp)
![Inhabitants of the rain forest answer a druid's summons](/Compendium/bestiary/beast/img/animals-rainforest.webp)

```statblock
"name": "Giant Venomous Snake"
"size": "Medium"
"type": "beast"
"alignment": "Unaligned"
"ac": !!int "14"
"hp": !!int "11"
"hit_dice": "2d8 + 2"
"modifier": !!int "4"
"stats":
  - !!int "10"
  - !!int "18"
  - !!int "13"
  - !!int "2"
  - !!int "10"
  - !!int "3"
"speed": "40 ft., swim 40 ft."
"skillsaves":
  - "name": "[Perception](/Compendium/rules/skills.md#Perception)"
    "desc": "+2"
"senses": "[Blindsight](/Compendium/rules/senses.md#Blindsight) 10 ft., passive Perception\
  \ 12"
"languages": ""
"cr": "1/4"
"actions":
  - "desc": "*Melee Attack Roll:* +6, reach 10 ft. *Hit:* 6 (1d4 + 4) Piercing damage\
      \ plus 4 (1d8) Poison damage."
    "name": "Bite"
"source":
  - "XMM"
"image": "/Compendium/bestiary/beast/token/giant-venomous-snake-xmm.webp"
```
^statblock

## Environment

coastal, desert, forest, grassland, hill, swamp