---
obsidianUIMode: preview
cssclasses:
- json5e-monster
tags:
- compendium/src/5e/xmm
- monster/cr/1-2
- monster/environment/urban
- monster/size/large
- monster/type/beast
statblock: inline
statblock-link: "#^statblock"
aliases:
- "Warhorse"
---
# Warhorse
*Source: Monster Manual (2024) p. 373, Player's Handbook (2024) p. 359. Available in the <span title='Systems Reference Document (5.2)'>SRD</span> and the Free Rules (2024)*
![](/Compendium/bestiary/beast/img/warhorse.webp#right)

## Animals

Use these stat blocks to represent the creatures they're named for or other similar creatures. For example, the [Panther](/Compendium/bestiary/beast/panther-xmm.md) stat block can also represent a mountain lion, while the [Giant Goat](/Compendium/bestiary/beast/giant-goat-xmm.md) stat block might represent a buffalo. Any of these stat blocks might also serve as fantastical animals with distinctive names and cosmetic details unique to your D&D adventures.

> [!gallery]
![A druid calls on animals of the hills and mountains to aid her cause](/Compendium/bestiary/beast/img/animals-hills-and-mountains.webp)
![Aquatic animals swim alongside a druid exploring the sea](/Compendium/bestiary/beast/img/animals-aquatic.webp)
![Inhabitants of the rain forest answer a druid's summons](/Compendium/bestiary/beast/img/animals-rainforest.webp)

```statblock
"name": "Warhorse"
"size": "Large"
"type": "beast"
"alignment": "Unaligned"
"ac": !!int "11"
"hp": !!int "19"
"hit_dice": "3d10 + 3"
"modifier": !!int "1"
"stats":
  - !!int "18"
  - !!int "12"
  - !!int "13"
  - !!int "2"
  - !!int "12"
  - !!int "7"
"speed": "60 ft."
"saves":
  - "wisdom": !!int "3"
"senses": "passive Perception 11"
"languages": ""
"cr": "1/2"
"actions":
  - "desc": "*Melee Attack Roll:* +6, reach 5 ft. *Hit:* 9 (2d4 + 4) Bludgeoning damage.\
      \ If the target is a Large or smaller creature and the horse moved 20+ feet\
      \ straight toward it immediately before the hit, the target takes an extra 5\
      \ (2d4) Bludgeoning damage and has the [Prone](/Compendium/rules/conditions.md#Prone)\
      \ condition."
    "name": "Hooves"
"source":
  - "XMM"
  - "XPHB"
"image": "/Compendium/bestiary/beast/token/warhorse-xmm.webp"
```
^statblock

## Environment

urban