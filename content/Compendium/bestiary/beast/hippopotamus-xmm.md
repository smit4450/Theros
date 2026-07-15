---
obsidianUIMode: preview
cssclasses:
- json5e-monster
tags:
- compendium/src/5e/xmm
- monster/cr/4
- monster/environment/forest
- monster/environment/grassland
- monster/environment/swamp
- monster/size/large
- monster/type/beast
statblock: inline
statblock-link: "#^statblock"
aliases:
- "Hippopotamus"
---
# Hippopotamus
*Source: Monster Manual (2024) p. 362. Available in the <span title='Systems Reference Document (5.2)'>SRD</span> and the Free Rules (2024)*
![](/Compendium/bestiary/beast/img/hippopotamus.webp#right)

## Animals

Use these stat blocks to represent the creatures they're named for or other similar creatures. For example, the [Panther](/Compendium/bestiary/beast/panther-xmm.md) stat block can also represent a mountain lion, while the [Giant Goat](/Compendium/bestiary/beast/giant-goat-xmm.md) stat block might represent a buffalo. Any of these stat blocks might also serve as fantastical animals with distinctive names and cosmetic details unique to your D&D adventures.

> [!gallery]
![A druid calls on animals of the hills and mountains to aid her cause](/Compendium/bestiary/beast/img/animals-hills-and-mountains.webp)
![Aquatic animals swim alongside a druid exploring the sea](/Compendium/bestiary/beast/img/animals-aquatic.webp)
![Inhabitants of the rain forest answer a druid's summons](/Compendium/bestiary/beast/img/animals-rainforest.webp)

```statblock
"name": "Hippopotamus"
"size": "Large"
"type": "beast"
"alignment": "Unaligned"
"ac": !!int "14"
"hp": !!int "82"
"hit_dice": "11d10 + 22"
"modifier": !!int "-2"
"stats":
  - !!int "21"
  - !!int "7"
  - !!int "15"
  - !!int "2"
  - !!int "12"
  - !!int "4"
"speed": "30 ft., swim 30 ft."
"saves":
  - "strength": !!int "7"
"skillsaves":
  - "name": "[Perception](/Compendium/rules/skills.md#Perception)"
    "desc": "+3"
"senses": "passive Perception 13"
"languages": ""
"cr": "4"
"traits":
  - "desc": "The hippopotamus can hold its breath for 10 minutes."
    "name": "Hold Breath"
"actions":
  - "desc": "The hippopotamus makes two Bite attacks."
    "name": "Multiattack"
  - "desc": "*Melee Attack Roll:* +7, reach 5 ft. *Hit:* 16 (2d10 + 5) Piercing damage."
    "name": "Bite"
"source":
  - "XMM"
"image": "/Compendium/bestiary/beast/token/hippopotamus-xmm.webp"
```
^statblock

## Environment

forest, grassland, swamp