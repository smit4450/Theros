---
obsidianUIMode: preview
cssclasses:
- json5e-monster
tags:
- compendium/src/5e/xmm
- monster/cr/1
- monster/environment/forest
- monster/environment/grassland
- monster/size/large
- monster/type/beast
statblock: inline
statblock-link: "#^statblock"
aliases:
- "Tiger"
---
# Tiger
*Source: Monster Manual (2024) p. 371, Player's Handbook (2024) p. 358. Available in the <span title='Systems Reference Document (5.2)'>SRD</span> and the Free Rules (2024)*
![](/Compendium/bestiary/beast/img/tiger.webp#right)

## Animals

Use these stat blocks to represent the creatures they're named for or other similar creatures. For example, the [Panther](/Compendium/bestiary/beast/panther-xmm.md) stat block can also represent a mountain lion, while the [Giant Goat](/Compendium/bestiary/beast/giant-goat-xmm.md) stat block might represent a buffalo. Any of these stat blocks might also serve as fantastical animals with distinctive names and cosmetic details unique to your D&D adventures.

> [!gallery]
![A druid calls on animals of the hills and mountains to aid her cause](/Compendium/bestiary/beast/img/animals-hills-and-mountains.webp)
![Aquatic animals swim alongside a druid exploring the sea](/Compendium/bestiary/beast/img/animals-aquatic.webp)
![Inhabitants of the rain forest answer a druid's summons](/Compendium/bestiary/beast/img/animals-rainforest.webp)

```statblock
"name": "Tiger"
"size": "Large"
"type": "beast"
"alignment": "Unaligned"
"ac": !!int "13"
"hp": !!int "30"
"hit_dice": "4d10 + 8"
"modifier": !!int "3"
"stats":
  - !!int "17"
  - !!int "16"
  - !!int "14"
  - !!int "3"
  - !!int "12"
  - !!int "8"
"speed": "40 ft."
"skillsaves":
  - "name": "[Perception](/Compendium/rules/skills.md#Perception)"
    "desc": "+3"
  - "name": "[Stealth](/Compendium/rules/skills.md#Stealth)"
    "desc": "+7"
"senses": "[Darkvision](/Compendium/rules/senses.md#Darkvision) 60 ft., passive Perception\
  \ 13"
"languages": ""
"cr": "1"
"actions":
  - "desc": "*Melee Attack Roll:* +5, reach 5 ft. *Hit:* 10 (2d6 + 3) Slashing damage.\
      \ If the target is a Large or smaller creature, it has the [Prone](/Compendium/rules/conditions.md#Prone)\
      \ condition."
    "name": "Rend"
"bonus_actions":
  - "desc": "The tiger takes the [Disengage](/Compendium/rules/actions.md#Disengage)\
      \ or [Hide](/Compendium/rules/actions.md#Hide) action."
    "name": "Nimble Escape"
"source":
  - "XMM"
  - "XPHB"
"image": "/Compendium/bestiary/beast/token/tiger-xmm.webp"
```
^statblock

## Environment

forest, grassland