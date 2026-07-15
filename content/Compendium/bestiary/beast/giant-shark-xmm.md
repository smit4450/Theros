---
obsidianUIMode: preview
cssclasses:
- json5e-monster
tags:
- compendium/src/5e/xmm
- monster/cr/5
- monster/environment/underwater
- monster/size/huge
- monster/type/beast
statblock: inline
statblock-link: "#^statblock"
aliases:
- "Giant Shark"
---
# Giant Shark
*Source: Monster Manual (2024) p. 359. Available in the <span title='Systems Reference Document (5.2)'>SRD</span> and the Free Rules (2024)*
![](/Compendium/bestiary/beast/img/hunter-shark.webp#right)

## Animals

Use these stat blocks to represent the creatures they're named for or other similar creatures. For example, the [Panther](/Compendium/bestiary/beast/panther-xmm.md) stat block can also represent a mountain lion, while the [Giant Goat](/Compendium/bestiary/beast/giant-goat-xmm.md) stat block might represent a buffalo. Any of these stat blocks might also serve as fantastical animals with distinctive names and cosmetic details unique to your D&D adventures.

> [!gallery]
![A druid calls on animals of the hills and mountains to aid her cause](/Compendium/bestiary/beast/img/animals-hills-and-mountains.webp)
![Aquatic animals swim alongside a druid exploring the sea](/Compendium/bestiary/beast/img/animals-aquatic.webp)
![Inhabitants of the rain forest answer a druid's summons](/Compendium/bestiary/beast/img/animals-rainforest.webp)

```statblock
"name": "Giant Shark"
"size": "Huge"
"type": "beast"
"alignment": "Unaligned"
"ac": !!int "13"
"hp": !!int "92"
"hit_dice": "8d12 + 40"
"modifier": !!int "3"
"stats":
  - !!int "23"
  - !!int "11"
  - !!int "21"
  - !!int "1"
  - !!int "10"
  - !!int "5"
"speed": "5 ft., swim 60 ft."
"skillsaves":
  - "name": "[Perception](/Compendium/rules/skills.md#Perception)"
    "desc": "+3"
"senses": "[Blindsight](/Compendium/rules/senses.md#Blindsight) 60 ft., passive Perception\
  \ 13"
"languages": ""
"cr": "5"
"traits":
  - "desc": "The shark can breathe only underwater."
    "name": "Water Breathing"
"actions":
  - "desc": "The shark makes two Bite attacks."
    "name": "Multiattack"
  - "desc": "*Melee Attack Roll:* +9 (with [Advantage](/Compendium/rules/variant-rules/advantage-xphb.md)\
      \ if the target doesn't have all its [Hit Points](/Compendium/rules/variant-rules/hit-points-xphb.md)),\
      \ reach 5 ft. *Hit:* 22 (3d10 + 6) Piercing damage."
    "name": "Bite"
"source":
  - "XMM"
"image": "/Compendium/bestiary/beast/token/giant-shark-xmm.webp"
```
^statblock

## Environment

underwater