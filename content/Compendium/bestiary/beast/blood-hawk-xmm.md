---
obsidianUIMode: preview
cssclasses:
- json5e-monster
tags:
- compendium/src/5e/xmm
- monster/cr/1-8
- monster/environment/arctic
- monster/environment/coastal
- monster/environment/forest
- monster/environment/grassland
- monster/environment/hill
- monster/environment/mountain
- monster/size/small
- monster/type/beast
statblock: inline
statblock-link: "#^statblock"
aliases:
- "Blood Hawk"
---
# Blood Hawk
*Source: Monster Manual (2024) p. 350. Available in the <span title='Systems Reference Document (5.2)'>SRD</span> and the Free Rules (2024)*
![](/Compendium/bestiary/beast/img/blood-hawk.webp#right)

## Animals

Use these stat blocks to represent the creatures they're named for or other similar creatures. For example, the [Panther](/Compendium/bestiary/beast/panther-xmm.md) stat block can also represent a mountain lion, while the [Giant Goat](/Compendium/bestiary/beast/giant-goat-xmm.md) stat block might represent a buffalo. Any of these stat blocks might also serve as fantastical animals with distinctive names and cosmetic details unique to your D&D adventures.

> [!gallery]
![A druid calls on animals of the hills and mountains to aid her cause](/Compendium/bestiary/beast/img/animals-hills-and-mountains.webp)
![Aquatic animals swim alongside a druid exploring the sea](/Compendium/bestiary/beast/img/animals-aquatic.webp)
![Inhabitants of the rain forest answer a druid's summons](/Compendium/bestiary/beast/img/animals-rainforest.webp)

```statblock
"name": "Blood Hawk"
"size": "Small"
"type": "beast"
"alignment": "Unaligned"
"ac": !!int "12"
"hp": !!int "7"
"hit_dice": "2d6"
"modifier": !!int "2"
"stats":
  - !!int "6"
  - !!int "14"
  - !!int "10"
  - !!int "3"
  - !!int "14"
  - !!int "5"
"speed": "10 ft., fly 60 ft."
"skillsaves":
  - "name": "[Perception](/Compendium/rules/skills.md#Perception)"
    "desc": "+6"
"senses": "passive Perception 16"
"languages": ""
"cr": "1/8"
"traits":
  - "desc": "The hawk has [Advantage](/Compendium/rules/variant-rules/advantage-xphb.md)\
      \ on an attack roll against a creature if at least one of the hawk's allies\
      \ is within 5 feet of the creature and the ally doesn't have the [Incapacitated](/Compendium/rules/conditions.md#Incapacitated)\
      \ condition."
    "name": "Pack Tactics"
"actions":
  - "desc": "*Melee Attack Roll:* +4, reach 5 ft. *Hit:* 4 (1d4 + 2) Piercing damage,\
      \ or 6 (1d8 + 2) Piercing damage if the target is [Bloodied](/Compendium/rules/conditions.md#Bloodied)."
    "name": "Beak"
"source":
  - "XMM"
"image": "/Compendium/bestiary/beast/token/blood-hawk-xmm.webp"
```
^statblock

## Environment

arctic, coastal, forest, grassland, hill, mountain