---
obsidianUIMode: preview
cssclasses:
- json5e-monster
tags:
- compendium/src/5e/xmm
- monster/cr/1
- monster/environment/arctic
- monster/environment/forest
- monster/environment/hill
- monster/size/large
- monster/type/beast
statblock: inline
statblock-link: "#^statblock"
aliases:
- "Brown Bear"
---
# Brown Bear
*Source: Monster Manual (2024) p. 350, Player's Handbook (2024) p. 347. Available in the <span title='Systems Reference Document (5.2)'>SRD</span> and the Free Rules (2024)*
![](/Compendium/bestiary/beast/img/brown-bear.webp#right)

## Animals

Use these stat blocks to represent the creatures they're named for or other similar creatures. For example, the [Panther](/Compendium/bestiary/beast/panther-xmm.md) stat block can also represent a mountain lion, while the [Giant Goat](/Compendium/bestiary/beast/giant-goat-xmm.md) stat block might represent a buffalo. Any of these stat blocks might also serve as fantastical animals with distinctive names and cosmetic details unique to your D&D adventures.

> [!gallery]
![A druid calls on animals of the hills and mountains to aid her cause](/Compendium/bestiary/beast/img/animals-hills-and-mountains.webp)
![Aquatic animals swim alongside a druid exploring the sea](/Compendium/bestiary/beast/img/animals-aquatic.webp)
![Inhabitants of the rain forest answer a druid's summons](/Compendium/bestiary/beast/img/animals-rainforest.webp)

```statblock
"name": "Brown Bear"
"size": "Large"
"type": "beast"
"alignment": "Unaligned"
"ac": !!int "11"
"hp": !!int "22"
"hit_dice": "3d10 + 6"
"modifier": !!int "1"
"stats":
  - !!int "17"
  - !!int "12"
  - !!int "15"
  - !!int "2"
  - !!int "13"
  - !!int "7"
"speed": "40 ft., climb 30 ft."
"skillsaves":
  - "name": "[Perception](/Compendium/rules/skills.md#Perception)"
    "desc": "+3"
"senses": "[Darkvision](/Compendium/rules/senses.md#Darkvision) 60 ft., passive Perception\
  \ 13"
"languages": ""
"cr": "1"
"actions":
  - "desc": "The bear makes one Bite attack and one Claw attack."
    "name": "Multiattack"
  - "desc": "*Melee Attack Roll:* +5, reach 5 ft. *Hit:* 7 (1d8 + 3) Piercing damage."
    "name": "Bite"
  - "desc": "*Melee Attack Roll:* +5, reach 5 ft. *Hit:* 5 (1d4 + 3) Slashing damage.\
      \ If the target is a Large or smaller creature, it has the [Prone](/Compendium/rules/conditions.md#Prone)\
      \ condition."
    "name": "Claw"
"source":
  - "XMM"
  - "XPHB"
"image": "/Compendium/bestiary/beast/token/brown-bear-xmm.webp"
```
^statblock

## Environment

arctic, forest, hill