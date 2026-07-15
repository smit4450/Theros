---
obsidianUIMode: preview
cssclasses:
- json5e-monster
tags:
- compendium/src/5e/xmm
- monster/cr/2
- monster/environment/arctic
- monster/environment/underwater
- monster/size/large
- monster/type/beast/dinosaur
statblock: inline
statblock-link: "#^statblock"
aliases:
- "Plesiosaurus"
---
# Plesiosaurus
*Source: Monster Manual (2024) p. 366. Available in the <span title='Systems Reference Document (5.2)'>SRD</span> and the Free Rules (2024)*
![](/Compendium/bestiary/beast/img/plesiosaurus.webp#right)

## Animals

Use these stat blocks to represent the creatures they're named for or other similar creatures. For example, the [Panther](/Compendium/bestiary/beast/panther-xmm.md) stat block can also represent a mountain lion, while the [Giant Goat](/Compendium/bestiary/beast/giant-goat-xmm.md) stat block might represent a buffalo. Any of these stat blocks might also serve as fantastical animals with distinctive names and cosmetic details unique to your D&D adventures.

> [!gallery]
![A druid calls on animals of the hills and mountains to aid her cause](/Compendium/bestiary/beast/img/animals-hills-and-mountains.webp)
![Aquatic animals swim alongside a druid exploring the sea](/Compendium/bestiary/beast/img/animals-aquatic.webp)
![Inhabitants of the rain forest answer a druid's summons](/Compendium/bestiary/beast/img/animals-rainforest.webp)

```statblock
"name": "Plesiosaurus"
"size": "Large"
"type": "beast"
"subtype": "dinosaur"
"alignment": "Unaligned"
"ac": !!int "13"
"hp": !!int "68"
"hit_dice": "8d10 + 24"
"modifier": !!int "2"
"stats":
  - !!int "18"
  - !!int "15"
  - !!int "16"
  - !!int "2"
  - !!int "12"
  - !!int "5"
"speed": "20 ft., swim 40 ft."
"skillsaves":
  - "name": "[Perception](/Compendium/rules/skills.md#Perception)"
    "desc": "+3"
  - "name": "[Stealth](/Compendium/rules/skills.md#Stealth)"
    "desc": "+4"
"senses": "passive Perception 13"
"languages": ""
"cr": "2"
"traits":
  - "desc": "The plesiosaurus can hold its breath for 1 hour."
    "name": "Hold Breath"
"actions":
  - "desc": "*Melee Attack Roll:* +6, reach 10 ft. *Hit:* 11 (2d6 + 4) Piercing damage."
    "name": "Bite"
"source":
  - "XMM"
"image": "/Compendium/bestiary/beast/token/plesiosaurus-xmm.webp"
```
^statblock

## Environment

arctic, underwater