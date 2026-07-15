---
obsidianUIMode: preview
cssclasses:
- json5e-monster
tags:
- compendium/src/5e/xmm
- monster/cr/3
- monster/environment/underwater
- monster/size/huge
- monster/type/beast
statblock: inline
statblock-link: "#^statblock"
aliases:
- "Killer Whale"
---
# Killer Whale
*Source: Monster Manual (2024) p. 364. Available in the <span title='Systems Reference Document (5.2)'>SRD</span> and the Free Rules (2024)*
![A druid calls on animals of the hills and mountains to aid her cause](/Compendium/bestiary/beast/img/animals-hills-and-mountains.webp#right)

## Animals

Use these stat blocks to represent the creatures they're named for or other similar creatures. For example, the [Panther](/Compendium/bestiary/beast/panther-xmm.md) stat block can also represent a mountain lion, while the [Giant Goat](/Compendium/bestiary/beast/giant-goat-xmm.md) stat block might represent a buffalo. Any of these stat blocks might also serve as fantastical animals with distinctive names and cosmetic details unique to your D&D adventures.

> [!gallery]
![Aquatic animals swim alongside a druid exploring the sea](/Compendium/bestiary/beast/img/animals-aquatic.webp)
![Inhabitants of the rain forest answer a druid's summons](/Compendium/bestiary/beast/img/animals-rainforest.webp)

```statblock
"name": "Killer Whale"
"size": "Huge"
"type": "beast"
"alignment": "Unaligned"
"ac": !!int "12"
"hp": !!int "90"
"hit_dice": "12d12 + 12"
"modifier": !!int "2"
"stats":
  - !!int "19"
  - !!int "14"
  - !!int "13"
  - !!int "3"
  - !!int "12"
  - !!int "7"
"speed": "5 ft., swim 60 ft."
"skillsaves":
  - "name": "[Perception](/Compendium/rules/skills.md#Perception)"
    "desc": "+3"
  - "name": "[Stealth](/Compendium/rules/skills.md#Stealth)"
    "desc": "+4"
"senses": "[Blindsight](/Compendium/rules/senses.md#Blindsight) 120 ft., passive Perception\
  \ 13"
"languages": ""
"cr": "3"
"traits":
  - "desc": "The whale can hold its breath for 30 minutes."
    "name": "Hold Breath"
"actions":
  - "desc": "*Melee Attack Roll:* +6, reach 5 ft. *Hit:* 21 (5d6 + 4) Piercing damage."
    "name": "Bite"
"source":
  - "XMM"
"image": "/Compendium/bestiary/beast/token/killer-whale-xmm.webp"
```
^statblock

## Environment

underwater