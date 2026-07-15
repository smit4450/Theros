---
obsidianUIMode: preview
cssclasses:
- json5e-monster
tags:
- compendium/src/5e/xmm
- monster/cr/1-4
- monster/environment/coastal
- monster/environment/grassland
- monster/environment/mountain
- monster/size/medium
- monster/type/beast/dinosaur
statblock: inline
statblock-link: "#^statblock"
aliases:
- "Pteranodon"
---
# Pteranodon
*Source: Monster Manual (2024) p. 367. Available in the <span title='Systems Reference Document (5.2)'>SRD</span> and the Free Rules (2024)*
![](/Compendium/bestiary/beast/img/pteranodon.webp#right)

## Animals

Use these stat blocks to represent the creatures they're named for or other similar creatures. For example, the [Panther](/Compendium/bestiary/beast/panther-xmm.md) stat block can also represent a mountain lion, while the [Giant Goat](/Compendium/bestiary/beast/giant-goat-xmm.md) stat block might represent a buffalo. Any of these stat blocks might also serve as fantastical animals with distinctive names and cosmetic details unique to your D&D adventures.

> [!gallery]
![A druid calls on animals of the hills and mountains to aid her cause](/Compendium/bestiary/beast/img/animals-hills-and-mountains.webp)
![Aquatic animals swim alongside a druid exploring the sea](/Compendium/bestiary/beast/img/animals-aquatic.webp)
![Inhabitants of the rain forest answer a druid's summons](/Compendium/bestiary/beast/img/animals-rainforest.webp)

```statblock
"name": "Pteranodon"
"size": "Medium"
"type": "beast"
"subtype": "dinosaur"
"alignment": "Unaligned"
"ac": !!int "13"
"hp": !!int "13"
"hit_dice": "3d8"
"modifier": !!int "2"
"stats":
  - !!int "12"
  - !!int "15"
  - !!int "10"
  - !!int "2"
  - !!int "9"
  - !!int "5"
"speed": "10 ft., fly 60 ft."
"skillsaves":
  - "name": "[Perception](/Compendium/rules/skills.md#Perception)"
    "desc": "+1"
"senses": "passive Perception 11"
"languages": ""
"cr": "1/4"
"traits":
  - "desc": "The pteranodon doesn't provoke an Opportunity Attack when it flies out\
      \ of an enemy's reach."
    "name": "Flyby"
"actions":
  - "desc": "*Melee Attack Roll:* +4, reach 5 ft. *Hit:* 6 (1d8 + 2) Piercing damage."
    "name": "Bite"
"source":
  - "XMM"
"image": "/Compendium/bestiary/beast/token/pteranodon-xmm.webp"
```
^statblock

## Environment

coastal, grassland, mountain